"""
Engine

Description: (Without Matrix Projection) OpenGL-like 3D Cube!
"""
# Modules
from Camera import * # Contains Camera Controller and Other Stuff
from Primitives import * # Contains all 3D Shapes

# Libraries
import pygame,random,sys
pygame.init()
        
# PyGame Variables
w, h = 1240, 720
cx, cy = w // 2, h // 2
screen = pygame.display.set_mode([w, h])
clock = pygame.time.Clock()

# Scene
s0 = Scene()
scene0 = s0.CreateScene((w,h))
BACKGROUND_COLOR = (129, 236, 236)

# Camera
cam = Camera((0, -3, -15)) # Player Controller

# Objects
objects = [Ground_OBJ((0,0,0)), Cube((3,0,0)), Cube((3,3,0))]

while(1):
    key = pygame.key.get_pressed()
    dt = clock.tick(20) / 1000
    
    for e in pygame.event.get():
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                print(clock.get_fps())
                sys.exit()
            
    scene0.fill(BACKGROUND_COLOR)
    
    face_list = []
    face_color = []
    depth = []
    
    for obj in objects: # Loads Objects from 'Objects' list
        
        vert_list = []
        screen_coords = []
        for x,y,z in obj.verts:
            
            # Vertices
            x -= cam.pos[0]
            y -= cam.pos[1]
            z -= cam.pos[2]
                
            x,z = rotate2d((x,z), cam.rot[1])
            y,z = rotate2d((y,z), cam.rot[0])
            vert_list += [(x,y,z)]
            
            # Camera Settings 
            f = 200 / z
            x,y = x * f, y * f
            screen_coords += [(cx + int(x), cy + int(y))]
        
        for f in range(len(obj.faces)):
            face = obj.faces[f]
            
            on_screen = True
            for i in face:
                x,y = screen_coords[i]
                if vert_list[i][2] > 0 and x > 0 and x < w and x and y > 0 and y < h:
                    on_screen = True
                    break
            
            if on_screen:
                # Coloring Faces
                coords = [screen_coords[i] for i in face]
                face_list += [coords]
                face_color += [obj.colors[f]]
                
                # Ordering Depth Layers
                depth += [sum(sum(vert_list[j][i]/len(face) for j in face)**2 for i in range(3))]
    
    order = sorted(range(len(face_list)),key=lambda i:depth[i],reverse=1)
    
    for i in order:
        try: pygame.draw.polygon(scene0, face_color[i], face_list[i],width=0)
        except: pass
    
    pygame.display.flip()
    
    cam.Rotate(dt,key)
    cam.Move(dt,key)
