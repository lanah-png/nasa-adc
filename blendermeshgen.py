import bpy 
import math 

# Settings 
name = 'mesh' 

verts = []
faces = []


# Utility Functions 
def vert(x,y,z): 
    """ Make a vertex """ 
    return (x, y, z) 

# generate verts
file = open("squarefulldatascale1.txt", "r")
s = file.read().split("\n")

size = len(s)

#separate txt file by linebreaks

for x in range(0, size-1):
    values = s[x].split(",")
    for y in range(0, size-1):
        verts.append(vert(x, y, float(values[y])))

#face stuff that might not work
faces = [(i, i - 1, i - 1 + size, i + size) for i in range( 1, len(verts) - size ) if i % size != 0]


#mesh setup
new_mesh = bpy.data.meshes.new('new_mesh')
new_mesh.from_pydata(verts, [], faces)
new_mesh.update()

# make object from mesh
new_object = bpy.data.objects.new(name, new_mesh)
#smooth shading
for p in new_object.data.polygons:
    p.use_smooth = True
# make collection
new_collection = bpy.data.collections.new('new_collection')
bpy.context.scene.collection.children.link(new_collection)
#add object to scene collection
new_collection.objects.link(new_object)
