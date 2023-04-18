"""
Primitives

Description:
"""
class Cube:
    vertices = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1),(-1,1,1)
    faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
    colors = (255,0,0),(255,128,0),(255,255,0),(255,255,255),(0,0,255),(0,255,0)
    
    def Translate(self, pos=(0,0,0)):
        x,y,z = pos     
        self.verts = [(x + X/2,y + Y/2,z + Z/2) for X,Y,Z in self.vertices]
    
    def __init__(self, pos=(0,0,0)):
        x,y,z = pos     
        self.Translate((x,y,z))
    
    def Collider(self, offset=(0,0,0)):
        return offset

"""
Custom OBJ Loading
"""
class Unpack_Obj:
    
    def __init__(self, vertex=[], faces=[]):
        self.vertex = vertex
        self.faces = faces
        
    def unpack_obj_from_file(self, filename):
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    self.vertex.append([float(i) for i in line.split()[1:]])
                
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    self.faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])

class Ground_OBJ:
    
    vertices = (-0.07, -0.0, 27.5),(-47, 0.0, -27.5),(-0.07, 0.0, -27.5),(-47, -0.0, 27.5),(-47, 1.0, 27.5),(-47, 1.0, -27.5),(-0.07, 1.0, 27.5),(-0.07, 1.0, -27.5)
    faces = (1, 2, 0, 3),(4, 5, 1, 3),(6, 4, 3, 0),(5, 7, 2, 1),(7, 6, 0, 2),(7, 5, 4, 6)
    colors = (0,255,0),(0,255,0),(0,255,0),(39, 174, 96),(39, 174, 96),(39, 174, 96)
    
    def Translate(self, pos=(0,0,0)):
        x,y,z = pos     
        self.verts = [(x + X/2,y + Y/2,z + Z/2) for X,Y,Z in self.vertices]
    
    def __init__(self, pos=(0,0,0)):
        x,y,z = pos     
        self.Translate((x,y,z))
    
    def Collider(self, offset=(0,0,0)):
        return offset
