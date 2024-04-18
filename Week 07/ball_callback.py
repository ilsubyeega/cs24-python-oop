import pygame
from pygame.locals import *
import random


class Ball:

    def __init__(self, window, window_width, window_height, callback):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.callback = callback

        self.image = pygame.image.load('assets/ball.png')
        ball_rect = self.image.get_rect()
        self.width = ball_rect.width
        self.height = ball_rect.height
        self.max_width = window_width - self.width
        self.max_height = window_height - self.height

        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)

        speeds_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speeds_list)
        self.ySpeed = random.choice(speeds_list)

    def update(self):
        if (self.x < 0) or (self.x >= self.max_width):
            self.xSpeed = -self.xSpeed
            if self.callback:
                self.callback()
        if (self.y < 0) or (self.y >= self.max_height):
            self.ySpeed = -self.ySpeed
            if self.callback:
                self.callback()

        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
