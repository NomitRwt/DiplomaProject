#==============================================================================
#Reading format on cloud compare
#==============================================================================
import open3d


format_list = ["ASCII cloud.txt", "CloudCompare entities.bin", "DXF geometry.dxf", "E57 cloud.e57", "LAS 1.3 or 1.4.las", "LAS cloud.las", "PLY mesh ASCII.ply", "PLY mesh binary.ply", "Point Cloud Library cloud.pcd", "Point+ Value cloud.pv", "Point+Normal cloud.pn", "SHP entity.shp", "Simple binary file.sbf", "Simple binary file.sbf.data", "VTK cloud or mesh.vtk"]
for i in format_list:
    point_cloud = open3d.io.read_point_cloud("Datasets/Cloud Compare Outputs/"+i)
