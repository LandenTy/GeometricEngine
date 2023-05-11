"""
Example

Description: Showcasing the use of Example Images from 'Images.py'
"""
from IMAGES import *
import pygame,sys
pygame.init()

w,h = (1920,1080)
win = pygame.display.set_mode([w,h])

img1 = Rock((255,255,255),(0,0))
img2 = Testing((255,255,255),(0,0))
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
    
    win.fill((125,125,125))
    win.blit(img1.img,(0,0))
    win.blit(img2.img,(0,0))
    
    pygame.display.flip()
