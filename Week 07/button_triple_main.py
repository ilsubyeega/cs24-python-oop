import pygame
from pygame.locals import *
import sys
import random
from button import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 90
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

button_a = SimpleButton(window, (50, 30), 'assets/buttonAUp.png', 'assets/buttonADown.png')
button_b = SimpleButton(window, (250, 30), 'assets/buttonBUp.png', 'assets/buttonBDown.png')
button_c = SimpleButton(window, (450, 30), 'assets/buttonCUp.png', 'assets/buttonCDown.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if button_a.handle_event(event):
            print('Button A clicked')

        if button_b.handle_event(event):
            print('Button B clicked')

        if button_c.handle_event(event):
            print('Button C clicked')

    window.fill(BLACK)

    button_a.draw()
    button_b.draw()
    button_c.draw()
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
