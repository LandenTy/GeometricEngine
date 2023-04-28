"""
Camera

Description:
"""
import pygame,math,time
pygame.init()

# Functions
def rotate2d(pos, rad): 
    x,y = pos
    s,c = math.sin(rad),math.cos(rad)
    
    return x * c - y * s, y * c + x * s

# Classes
class Camera:
    
    def __init__(self,pos=(0, 0, 0),rot=(0,0),speed=1,jumpHeight=5):
        self.pos = list(pos)
        self.rot = list(rot)
        self.speed = speed
        self.jumpHeight = jumpHeight
    
    def Mouse_Controller(self, event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x /= 200
            y /= 200
            
            self.rot[0] += y
            self.rot[1] += x
 
    def Rotate(self, dt, key):
        s = dt * 1.5
        
        # Rotate
        if key[pygame.K_RIGHT]: self.rot[1] += s
        if key[pygame.K_LEFT]: self.rot[1] -= s
        
        if key[pygame.K_DOWN]: self.rot[0] += s
        if key[pygame.K_UP]: self.rot[0] -= s
        
    def Move(self, dt, key):
        s = dt * 3 # X Rotation
        
        # Flying
        if key[pygame.K_q]: self.pos[1] += s
        if key[pygame.K_e]: self.pos[1] -= s
        
        # Normalize Rotation
        x,z = s * math.sin(self.rot[1]), s * math.cos(self.rot[1])
        
        # Arrows
        if key[pygame.K_w]: # Forward
            self.pos[0] += x * self.speed
            self.pos[2] += z * self.speed
            
        if key[pygame.K_s]: # Backward
            self.pos[0] -= x * self.speed
            self.pos[2] -= z * self.speed
            
        if key[pygame.K_a]: # Strafe Left
            self.pos[0] -= z * self.speed
            self.pos[2] += x * self.speed
            
        if key[pygame.K_d]: # Strafe Right
            self.pos[0] += z * self.speed
            self.pos[2] -= x * self.speed
        
        # Running (LShift & RShift)
        if pygame.key.get_mods() == 2: self.speed = 2
        else: self.speed = 1
        
        if key[pygame.K_SPACE]: # Jumping
            print("Jumping!")
    
class Scene:
        
    def CreateScene(sceneList, (w,h)):
        scene = pygame.display.set_mode([w,h])
        return scene

class Material:
    
    def __init__(self, (r,g,b)):
        self.mat = tuple([r,g,b])
        
    def color(self):
        return self.mat
