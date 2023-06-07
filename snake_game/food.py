from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from snake import Coordinate


class Food:
    size = 0.5

    def __init__(self, coordinate: Coordinate):
        self.x = coordinate.x
        self.y = coordinate.y

    def get_location(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def draw(self):
        # draw a circular food
        glBegin(GL_POLYGON)
        glColor3fv((1, 1, 0))
        for i in range(360):
            glVertex3fv((self.x + self.size * np.cos(i), self.y + self.size * np.sin(i), 0))
        glEnd()

    def move(self, x, y):
        self.x = x
        self.y = y


# test the code using pygame
if __name__ == "__main__":
    import pygame
    from pygame.locals import *

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -50)

    food = Food(Coordinate(0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        food.draw()
        pygame.display.flip()
        pygame.time.wait(100)
