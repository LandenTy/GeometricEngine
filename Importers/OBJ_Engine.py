"""
OBJ_Engine

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

def Save_Data(filename, obj, mats):
    c = 0
    with open(filename, 'w') as f:
        for i in range(len(obj.vertex)): # Writing Vertices
            f.write(str(tuple(obj.vertex[i])))
            f.write(",")
        
        f.write("\n\n")
        for j in range(len(obj.faces)): # Writing Faces
            f.write(str(tuple(obj.faces[j])))
            f.write(",")
        
        f.write("\n\n")
        for k in range(len(obj.faces)):
            f.write(str(mats[c].color()))
            f.write(",")
            
            if c < len(mats) - 1:
                c += 1
            else:
                c = 0
        
        print("Finished!")
        print("You may now close the window...")
