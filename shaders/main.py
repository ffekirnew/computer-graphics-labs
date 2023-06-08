import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *

import numpy as np

from pyramid.definition import pyramid_vertices, pyramid_edges, pyramid_surfaces, pyramid


def getFileContent(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content


def load_shaders():
    print("Loading Shaders")
    # read Shader File content
    vertex_shader_content = getFileContent("vertex_shader.glsl")
    fragment_shader_content = getFileContent("fragment_shader.glsl")
    # compile Shader content
    vertex_shader = compileShader(vertex_shader_content, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment_shader_content, GL_FRAGMENT_SHADER)
    # Compile shader program
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)


def draw():
    pyramid(pyramid_vertices, pyramid_edges, pyramid_surfaces)


def main():
    pygame.init()
    display = (800, 600)

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Shaders")

    load_shaders()

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

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
