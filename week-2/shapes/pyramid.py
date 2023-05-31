import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pyramid_vertices = (
    (0, 1, 0),
    (-1, -1, 1),
    (1, -1, 1),
    (1, -1, -1),
    (-1, -1, -1)
)

pyramid_faces = (
    (0, 1, 2),
    (0, 2, 3),
    (0, 3, 4),
    (0, 4, 1),
    (1, 3, 2),
    (4, 3, 1)
)

pyramid_edges = (
    (0, 1),
    (0, 2),
    (0, 3),
    (0, 4),
    (1, 2),
    (1, 4),
    (2, 3),
    (3, 4),
)


def Pyramid(pyramid_vertices, pyramid_faces):
    glBegin(GL_TRIANGLES)
    for face in pyramid_faces:
        for vertex in face:
            glColor3f(1.0, 0.0, 0.0)  # Set the color (red in this example)
            glVertex3fv(pyramid_vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in pyramid_edges:
        glColor3f(0.0, 1.0, 0.0)  # Set the color (green in this example)
        for vertex in edge:
            glVertex3fv(pyramid_vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display
    gluPerspective(45, (display[0] / display[1]), 0.1, 15.0)
    glTranslatef(0, 0, -5)  # Move the pyramid away from the camera
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Pyramid(pyramid_vertices, pyramid_faces)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
