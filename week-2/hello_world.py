import pygame
from pygame.locals import *
from sys import exit

pygame.init()
pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World")
# Did the user click the window close button?
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
