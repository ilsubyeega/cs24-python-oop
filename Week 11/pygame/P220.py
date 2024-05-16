# homework: do area diff on triangle, instead of rectangle.

import pygame
import sys
from pygame.locals import *
from triangle import *

WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_TRIANGLES = 10
FIRST_TRIANGLE = 'first'
SECOND_TRIANGLE = 'second'

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

trianglesList = []
for i in range(0, N_TRIANGLES):
    oTriangle = Triangle(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    trianglesList.append(oTriangle)

tmp_triangle = FIRST_TRIANGLE

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oTriangle in reversed(trianglesList):  # render priority?
                if oTriangle.has_clicked_inside(event.pos):
                    print('Clicked inside a triangle: ', tmp_triangle)

                    if tmp_triangle == FIRST_TRIANGLE:
                        tmp_first = oTriangle
                        tmp_triangle = SECOND_TRIANGLE

                    elif tmp_triangle == SECOND_TRIANGLE:
                        tmp_second = oTriangle
                        if tmp_first == tmp_second:
                            print('Two triangle\'s area are the same')
                        elif tmp_first > tmp_second:
                            print('First triangle is bigger')
                        else:
                            print('Second triangle is bigger')
                        tmp_triangle = FIRST_TRIANGLE
    window.fill(WHITE)
    for oTriangle in trianglesList:
        oTriangle.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)