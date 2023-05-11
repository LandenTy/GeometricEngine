"""
IMAGES

Description: A Collection of Developer-Made Test Images :D
"""
# Modules
import pygame
pygame.init()

class Rock:
    def __init__(self,bg_color,pos=(0,0)):
        self.pos = list(pos)
        self.img = pygame.Surface([250, 250])
        self.img.fill(bg_color)

        # Drawing Code Goes Here
        pygame.draw.polygon(self.img,(0, 0, 0),[(19, 19), (238, 229), (64, 172)])
        pygame.draw.polygon(self.img,(0, 0, 0),[(56, 200), (211, 241), (8, 239)])
        pygame.draw.polygon(self.img,(211, 211, 211),[(236, 226), (238, 183), (22, 18)])
        pygame.draw.polygon(self.img,(220, 220, 220),[(22, 18), (192, 131), (236, 181)])

class Testing:
    def __init__(self,bg_color,pos=(0,0)):
        self.pos = list(pos)
        self.img = pygame.Surface([125, 125])
        self.img.fill(bg_color)

        # Drawing Code Goes Here
        pygame.draw.polygon(self.img,(0, 0, 0),[(8, 5), (121, 6), (122, 45)])
        pygame.draw.polygon(self.img,(255, 255, 0),[(5, 13), (120, 52), (6, 57)])
        pygame.draw.polygon(self.img,(255, 0, 0),[(120, 60), (7, 63), (117, 88)])
        pygame.draw.polygon(self.img,(0, 255, 0),[(10, 76), (8, 118), (113, 96)])
        pygame.draw.polygon(self.img,(0, 0, 255),[(113, 101), (44, 117), (113, 121)])
        
