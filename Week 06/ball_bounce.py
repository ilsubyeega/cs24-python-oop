import pygame
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 120

ball_image = pygame.image.load('./assets/images/ball.png')

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

x_pos = 50
y_pos = 200

x_speed = 3
y_speed = 3

BALL_WIDTH = ball_image.get_width()
BALL_HEIGHT = ball_image.get_height()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x_pos += x_speed
    y_pos += y_speed

    if x_pos <= 0 or x_pos >= WINDOW_WIDTH - BALL_WIDTH:
        x_speed = -x_speed

    if y_pos <= 0 or y_pos >= WINDOW_HEIGHT - BALL_HEIGHT:
        y_speed = -y_speed

    window.fill(BLACK)

    window.blit(ball_image, (x_pos, y_pos))
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)