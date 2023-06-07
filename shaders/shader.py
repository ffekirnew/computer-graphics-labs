from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

class Shader:
    def __init__(self, vertex_shader_file, fragment_shader_file):
        self.program = compileProgram(
            self.load_shader(vertex_shader_file, GL_VERTEX_SHADER),
            self.load_shader(fragment_shader_file, GL_FRAGMENT_SHADER)
        )
        self.uniform_model = glGetUniformLocation(self.program, "model")
        self.uniform_view = glGetUniformLocation(self.program, "view")
        self.uniform_projection = glGetUniformLocation(self.program, "projection")

    def load_shader(self, filename, shader_type):
        with open(filename, 'r') as file:
            shader_code = file.read()
        shader = compileShader(shader_code, shader_type)
        return shader

    def use(self):
        glUseProgram(self.program)
