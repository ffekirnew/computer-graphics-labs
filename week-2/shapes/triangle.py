import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


pyramid_vertices = [
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
    (0, 0, -1),
    (-1, 0, 0),
]

pyramid_edges = [
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 4),
    (2, 3),
    (3, 4),
]


def draw_pyramid():
    glBegin(GL_LINES)
    for edge in pyramid_edges:
        for vertex in edge:
            glVertex3fv(pyramid_vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display
    gluPerspective(120, (display[0] / display[1]), 0.1, 50.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_pyramid()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
