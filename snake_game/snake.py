import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# create a named tuple for the coordinates
from collections import namedtuple

Coordinate = namedtuple("Coordinate", ["x", "y"])


class Segment:
    size = 1

    def __init__(self, x, y, is_head):
        self.x = x
        self.y = y
        self.is_head = is_head

    def get_location(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def move(self, direction: Coordinate):
        self.x += direction.x
        self.y += direction.y

    def goto(self, location: Coordinate):
        self.x = location.x
        self.y = location.y

    def draw(self):
        glBegin(GL_QUADS)
        if self.is_head:
            glColor3fv((1, 0, 0))
        else:
            glColor3fv((0, 1, 0))
        glVertex3fv((self.x, self.y, 0))
        glVertex3fv((self.x + self.size, self.y, 0))
        glVertex3fv((self.x + self.size, self.y + self.size, 0))
        glVertex3fv((self.x, self.y + self.size, 0))
        glEnd()


class Snake:
    start_size = 20

    def __init__(self):
        self.segments = []
        for i in range(self.start_size):
            self.segments.append(Segment(-1 * i * Segment.size, 0, i == 0))

    def get_location(self):
        return self.segments[0].get_location()

    def extend(self):
        last_segment = self.segments[-1]
        self.segments.append(Segment(last_segment.x - Segment.size, last_segment.y, False))

    def draw(self) -> None:
        for segment in self.segments:
            segment.draw()

    def move(self, direction: Coordinate) -> None:
        for i in range(len(self.segments) - 1, -1, -1):
            segment = self.segments[i]
            if i == 0:
                segment.move(direction)
            else:
                previous_segment = self.segments[i - 1]
                segment.goto(previous_segment.get_location())
