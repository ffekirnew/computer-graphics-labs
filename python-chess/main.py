from sys import exit
from pygame.locals import *
import pygame
background_image_filename = "images/background.png"
mouse_image_filename = "images/python-logo.jpg"


pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello, World")

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(background, (0, 0))

        x, y = pygame.mouse.get_pos()

        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2

        screen.blit(mouse_cursor, (x, y))

        pygame.display.update()
