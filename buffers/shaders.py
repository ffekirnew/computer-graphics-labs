import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import numpy as np

# Vertex shader source code
vertex_shader = """
#version 330
layout (location = 0) in vec3 position;
void main()
{
    gl_Position = vec4(position, 1.0);
}
"""

# Fragment shader source code
fragment_shader = """
#version 330
out vec4 fragColor;
void main()
{
    fragColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

# Vertex data for a square
squareVertices = np.array([
    0.5, 0, 0.0,  # Top right
    0.5, -0.75, 0.0,  # Bottom right
    -0.5, -0.75, 0.0,  # Bottom left
    -0.5, 0, 0.0  # Top left
], dtype=np.float32)

# Vertex data for a triangle
triangleVertices = np.array([
    -0.5, 0.25, 0.0,  # Bottom left
    0.5, 0.25, 0.0,  # Bottom right
    0.0, 0.9, 0.0  # Top
], dtype=np.float32)


def create_shader(shader_type, source):
    shader = compileShader(source, shader_type)
    return shader


def create_program(vertex_shader, fragment_shader):
    program = compileProgram(vertex_shader, fragment_shader)
    return program


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


def main():
    # Initialize Pygame and create a window
    pygame.init()
    width, height = 800, 600
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    # Create the square and triangle
    square_vao = create_square()

    # Create the shader program
    vertex_shader_obj = create_shader(GL_VERTEX_SHADER, vertex_shader)
    fragment_shader_obj = create_shader(GL_FRAGMENT_SHADER, fragment_shader)
    shader_program = create_program(vertex_shader_obj, fragment_shader_obj)

    # Use the shader program
    glUseProgram(shader_program)

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

        # Draw the square
        glBindVertexArray(square_vao)
        glDrawArrays(GL_QUADS, 0, 4)

        # Swap the buffers
        pygame.display.flip()


if __name__ == "__main__":
    main()
