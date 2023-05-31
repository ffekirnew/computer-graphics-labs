import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

triangle_vertices = (
    (0, 1, 0),
    (-1, -1, 0),
    (1, -1, 0)
)


def Triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0, 0.5)  # Purple color
    for vertex in triangle_vertices:
        glVertex3fv(vertex)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Triangle")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        Triangle()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
