import pygame
from pygame.locals import *
import sys
import random

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_SIZE = 100

N_PIXELS_TO_MOVE = 4

MAX_WIDTH = WINDOW_WIDTH - BALL_SIZE
MAX_HEIGHT = WINDOW_HEIGHT - BALL_SIZE

pygame.init()

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

ball_image = pygame.image.load('./assets/images/ball.png')
target_image = pygame.image.load('./assets/images/target.jpg')
seal_image = pygame.image.load('./assets/images/seal.jpg')

ball_x = random.randint(0, MAX_WIDTH)
ball_y = random.randint(0, MAX_HEIGHT)
ball_rect = pygame.Rect(ball_x, ball_y, BALL_SIZE, BALL_SIZE)

hold_state = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            ball_x, ball_y = pygame.mouse.get_pos()
            ball_x -= 50
            ball_y -= 50

            if ball_rect.collidepoint(ball_x, ball_y):
                """
                # if user clicked a ball, move it to a random location
                ball_x = random.randint(0, MAX_WIDTH)
                ball_y = random.randint(0, MAX_HEIGHT)
                """

                # if user clicked a ball, center it on the screen
                ball_x = (WINDOW_WIDTH - BALL_SIZE) // 2
                ball_y = (WINDOW_HEIGHT - BALL_SIZE) // 2

            ball_rect.topleft = (ball_x, ball_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                hold_state = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hold_state = True

            if event.key == pygame.K_LEFT:
                ball_rect.move_ip(-N_PIXELS_TO_MOVE, 0)

            if event.key == pygame.K_RIGHT:
                ball_rect.move_ip(N_PIXELS_TO_MOVE, 0)

        if event.type == pygame.MOUSEMOTION:
            if hold_state:
                pos_x, pos_y = pygame.mouse.get_pos()
                ball_rect.topleft = (pos_x-50, pos_y-50)

    window.fill(BLACK)

    window.blit(target_image, (250, 200))
    window.blit(ball_image, ball_rect)

    target_rect = pygame.Rect(250, 200, 100, 100)
    if ball_rect.colliderect(target_rect):
        window.blit(seal_image, (0, 0))

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
