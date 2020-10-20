#==============================================================================
#Comparing the read time of .pcd, .ply, .pts, .xyz
#==============================================================================
import open3d as o3d
import numpy as np
import time


i = 0
iteration = []
time_taken_pcd = []
while(i<=100):
    i = i + 1
    iteration.append(i)
    start = time.perf_counter_ns()
    point_cloud = o3d.io.read_point_cloud("Datasets/Output/output.pcd")
    stop = time.perf_counter_ns()
    t = stop-start
    time_taken_pcd.append(t)

print(np.mean(time_taken_pcd),"Mean time for .pcd")

i = 0
time_taken_ply = []
while(i<=100):
    i = i + 1
    start = time.perf_counter_ns()
    point_cloud = o3d.io.read_point_cloud("Datasets/Output/output.ply")
    stop = time.perf_counter_ns()
    t = stop-start
    time_taken_ply.append(t)

print(np.mean(time_taken_ply),"Polygon file format =")

i = 0
time_taken_pts = []
while(i<=100):
    i = i + 1
    start = time.perf_counter_ns()
    point_cloud = o3d.io.read_point_cloud("Datasets/Output/output.pts")
    stop = time.perf_counter_ns()
    t = stop-start
    time_taken_pts.append(t)

print( np.mean(time_taken_pts),"Laser scan plain format")

i = 0
time_taken_xyz = []
while(i<=100):
    i = i + 1
    start = time.perf_counter_ns()
    point_cloud = o3d.io.read_point_cloud("Datasets/Output/output.xyz")
    stop = time.perf_counter_ns()
    t = stop-start
    time_taken_xyz.append(t)

print(np.mean(time_taken_xyz),"XYZ")


import matplotlib.pyplot as plt
plt.plot(iteration, time_taken_pcd)
plt.plot(iteration, time_taken_ply)
plt.plot(iteration, time_taken_pts, "r")
plt.plot(iteration, time_taken_xyz)
plt.title('the fastest format', size = 19)
plt.xlabel('Iteration', size = 19)
plt.ylabel('Time (nano seconds)', size = 19)
plt.show()
