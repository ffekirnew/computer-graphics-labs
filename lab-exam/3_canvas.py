# Draw a 500 by 400 pixel canvas using pygame. Make it in a function named main. Set the title of your canvas. Add an event to your canvas so that it quits when Key A is pressed in your keyboard. Fill the canvas with white color.
import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (160, 32, 240)

def main():
    pygame.init()
    display = (500, 400)
    pygame.display.set_mode(display)
    pygame.display.set_caption("Lab Exam 1")

    canvas = pygame.display.get_surface()
    canvas.fill((255, 255, 255))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    running = False

        pygame.draw.line(canvas, RED, (50, 50), (250, 50), 3)
        pygame.draw.polygon(canvas, RED, [(250, 80), (80, 230), (420, 230)], 0)
        pygame.draw.polygon(canvas, BLUE, [(250, 380), (80, 230), (420, 230)], 0)
        pygame.draw.circle(canvas, PURPLE, (250, 230), 5, 0)

        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()