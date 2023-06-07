import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import numpy.random as npr

from snake import Snake, Coordinate
from food import Food


def main():
    snake = Snake()
    # generate food placed at a random location
    random_coordinate = Coordinate(npr.randint(0, 20), npr.randint(0, 20))
    food = Food(random_coordinate)
    movement_direction = Coordinate(1, 0)

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movement_direction = Coordinate(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    movement_direction = Coordinate(1, 0)
                elif event.key == pygame.K_UP:
                    movement_direction = Coordinate(0, 1)
                elif event.key == pygame.K_DOWN:
                    movement_direction = Coordinate(0, -1)
                elif event.key == pygame.K_SPACE:
                    snake.extend()

        if abs(snake.get_location().x - food.get_location().x) < 1 and abs(
                snake.get_location().y - food.get_location().y) < 1:
            snake.extend()
            random_coordinate = Coordinate(npr.randint(0, 20), npr.randint(0, 20))
            food.move(random_coordinate.x, random_coordinate.y)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        snake.move(movement_direction)
        snake.draw()
        food.draw()
        pygame.display.flip()
        pygame.time.wait(100)


if __name__ == "__main__":
    main()
