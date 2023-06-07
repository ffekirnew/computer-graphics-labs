import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from shader import Shader
from cube import Cube
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


def main():
    # Initialize Pygame
    pygame.init()
    width, height = 800, 600
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    # Create a shader program
    shader_program = Shader("vertex_shader.glsl", "fragment_shader.glsl")

    # Create a cube object
    cube = Cube()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Clear the screen
        glClearColor(0.2, 0.2, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Set up the shader program
        shader_program.use()

        # Rotate the cube
        cube.rotate(0.5, 1, 1, 1)

        # Render the cube
        cube.render()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
