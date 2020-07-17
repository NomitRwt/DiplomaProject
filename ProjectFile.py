import open3d as o3d
import numpy as np
import copy


# PART ONE: Working on self generated point cloud------------------------------------------------------------------------

# 1.

outlier_pcd = o3d.io.read_point_cloud("Electrical Pole.ply")
o3d.visualization.draw_geometries([outlier_pcd])


# Interactive Viusalization
def demo_crop_geometry():
    print("Demo for manual geometry cropping")
    print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
    print("2) Press 'K' to lock screen and to switch to selection mode")
    print("3) Drag for rectangle selection,")
    print("   or use ctrl + left click for polygon selection")
    print("4) Press 'C' to get a selected geometry and to save it")
    print("5) Press 'F' to switch to freeview mode")
    pcd = o3d.io.read_point_cloud("Electrical Pole.ply")
    o3d.visualization.draw_geometries_with_editing([pcd])
    return


demo_crop_geometry()


# See inlier and outlier point cloud
def display_inlier_outlier(outpcl, inpcl):
    out_new = outpcl.paint_uniform_color([1, 0, 0])
    in_new = inpcl.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([in_new, out_new])


# 2.

# Statistical method
inlier_pcd_stat, ind_stat = outlier_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
display_inlier_outlier(outlier_pcd, inlier_pcd_stat)

# Radius method
inlier_pcd_rad, ind_rad = outlier_pcd.remove_radius_outlier(nb_points=16, radius=1)
display_inlier_outlier(outlier_pcd, inlier_pcd_rad)

# 3.

# Surface reconstruction

# Alpha Shapes
alpha = 0.1
alpha_shape = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(inlier_pcd_rad, alpha)
o3d.visualization.draw_geometries([alpha_shape])

# Ball Pivoting
# PreRequisite: Vertex Normals Estimation
inlier_pcd_rad.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
radii = [0.005, 0.01, 0.02, 0.04]
ball_pivoting = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(inlier_pcd_rad,
                                                                                o3d.utility.DoubleVector(radii))
o3d.visualization.draw_geometries([inlier_pcd_rad, ball_pivoting])

# Poissons
with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
    poissons, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(inlier_pcd_rad, depth=15)
    o3d.visualization.draw_geometries([poissons])


# PART TWO: Working on point cloud ITC building scans--------------------------------------------------------------------
# Convert numpy to point cloud
point_cloud_one = np.loadtxt("Scan_one.txt", delimiter=',')
pcd_one = o3d.geometry.PointCloud()
pcd_one.points = o3d.utility.Vector3dVector(point_cloud_one[:, 1:4])

# Repeat the procedure for the second scan
point_cloud_two = np.loadtxt("Scan_two.txt", delimiter=',')
pcd_two = o3d.geometry.PointCloud()
pcd_two.points = o3d.utility.Vector3dVector(point_cloud_two[:, 1:4])

# Down-sampling the voxels for efficient visualization
downpcd_one = pcd_one.voxel_down_sample(voxel_size=0.05)
downpcd_two = pcd_two.voxel_down_sample(voxel_size=0.05)


# Manuel Registration

# Drawing the registration result with transformation
def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


# Define a function to pick points in the point cloud
def pick_points(pcd):
    print("")
    print("1) Please pick at least three correspondences using [shift + left click]")
    print("Press [shift + right click] to undo point picking")
    print("2) Afther picking points, press q for close the window")
    vis = o3d.visualization.VisualizerWithEditing()
    vis.create_window()
    vis.add_geometry(pcd)
    vis.run()  # user picks points
    vis.destroy_window()
    print("")
    return vis.get_picked_points()


def demo_manual_registration():
    print("Demo for manual ICP")
    source = downpcd_one
    target = downpcd_two
    print("Visualization of two point clouds before manual alignment")
    draw_registration_result(source, target, np.identity(4))

    # pick points from two point clouds and builds correspondences
    picked_id_source = pick_points(source)
    picked_id_target = pick_points(target)
    assert (len(picked_id_source) >= 3 and len(picked_id_target) >= 3)
    assert (len(picked_id_source) == len(picked_id_target))
    corr = np.zeros((len(picked_id_source), 2))
    corr[:, 0] = picked_id_source
    corr[:, 1] = picked_id_target

    # estimate rough transformation using correspondences
    print("Compute a rough transform using the correspondences given by user")
    p2p = o3d.registration.TransformationEstimationPointToPoint()
    trans_init = p2p.compute_transformation(source, target, o3d.utility.Vector2iVector(corr))

    # point-to-point ICP for refinement
    print("Perform point-to-point ICP refinement")
    threshold = 0.03  # 3cm distance threshold
    reg_p2p = o3d.registration.registration_icp(source, target, threshold, trans_init,
                                                o3d.registration.TransformationEstimationPointToPoint())
    draw_registration_result(source, target, reg_p2p.transformation)
    print("")


demo_manual_registration()



# PART THREE: Working on benchmark dataset (Redwood)---------------------------------------------------------------------
#Robust Reconstruction
#Check Readme.md