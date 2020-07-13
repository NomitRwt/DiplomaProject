import open3d as o3d
import numpy as np
import matplotlib as plt


#PART ONE: Working on self generated point cloud------------------------------------------------------------------------

#outlier_pcd = o3d.io.read_point_cloud("Electrical Pole.ply")
#o3d.visualization.draw_geometries([pcd])

#Interactive Viusalization
#def demo_crop_geometry():
#    print("Demo for manual geometry cropping")
#    print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
#    print("2) Press 'K' to lock screen and to switch to selection mode")
#    print("3) Drag for rectangle selection,")
#    print("   or use ctrl + left click for polygon selection")
#    print("4) Press 'C' to get a selected geometry and to save it")
#    print("5) Press 'F' to switch to freeview mode")
#    pcd = o3d.io.read_point_cloud("Electrical Pole.ply")
#    o3d.visualization.draw_geometries_with_editing([pcd])
#    return

#demo_crop_geometry()

#See inlier and outlier point cloud
#def display_inlier_outlier(outpcl, inpcl):
#    out_new = outpcl.paint_uniform_color([1, 0, 0])
#    in_new = inpcl.paint_uniform_color([0.8, 0.8, 0.8])
#    o3d.visualization.draw_geometries([in_new, out_new])


#2.
#Statistical method
#inlier_pcd_stat, ind_stat = outlier_pcd.remove_statistical_outlier(nb_neighbors=20, std_ratio=2.0)
#display_inlier_outlier(outlier_pcd, inlier_pcd_stat)

#Radius method
#inlier_pcd_rad, ind_rad = outlier_pcd.remove_radius_outlier(nb_points=16, radius=1)
#display_inlier_outlier(outlier_pcd, inlier_pcd_rad)


#3
#Surface reconstruction

#Alpha Shapes
#alpha = 0.1
#alpha_shape = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(inlier_pcd_rad, alpha)
#o3d.visualization.draw_geometries([alpha_shape])

#Ball Pivoting
#PreReqquisite: Vertex Normals Estimation
#inlier_pcd_rad.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
#radii = [0.005, 0.01, 0.02, 0.04]
#ball_pivoting = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(inlier_pcd_rad, o3d.utility.DoubleVector(radii))
#o3d.visualization.draw_geometries([inlier_pcd_rad, ball_pivoting])

#Poissons
#with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
#    poissons, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(inlier_pcd_rad, depth=15)
#    #o3d.visualization.draw_geometries([poissons])


#PART TWO: Working on point cloud ITC building scans--------------------------------------------------------------------
#sample = o3d.io.read_point_cloud("Sample.txt",format='xyz')
#o3d.visualization.draw_geometries([sample])

#data = np.loadtxt("Sample.txt",delimiter=',')
