import random

import pygame
import sys
from pygame.locals import *
from square import Square
from circle import Circle
from triangle import Triangle
import pygwidgets

# homework
# 1. add magenta (applied on square, circle, triangle classes.)
# 2. extract x and y of shape and cursor to text.

WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_SHAPES = 10

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

shapes_list = []
shape_classes_tuple = (Square, Circle, Triangle)
for i in range(0, N_SHAPES):
    randomly_chosen_class = random.choice(shape_classes_tuple)
    o_shape = randomly_chosen_class(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    shapes_list.append(o_shape)

o_status_line = pygwidgets.DisplayText(window, (4, 4),
                                       'Click on shapes', fontSize=28)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for o_shape in reversed(shapes_list):
                if o_shape.has_clicked_inside(event.pos):
                    area = o_shape.get_area()
                    the_type = o_shape.get_type()
                    new_text = f"""
                    Clicked on a {the_type} whose area is {area:4.0f}
                    Mouse Pos: {event.pos[0]:4.0f}, {event.pos[1]:4.0f}
                    Shape Pos: {o_shape.x:4.0f}, {o_shape.y:4.0f}
                    """.strip()
                    o_status_line.setValue(new_text)
                    break

    window.fill(WHITE)
    for o_shape in shapes_list:
        o_shape.draw()
    o_status_line.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
