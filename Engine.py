"""
3D Engine

Description: (Without Matrix Projection) OpenGL-like 3D Cube!
(TECHSMART Compatible!)
"""
# Libraries
import pygame,math,sys
pygame.init()

# Functions
def rotate2d(pos, rad): 
    x,y = pos
    s,c = math.sin(rad),math.cos(rad)
    
    return x * c - y * s, y * c + x * s

# Classes
class Camera:
    
    def __init__(self, pos=(0, 0, 0), rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)
    
    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x /= 200
            y /= 200
            
            self.rot[0] += y
            self.rot[1] += x
    
    def Move(self, dt, key):
        s = dt * 5
        
        # Fly
        if key[pygame.K_e]: self.pos[1] += s
        if key[pygame.K_q]: self.pos[1] -= s
        
        # Arrows
        if key[pygame.K_w]: self.pos[2] += s
        if key[pygame.K_s]: self.pos[2] -= s
        if key[pygame.K_d]: self.pos[0] += s
        if key[pygame.K_a]: self.pos[0] -= s

# PyGame Variables
w, h = 800, 600
cx, cy = w // 2, h // 2
screen = pygame.display.set_mode([w, h])
clock = pygame.time.Clock()
BACKGROUND = (0,0,0)

# Cursor Settings
pygame.event.get()
pygame.mouse.set_visible(0)

# Camera
cam = Camera((0, 0, -5))

# Verts and Edges
verts = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
edges = (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
colors = (255,0,0),(255,128,0),(255,255,0),(255,255,255),(0,0,255),(0,255,0)

# Draw Loop
while True:
    fps = clock.tick(60)
    dt = fps / 1000
    
    for e in pygame.event.get():
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                print(clock.get_fps())
                sys.exit()
        
        cam.events(e)
    
    screen.fill(BACKGROUND)
    
    vert_list = []
    screen_coords = []
    for x,y,z in verts:
        
        # Vertices
        x -= cam.pos[0]
        y -= cam.pos[1]
        z -= cam.pos[2]
            
        x,z = rotate2d((x,z), cam.rot[1])
        y,z = rotate2d((y,z), cam.rot[0])
        vert_list += [(x,y,z)]
        
        # Screen Coordinates
        f = 200 / z
        x,y = x * f, y * f
        screen_coords += [(cx + int(x), cy + int(y))]
    
    face_list = []
    face_color = []
    depth = []
    
    for f in range(len(faces)):
        face = faces[f]
        
        on_screen = False
        for i in face:
            if vert_list[i][2] > 0:
                on_screen = True
                break
        
        if on_screen:
            # Coloring Faces
            coords = [screen_coords[i] for i in face]
            face_list += [coords]
            face_color += [colors[f]]
            
            # Ordering Depth Layers
            depth += [sum(sum(vert_list[j][i]/len(face) for j in face)**2 for i in range(3))]
    
    order = sorted(range(len(face_list)),key=lambda i:depth[i], reverse=1)
    
    for i in order:
        pygame.draw.polygon(screen, face_color[i], face_list[i])
    
    pygame.display.flip()
    
    # Camera Controller
    key = pygame.key.get_pressed()
    cam.Move(dt, key)
