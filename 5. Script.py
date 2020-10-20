#==============================================================================
#Comparing the size of mesh outputs
#==============================================================================
import open3d


mesh = open3d.io.read_triangle_mesh("Datasets/dragon_recon/dragon_vrip.ply")

formats = [".off", ".obj", ".ply", ".glb"]
for i in formats:
    open3d.io.write_triangle_mesh("Binary"+i, mesh, write_ascii = False)
    open3d.io.write_triangle_mesh("ASCII"+i, mesh, write_ascii = True)

# .stl format requires vertex normals
mesh.compute_vertex_normals()
open3d.io.write_triangle_mesh("Binary.stl", mesh, write_ascii = False)
open3d.io.write_triangle_mesh("ASCII.stl", mesh, write_ascii = True)
