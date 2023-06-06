import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define the parameters of the celestial bodies
sun_radius = 1.5
earth_radius = 0.7
moon_radius = 0.2
sun_distance = 0.0
earth_distance = 5.0
moon_distance = 1.5
rotation_speed = 1.0


def draw_sphere(radius):
    slices = 64
    stacks = 64
    gluSphere(gluNewQuadric(), radius, slices, stacks)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20.0)  # Move the camera back

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(rotation_speed, 0, 1, 0)  # Rotate the entire scene

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the Sun
        glColor3f(1.0, 0.7, 0.0)  # Set color to yellow
        glPushMatrix()
        glRotatef(rotation_speed, 0, 1, 0)  # Rotate the Sun
        draw_sphere(sun_radius)
        glPopMatrix()

        # Draw the Earth
        glColor3f(0.0, 0.7, 1.0)  # Set color to blue
        glPushMatrix()
        glRotatef(rotation_speed, 0, 1, 0)  # Rotate the Earth
        # Move the Earth away from the Sun
        glTranslatef(earth_distance, 0.0, 0.0)
        # Rotate the Earth around its own axis
        glRotatef(rotation_speed, 0, 1, 0)
        draw_sphere(earth_radius)

        # Draw the Moon
        glColor3f(0.7, 0.7, 0.7)  # Set color to gray
        glPushMatrix()
        glRotatef(2 * rotation_speed, 0, 1, 0)  # Rotate the Moon
        # Move the Moon away from the Earth
        glTranslatef(moon_distance, 0.0, 0.0)
        # Rotate the Moon around its own axis
        glRotatef(rotation_speed, 0, 1, 0)
        draw_sphere(moon_radius)
        glPopMatrix()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
