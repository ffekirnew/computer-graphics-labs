from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np


class Cube:
    def __init__(self):
        self.vertices = np.array([
            [-0.5, -0.5, -0.5],
            [0.5, -0.5, -0.5],
            [0.5, 0.5, -0.5],
            [-0.5, 0.5, -0.5],
            [-0.5, -0.5, 0.5],
            [0.5, -0.5, 0.5],
            [0.5, 0.5, 0.5],
            [-0.5, 0.5, 0.5]
        ], dtype=np.float32)

        self.indices = np.array([
            [0, 1, 2],
            [2, 3, 0],
            [1, 5, 6],
            [6, 2, 1],
            [7, 6, 5],
            [5, 4, 7],
            [4, 0, 3],
            [3, 7, 4],
            [4, 5, 1],
            [1, 0, 4],
            [3, 2, 6],
            [6, 7, 3]
        ], dtype=np.uint32)

        self.colors = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 1],
            [0.5, 0, 0],
            [0, 0.5, 0],
            [0, 0, 0.5],
            [0.5, 0.5, 0],
            [0.5, 0, 0.5],
            [0, 0.5, 0.5]
        ], dtype=np.float32)

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        #
        # self.vbo = glGenBuffers(1)
        # glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        # glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        #
        # glEnableVertexAttribArray(0)
        # glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        #
        # self.cbo = glGenBuffers(1)
        # glBindBuffer(GL_ARRAY_BUFFER, self.cbo)
        # glBufferData(GL_ARRAY_BUFFER, self.colors.nbytes, self.colors, GL_STATIC_DRAW)
        #
        # glEnableVertexAttribArray(1)
        # glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        #
        # self.ebo = glGenBuffers(1)
        # glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        # glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.indices.nbytes, self.indices, GL_STATIC_DRAW)
        #
        # glBindVertexArray(0)

    def render(self):
        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, len(self.indices) * 3, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)

    @staticmethod
    def rotate(angle, x, y, z):
        glRotatef(angle, x, y, z)
