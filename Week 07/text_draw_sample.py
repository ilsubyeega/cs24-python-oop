import pygame
from pygame.locals import *
import sys
import random
from text import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

text = SimpleText(window, (16, 16), "Hello World", (255, 0, 0))

frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BLACK)

    frame += 1
    text.set_value("Frame: #" + str(frame))
    text.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
