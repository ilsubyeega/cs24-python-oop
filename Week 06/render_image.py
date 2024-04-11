import pygame
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

ball_image = pygame.image.load('./assets/images/ball.png')
target_image = pygame.image.load('./assets/images/target.jpg')

seal_image = pygame.image.load('./assets/images/seal.jpg')
seal_image = pygame.transform.scale(seal_image, (140, 100))

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.blit(ball_image, (50, 200))
    window.blit(target_image, (250, 200))
    window.blit(seal_image, (450, 200))
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)
