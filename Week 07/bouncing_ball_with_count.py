import pygame
from pygame.locals import *
import sys
import random
from ball_callback import *
from text import *
from button import *

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

bounce_count = 0


def callback():
    global bounce_count
    bounce_count += 1


ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT, callback)
ball.xSpeed = 10
ball.ySpeed = 10

text = SimpleText(window, (16, 16), "Bounce Count: 0", (255, 255, 0))
button = SimpleButton(window, (16, 32), 'assets/buttonUp.png', 'assets/buttonDown.png')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if button.handle_event(event):
            print('Button clicked')
            bounce_count = 0

    window.fill(BLACK)
    ball.update()
    text.set_value("Bounce Count: " + str(bounce_count))
    ball.draw()
    text.draw()
    button.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
