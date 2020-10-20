#==============================================================================
#Comparing the size of point cloud
#==============================================================================import numpy as np
import open3d


pcd = open3d.geometry.PointCloud()
np_points = np.random.rand(1000000, 3)
pcd.points = open3d.utility.Vector3dVector(np_points)


formats = [".ply", ".pcd", ".pts", ".xyz"]
for i in formats:
    open3d.io.write_point_cloud("output"+i,pcd)
