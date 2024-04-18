import pygame
from pygame.locals import *
import sys
import random
from button import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 90
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

button = SimpleButton(window, (150, 30), 'assets/buttonUp.png', 'assets/buttonDown.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if button.handle_event(event):
            print('Button clicked')

    window.fill(BLACK)

    button.draw()
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
