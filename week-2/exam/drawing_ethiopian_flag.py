import pygame
from pygame.locals import *


def main():
    pygame.init()
    display = (500, 400)
    pygame.display.set_mode(display)
    pygame.display.set_caption("My Canvas")

    canvas = pygame.display.get_surface()
    canvas.fill((255, 255, 255))  # Fill canvas with white color

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False

        pygame.draw.line(canvas, (255, 0, 0), (50, 50),
                         (250, 50), 3)  # Draw a red line

        # Draw Ethiopian flag
        pygame.draw.rect(canvas, (0, 128, 0),
                         (50, 100, 400, 100))  # Green rectangle
        pygame.draw.rect(canvas, (255, 255, 0),
                         (50, 200, 400, 100))  # Yellow rectangle
        pygame.draw.rect(canvas, (255, 0, 0),
                         (50, 300, 400, 100))  # Red rectangle

        # Draw a purple point in the middle
        pygame.draw.circle(canvas, (128, 0, 128), (250, 250), 5)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
