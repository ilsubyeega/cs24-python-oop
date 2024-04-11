import pygame
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_MOVE = 3

ball_image = pygame.image.load('./assets/images/ball.png')

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

x_pos = 50
y_pos = 200

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key_pressed = pygame.key.get_pressed()

    if key_pressed[pygame.K_LEFT]:
        x_pos -= N_PIXELS_PER_MOVE

    if key_pressed[pygame.K_RIGHT]:
        x_pos += N_PIXELS_PER_MOVE

    if key_pressed[pygame.K_UP]:
        y_pos -= N_PIXELS_PER_MOVE

    if key_pressed[pygame.K_DOWN]:
        y_pos += N_PIXELS_PER_MOVE

    window.fill(BLACK)

    window.blit(ball_image, (x_pos, y_pos))
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
