import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (0, -1, 1),  # 0
    (0, 1, 1),  # 1
    (5, -1, 1),  # 2
    (5, 1, 1),  # 3
    (5, -1, -1),  # 4
    (5, 1, -1),  # 5
    (2, 1, -1),  # 6
    (2, -1, -1),  # 7
    (0, -1, -5),  # 8
    (0, 1, -5),  # 9
    (2, 1, -5),  # 10
    (2, -1, -5),  # 11

)

edges = (
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 3),
    (3, 5),
    (2, 4),
    (4, 5),
    (5, 6),
    (4, 7),
    (6, 7),
    (6, 10),
    (7, 11),
    (0, 8),
    (1, 9),
    (8, 9),
    (9, 10),
    (8, 11),
    (10, 11),
)


def translate(translation_vector, vertices):
    a, b, c = translation_vector

    translated = []
    for x, y, z in vertices:
        translated.append((x + a, y + b, z + c))

    return translated


def draw_shape(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        glColor3f(0.0, 1.0, 0.0)  # Set the color (green in this example)
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display
    gluPerspective(90, (display[0] / display[1]), 0.1, 15.0)
    glTranslatef(0, 0, -5)  # Move the pyramid away from the camera

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_shape(translate((0, -1, 3), vertices), edges)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
