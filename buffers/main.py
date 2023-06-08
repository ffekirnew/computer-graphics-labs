import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Vertex data for a square
squareVertices = np.array([
    0.5, 0.5, 0.0,  # Top right
    0.5, -0.5, 0.0,  # Bottom right
    -0.5, -0.5, 0.0,  # Bottom left
    -0.5, 0.5, 0.0  # Top left
], dtype=np.float32)

# Vertex data for a triangle
triangleVertices = np.array([
    -0.5, -0.5, 0.0,  # Bottom left
    0.5, -0.5, 0.0,  # Bottom right
    0.0, 0.5, 0.0  # Top
], dtype=np.float32)


def create_square():
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, squareVertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return vao


def create_triangle():
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo)
    glBufferData(GL_ARRAY_BUFFER, triangleVertices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
    glEnableVertexAttribArray(0)

    glBindVertexArray(0)
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    return vao


def main():
    # Initialize Pygame and create a window
    pygame.init()
    width, height = 800, 600
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    # Create the square and triangle
    square_vao = create_square()
    triangle_vao = create_triangle()

    # Set up the OpenGL viewport
    glViewport(0, 0, width, height)
    glClearColor(0.2, 0.3, 0.4, 1.0)

    # Rendering loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        # # Render the square
        # glBindVertexArray(square_vao)
        # glDrawArrays(GL_TRIANGLE_FAN, 0, 4)

        # Render the triangle
        glBindVertexArray(triangle_vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)

        # Swap buffers
        pygame.display.flip()


if name == "main":
    main()
