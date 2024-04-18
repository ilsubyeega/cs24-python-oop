import pygame
from pygame.locals import *
import sys
import random
from ball import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 10

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ballList = []
for _ in range(0, N_BALLS):
    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for ball in ballList:
        ball.update()

    window.fill(BLACK)

    for ball in ballList:
        ball.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)