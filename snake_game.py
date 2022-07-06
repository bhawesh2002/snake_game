import sys
import os
import pygame
from pygame.locals import *

pygame.init()

width,height = 600,600
window = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption("!!!SNAKE!!!")
white = (255,255,225)
while True:
    window.fill(white)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and K_q):
            pygame.quit()
            sys.exit()