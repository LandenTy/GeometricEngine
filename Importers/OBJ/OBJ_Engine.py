"""
Engine

Description:
"""
import random

class Unpack_Obj:
    
    def __init__(self, vertex=[], faces=[]):
        self.vertex = vertex
        self.faces = faces
        
    def unpack_obj_from_file(self, filename):
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    self.vertex.append([round(float(i)) for i in line.split()[1:]])
                
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    self.faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
            
class Material:
    
    def __init__(self, (r,g,b)):
        self.mat = tuple([r,g,b])
        
    def color(self):
        return self.mat

def Save_Data(filename,obj,obj_name,mats):
    c = 0
    vertex = "    vertices = "
    face = "    faces = "
    color = "    colors = "

    with open(filename, 'w') as f:
        
        # Setting up class
        f.write("class " + obj_name + ":\n")
        
        for i in range(len(obj.vertex)): # Writing Vertices
            vertex += str(tuple(obj.vertex[i])) + ","
        
        f.write(vertex + "\n")
        for j in range(len(obj.faces)): # Writing Faces
            face += str(tuple(obj.faces[j])) + ","
        
        f.write(face + "\n")
        for k in range(len(obj.faces)): # Writing Colors
            color += str(mats[c].color()) + ","
            
            if c < len(mats) - 1:
                c += 1
            else:
                c = 0
        
        f.write(color + "\n\n")
        f.write("   def Translate(self,pos=(0,0,0)):\n")
        f.write("       x,y,z = pos\n")
        f.write("       self.verts = [(x + X/2,y + Y/2,z + Z/2) for X,Y,Z in self.vertices]\n\n")
        f.write("   def __init__(self,pos=(0,0,0)):\n")
        f.write("       x,y,z = pos\n")
        f.write("       self.Translate((x,y,z))")
        
        print("Finished!")
        print("You may now close the window...")
