from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

def draw_line(x1, y1, x2, y2):
    
    glColor3f(255, 255, 255)

    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)

    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw_line(0, 0, 500, 500)

        pygame.display.flip()

if __name__ == "__main__":
    main()