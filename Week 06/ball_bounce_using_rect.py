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

ball_rect = ball_image.get_rect()
BALL_WIDTH = ball_rect.width
BALL_HEIGHT = ball_rect.height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ball_rect.left += x_speed
    ball_rect.top += y_speed

    if ball_rect.left <= 0 or ball_rect.right >= WINDOW_WIDTH:
        x_speed = -x_speed

    if ball_rect.top <= 0 or ball_rect.bottom >= WINDOW_HEIGHT:
        y_speed = -y_speed

    window.fill(BLACK)

    window.blit(ball_image, ball_rect)
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)