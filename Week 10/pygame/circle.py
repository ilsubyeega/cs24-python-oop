import pygame
import random
import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)


class Circle:

    def __init__(self, window, max_width, max_height):
        self.window = window

        self.color = random.choice((RED, GREEN, BLUE, MAGENTA))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.radius = random.randrange(10, 50)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y, self.radius * 2, self.radius * 2)
        self.shapeType = 'Circle'

    def has_clicked_inside(self, mouse_point):
        distance = math.sqrt(((mouse_point[0] - self.centerX) ** 2) + ((mouse_point[1] - self.centerY) ** 2))
        if distance <= self.radius:
            return True
        else:
            return False

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def get_type(self):
        return self.shapeType

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.centerX, self.centerY), self.radius, 0)