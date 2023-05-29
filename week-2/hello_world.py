import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World")
# Did the user click the window close button?
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    quit()
    pygame.display.update()
