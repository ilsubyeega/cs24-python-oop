# Square class

import pygame
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)


class Square:

    def __init__(self, window, max_width, max_height):
        self.window = window
        self.widthAndHeight = random.randrange(10, 100)
        self.color = random.choice((RED, GREEN, BLUE, MAGENTA))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.rect = pygame.Rect(self.x, self.y, self.widthAndHeight,
                                self.widthAndHeight)
        self.shapeType = 'Square'

    def has_clicked_inside(self, mouse_point):
        clicked = self.rect.collidepoint(mouse_point)
        return clicked

    def get_type(self):
        return self.shapeType

    def get_area(self):
        area = self.widthAndHeight * self.widthAndHeight
        return area

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.widthAndHeight, self.widthAndHeight))
