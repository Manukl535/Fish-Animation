import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
from math import sin, cos

# Global variables
fish_positions = {
    'fish1': [-1.0, 0.0],  # Start on the left side
    'fish2': [-0.8, -0.2],  # Start on the left side
    'fish3': [0.8, 0.2],    # Start on the right side
    'fish4': [0.6, -0.2],   # Start on the right side
    'fish5': [0.4, 0.0]     # Start on the right side
}

fish_directions = {
    'fish1': -1,  # Move to the left
    'fish2': -1,  # Move to the left
    'fish3': -1,  # Move to the left
    'fish4': -1,  # Move to the left
    'fish5': -1   # Move to the left
}

bubbles = []

def draw_water():
    glColor3f(0.678, 0.847, 0.902)  # Light Blue color for water
    glBegin(GL_QUADS)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glVertex2f(1.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()

def fish1(x, y):
    glColor3f(1.0, 0.0, 0.0)  # Red color
    glBegin(GL_POLYGON)
    glVertex2f(0.8 + x, 0.25 + y)
    glVertex2f(0.85 + x, 0.3 + y)
    glVertex2f(0.875 + x, 0.3 + y)
    glVertex2f(0.95 + x, 0.25 + y)
    glVertex2f(0.875 + x, 0.2 + y)
    glVertex2f(0.85 + x, 0.2 + y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(0.93 + x, 0.25 + y)
    glVertex2f(0.99 + x, 0.29 + y)
    glVertex2f(0.99 + x, 0.21 + y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(0.875 + x, 0.3 + y)
    glVertex2f(0.89 + x, 0.4 + y)
    glVertex2f(0.85 + x, 0.3 + y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glVertex2f(0.875 + x, 0.2 + y)
    glVertex2f(0.89 + x, 0.1 + y)
    glVertex2f(0.85 + x, 0.2 + y)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # Black color for eye
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2f(0.83 + x, 0.265 + y)
    glEnd()

def fish2(x, y):
    glColor3f(0.0, 1.0, 0.0)  # Green color
    glBegin(GL_POLYGON)
    glVertex2f(0.8 + x, 0.05 + y)
    glVertex2f(0.85 + x, 0.1 + y)
    glVertex2f(0.95 + x, 0.05 + y)
    glVertex2f(0.85 + x, 0.0 + y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 1.0)  # Blue color for tail
    glVertex2f(0.93 + x, 0.05 + y)
    glVertex2f(0.99 + x, 0.09 + y)
    glVertex2f(0.99 + x, 0.01 + y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color for fins
    glVertex2f(0.85 + x, 0.095 + y)
    glColor3f(1.0, 0.0, 0.0)  # Red color for fins
    glVertex2f(0.89 + x, 0.125 + y)
    glVertex2f(0.87 + x, 0.07 + y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color for fins
    glVertex2f(0.85 + x, 0.007 + y)
    glColor3f(1.0, 0.0, 0.0)  # Red color for fins
    glVertex2f(0.895 + x, -0.035 + y)
    glVertex2f(0.87 + x, 0.02 + y)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # Black color for eye
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(0.83 + x, 0.065 + y)
    glEnd()

def fish3(x, y):
    glColor3f(1.6, 0.7, 0.0)  # Orange color
    glBegin(GL_POLYGON)
    glVertex2f(-0.8 - x, -0.05 - y)
    glVertex2f(-0.85 - x, -0.1 - y)
    glVertex2f(-0.95 - x, -0.05 - y)
    glVertex2f(-0.85 - x, 0.0 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.5, 0.0)  # Darker orange color
    glVertex2f(-0.93 - x, -0.05 - y)
    glVertex2f(-0.99 - x, -0.09 - y)
    glVertex2f(-0.99 - x, -0.01 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.5, 0.0)  # Darker orange color
    glVertex2f(-0.85 - x, -0.095 - y)
    glVertex2f(-0.89 - x, -0.125 - y)
    glVertex2f(-0.87 - x, -0.07 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(0.8, 0.5, 0.0)  # Darker orange color
    glVertex2f(-0.85 - x, -0.007 - y)
    glVertex2f(-0.895 - x, 0.035 - y)
    glVertex2f(-0.87 - x, -0.02 - y)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # Black color for eye
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.83 - x, -0.035 - y)
    glEnd()

def fish4(x, y):
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glBegin(GL_POLYGON)
    glVertex2f(-0.8 - x, -0.25 - y)
    glVertex2f(-0.85 - x, -0.3 - y)
    glVertex2f(-0.875 - x, -0.3 - y)
    glVertex2f(-0.95 - x, -0.25 - y)
    glVertex2f(-0.875 - x, -0.2 - y)
    glVertex2f(-0.85 - x, -0.2 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glVertex2f(-0.93 - x, -0.25 - y)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(-0.99 - x, -0.2 - y)
    glVertex2f(-0.99 - x, -0.3 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glVertex2f(-0.875 - x, -0.3 - y)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(-0.89 - x, -0.4 - y)
    glVertex2f(-0.85 - x, -0.3 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glVertex2f(-0.875 - x, -0.2 - y)
    glColor3f(0.0, 0.0, 1.0)  # Blue color
    glVertex2f(-0.89 - x, -0.1 - y)
    glVertex2f(-0.85 - x, -0.2 - y)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # Black color for eye
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.83 - x, -0.265 - y)
    glEnd()

def fish5(x, y):
    glColor3f(1.0, 0.0, 1.0)  # Pink color
    glBegin(GL_POLYGON)
    glVertex2f(-0.8 - x, 0.0 - y)
    glVertex2f(-0.85 - x, 0.05 - y)
    glVertex2f(-0.875 - x, 0.05 - y)
    glVertex2f(-0.95 - x, 0.0 - y)
    glVertex2f(-0.875 - x, -0.05 - y)
    glVertex2f(-0.85 - x, -0.05 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.5, 1.0)  # Lighter pink color
    glVertex2f(-0.93 - x, 0.0 - y)
    glVertex2f(-0.99 - x, -0.04 - y)
    glVertex2f(-0.99 - x, 0.04 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.5, 1.0)  # Lighter pink color
    glVertex2f(-0.875 - x, 0.05 - y)
    glVertex2f(-0.89 - x, 0.15 - y)
    glVertex2f(-0.85 - x, 0.05 - y)
    glEnd()

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.5, 1.0)  # Lighter pink color
    glVertex2f(-0.875 - x, -0.05 - y)
    glVertex2f(-0.89 - x, -0.15 - y)
    glVertex2f(-0.85 - x, -0.05 - y)
    glEnd()

    glColor3f(0.0, 0.0, 0.0)  # Black color for eye
    glPointSize(4.0)
    glBegin(GL_POINTS)
    glVertex2f(-0.83 - x, 0.035 - y)
    glEnd()

def draw_seaweed():
    # Left side seaweed
    glColor3f(0.118, 0.565, 0.353)  # Dark green color
    glBegin(GL_POLYGON)
    glVertex2f(-1.0, -0.5)
    glVertex2f(-0.95, -0.3)
    glVertex2f(-0.92, -0.4)
    glVertex2f(-0.88, -0.25)
    glVertex2f(-0.85, -0.35)
    glEnd()

    # Right side seaweed
    glBegin(GL_POLYGON)
    glVertex2f(1.0, -0.5)
    glVertex2f(0.95, -0.3)
    glVertex2f(0.92, -0.4)
    glVertex2f(0.88, -0.25)
    glVertex2f(0.85, -0.35)
    glEnd()

def generate_bubbles():
    global bubbles
    if len(bubbles) < 20:  # Limit the number of bubbles on screen
        x = random.uniform(-1.0, 1.0)
        y = -1.0
        radius = random.uniform(0.01, 0.05)
        bubbles.append((x, y, radius))

def draw_bubbles():
    glColor3f(1.0, 1.0, 1.0)  # White color for bubbles
    for bubble in bubbles:
        x, y, radius = bubble
        segments = 100
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(x, y)
        for i in range(segments + 1):
            angle = i * 2.0 * 3.14159 / segments
            glVertex2f(x + (radius * cos(angle)), y + (radius * sin(angle)))
        glEnd()

def update_bubbles():
    global bubbles
    updated_bubbles = []
    for bubble in bubbles:
        x, y, radius = bubble
        y += 0.01  # Rise up
        if y < 1.0:
            updated_bubbles.append((x, y, radius))
    bubbles = updated_bubbles

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_water()
    draw_seaweed()  # Draw seaweed
    draw_bubbles()  # Draw bubbles
    for fish_name, position in fish_positions.items():
        x, y = position
        if fish_name == 'fish1':
            fish1(x, y)
        elif fish_name == 'fish2':
            fish2(x, y)
        elif fish_name == 'fish3':
            fish3(x, y)
        elif fish_name == 'fish4':
            fish4(x, y)
        elif fish_name == 'fish5':
            fish5(x, y)
    pygame.display.flip()

def update_fish_positions():
    for fish_name in fish_positions:
        x, y = fish_positions[fish_name]
        direction = fish_directions[fish_name]
        if direction == -1:
            x -= 0.005
            if x < -1.0:
                x = 1.0
        elif direction == 1:
            x += 0.005
            if x > 1.0:
                x = -1.0
        fish_positions[fish_name] = [x, y]
        fish_directions[fish_name] = direction

def main():
    pygame.init()
    display_mode = DOUBLEBUF | OPENGL
    pygame.display.set_mode((800, 600), display_mode)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return

        generate_bubbles()  # Generate new bubbles
        update_bubbles()    # Update bubble positions
        update_fish_positions()
        display()
        pygame.time.wait(10)

if __name__ == '__main__':
    main()
