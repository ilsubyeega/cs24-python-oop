import pygame
import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)


class Triangle:

    def __init__(self, window, max_width, max_height):
        self.window = window
        self.width = random.randrange(10, 100)
        self.height = random.randrange(10, 100)
        self.triangleSlope = -1 * (self.height / self.width)
        self.color = random.choice((RED, GREEN, BLUE, MAGENTA))
        self.x = random.randrange(1, max_width - 100)
        self.y = random.randrange(25, max_height - 100)
        self.rect = pygame.Rect(self.x, self.y,
                                self.width, self.height)
        self.shapeType = 'Triangle'

    def has_clicked_inside(self, mouse_point):
        in_rect = self.rect.collidepoint(mouse_point)
        if not in_rect:
            return False

        x_offset = mouse_point[0] - self.x
        y_offset = mouse_point[1] - self.y
        if x_offset == 0:
            return True

        point_slope_from_y_intercept = (y_offset - self.height) / x_offset
        if point_slope_from_y_intercept < self.triangleSlope:
            return True
        else:
            return False

    def get_type(self):
        return self.shapeType

    def get_area(self):
        area = .5 * self.width * self.height
        return area

    def draw(self):
        pygame.draw.polygon(self.window, self.color,
                            ((self.x, self.y + self.height),
                             (self.x, self.y),
                             (self.x + self.width, self.y)))