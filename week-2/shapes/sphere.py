import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from math import *


def draw_sphere():
    radius = 4
    slices = 128
    stacks = 128

    for i in range(stacks):
        color = (1.0, 0.0, 0.0) if i % 2 == 0 else (0.0, 0.0, 1.0)
        glColor3fv(color)

        lat0 = pi * (-0.5 + float(float(i - 1) / stacks))
        z0 = sin(lat0)
        zr0 = cos(lat0)

        lat1 = pi * (-0.5 + float(float(i) / stacks))
        z1 = sin(lat1)
        zr1 = cos(lat1)

        # Draw the current stack as a quad strip
        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * pi * float(float(j - 1) / slices)
            x = cos(lng)
            y = sin(lng)

            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0 * radius, y * zr0 * radius, z0 * radius)

            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1 * radius, y * zr1 * radius, z1 * radius)
        glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display
    gluPerspective(110, (display[0] / display[1]), 0.1, 15.0)
    glTranslatef(0.0, 0.0, -5.0)  # Move the objects away from the camera

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)  # Rotate the objects

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the sphere
        draw_sphere()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
