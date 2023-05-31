import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def draw_line(x1, y1, x2, y2):
    gluOrtho2D(0, 800, 0, 600)

    glBegin(GL_LINES)
    glColor3f(0, 0, 1)  # Blue color
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Line")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)

        draw_line(100, 100, 400, 300)

        pygame.display.flip()
        pygame.time.wait(20)


if __name__ == "__main__":
    main()
