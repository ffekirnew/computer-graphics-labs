import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *

import numpy as np


def draw():
    pass


def main():
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Shaders")

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        draw()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
