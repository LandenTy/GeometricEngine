"""
Camera

Description:
"""
import pygame, math
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
    
    def Mouse_Controller(self, event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel
            x /= 200
            y /= 200
            
            self.rot[0] += y
            self.rot[1] += x
    
    def Reset(self, key):
        if key[pygame.K_r]: 
            self.pos[0] = 0 
            self.pos[1] = 0 
            self.pos[2] = -5
            
            self.rot[1] = 0
            self.rot[0] = 0
 
    def Rotate(self, dt, key):
        s = dt * 1.5
        
        # Rotate
        if key[pygame.K_RIGHT]: self.rot[1] += s
        if key[pygame.K_LEFT]: self.rot[1] -= s
        
        if key[pygame.K_DOWN]: self.rot[0] += s
        if key[pygame.K_UP]: self.rot[0] -= s
        
    def Move(self, dt, key, flyCam):
        s = dt * 3 # X Rotation
        
        if flyCam:
            
            # Fly
            if key[pygame.K_q]: self.pos[1] -= s # Fly Up
            if key[pygame.K_e]: self.pos[1] += s # Fly Down
        
        # Arrows
        if key[pygame.K_w]: self.pos[2] += s # Forward
        if key[pygame.K_s]: self.pos[2] -= s # Backward
        if key[pygame.K_d]: self.pos[0] += s # Right
        if key[pygame.K_a]: self.pos[0] -= s # Left
    
    def CheckDrawFaces():
        
        return

class Scene:
        
    def CreateScene(sceneList, (w,h)):
        scene = pygame.display.set_mode([w,h])
        return scene
