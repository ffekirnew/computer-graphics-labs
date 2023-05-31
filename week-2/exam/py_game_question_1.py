import pygame
from pygame.locals import *


def main():
    pygame.init()
    display = (500, 400)  # setting size here
    pygame.display.set_mode(display)
    pygame.display.set_caption("Lab Exam")

    canvas = pygame.display.get_surface()
    canvas.fill((255, 255, 255))  # Fill canvas with white color

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:  # handling space key pressed
                if event.key == pygame.K_SPACE:
                    running = False

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
