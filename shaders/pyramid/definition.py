from OpenGL.GL import *
from OpenGL.GLU import *

pyramid_vertices = [
    (0, 1, 0),  # top
    (-1, -1, 1),  # front left
    (1, -1, 1),  # front right
    (1, -1, -1),  # back right
    (-1, -1, -1)  # back left
]

# edges of the pyramid
pyramid_edges = [
    (0, 1),  # top-front left
    (0, 2),  # top-front right
    (0, 3),  # top-back right
    (0, 4),  # top-back left
    (1, 2),  # front left-right
    (2, 3),  # front right-back right
    (3, 4),  # back right-back left
    (4, 1)  # back left-front left
]

# surfaces of the pyramid
pyramid_surfaces = [
    (0, 1, 2),  # front
    (0, 2, 3),  # right
    (0, 3, 4),  # back
    (0, 4, 1),  # left
    (1, 2, 3, 4)  # bottom
]


def pyramid(vertices, edges, surfaces):
    glBegin(GL_TRIANGLES)
    for surface in surfaces:
        for vertex in surface:
            glColor3fv((1, 0, 0))
            glVertex3fv(vertices[vertex])
    glEnd()

    # draw edges
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1, 1, 1))  # white
            glVertex3fv(vertices[vertex])
    glEnd()
