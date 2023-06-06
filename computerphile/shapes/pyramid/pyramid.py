# initialize and start working on a pygame and opengl project to draw a pyramid

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from commons import pyramid_vertices, pyramid_edges, pyramid_surfaces, pyramid
from transformations import Transformation


def move_pyramid(event, new_vertices):
    if event.key == pygame.K_LEFT:
        translated_vertices = Transformation.translate((-0.25, 0, 0), new_vertices)
    elif event.key == pygame.K_RIGHT:
        translated_vertices = Transformation.translate((0.25, 0, 0), new_vertices)
    elif event.key == pygame.K_UP:
        translated_vertices = Transformation.translate((0, 0.25, 0), new_vertices)
    elif event.key == pygame.K_DOWN:
        translated_vertices = Transformation.translate((0, -0.25, 0), new_vertices)

    return translated_vertices


def zoom_pyramid(event, new_vertices):
    if event.y == 1:
        zoomed_vertices = Transformation.scale((1.1, 1.1, 1.1), new_vertices)
    elif event.y == -1:
        zoomed_vertices = Transformation.scale((0.9, 0.9, 0.9), new_vertices)

    return zoomed_vertices


def rotate_pyramid(event, new_vertices):
    return new_vertices


# now write the main function, a simplistic main function and the pyramid should not rotate
def main(pyramid_vertices, pyramid_edges, pyramid_surfaces):
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # set the right perspective to be from the right angle, and write comment about the usage of the parameters
    # glPerspective(fov, aspect ratio, near clipping plane, far clipping plane)
    # fov: field of view, how much you can see
    # aspect ratio: width / height
    # near clipping plane: how close you can see
    # far clipping plane: how far you can see
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    # move the camera back by 5 units
    glTranslatef(0.0, 0.0, -5)

    new_vertices = pyramid_vertices
    paused = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                else:
                    new_vertices = move_pyramid(event, new_vertices)

            elif event.type == pygame.MOUSEWHEEL:
                if event.y == 1 or event.y == -1:
                    new_vertices = zoom_pyramid(event, new_vertices)
                else:
                    new_vertices = rotate_pyramid(event, new_vertices)

        if not paused:
            # rotate the pyramid, and write comment about it

            # glRotatef(angle, x, y, z)
            # angle: the angle of rotation
            # x, y, z: the axis of rotation
            # glRotatef(1, 3, 1, 1) means rotate 1 degree around the axis (3, 1, 1)
            # glRotatef(1, 4, 1, 4) means rotate 1 degree around the axis (4, 1, 4)
            glRotatef(4, 1, 1, 1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        pyramid(new_vertices, pyramid_edges, pyramid_surfaces)
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == '__main__':
    main(pyramid_vertices, pyramid_edges, pyramid_surfaces)
