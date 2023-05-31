import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

cube_vertices = (
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (1, -1, 1),
    (-1, 1, 1),
    (-1, -1, -1),
    (-1, -1, 1),
    (-1, 1, -1)
)


def scale_down(vertices, factor):
    scaled_down = []
    for x, y, z in vertices:
        scaled_down.append((x * factor, y * factor, z * factor))

    return scaled_down


cube_edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 7),
    (2, 5),
    (2, 3),
    (3, 6),
    (4, 6),
    (4, 7),
    (5, 6),
    (5, 7)
)


def Cube(cube_vertices):
    glBegin(GL_LINES)
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display
    gluPerspective(110, (display[0] / display[1]), 0.1, 15.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Cube(scale_down(cube_vertices, 0.2))
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
