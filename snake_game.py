import sys
import os
import pygame
from pygame.locals import *

pygame.init()

width,height = 600,600
window = pygame.display.set_mode((width,height))
caption = pygame.display.set_caption("!!!SNAKE!!!")
white = (255,255,225)
red = (255,0,0)
green_snake = pygame.image.load(os.path.join('Assets','green snake.png'))
orange_snake = pygame.image.load(os.path.join('Assets','snake orange.png'))
run = True
while run:
    window.fill(white)
    window.blit(green_snake,(400,400))
    window.blit(orange_snake,(200,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and K_q):
            pygame.quit()
            sys.exit()