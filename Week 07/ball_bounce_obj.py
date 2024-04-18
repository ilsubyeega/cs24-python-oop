import pygame
from pygame.locals import *
import sys
import random
from ball import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

o_ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    o_ball.update()
    window.fill(BLACK)

    o_ball.draw()
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)