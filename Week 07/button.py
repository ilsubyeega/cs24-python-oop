import pygame
from pygame.locals import *


class SimpleButton:
    STATE_IDLE = 'idle'
    STATE_ARMED = 'armed'
    STATE_DISARMED = 'disarmed'

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surface_up = pygame.image.load(up)
        self.surface_down = pygame.image.load(down)

        self.rect = self.surface_up.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handle_event(self, event_obj):

        if event_obj.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        is_event_point_in_button_rect = self.rect.collidepoint(event_obj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (event_obj.type == MOUSEBUTTONDOWN) and is_event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED

        elif self.state == SimpleButton.STATE_ARMED:
            if (event_obj.type == MOUSEBUTTONUP) and is_event_point_in_button_rect:
                self.state = SimpleButton.STATE_IDLE
                return True

            if (event_obj.type == MOUSEMOTION) and (not is_event_point_in_button_rect):
                self.state = SimpleButton.STATE_DISARMED

        elif self.state == SimpleButton.STATE_DISARMED:
            if is_event_point_in_button_rect:
                self.state = SimpleButton.STATE_ARMED
            elif event_obj.type == MOUSEBUTTONUP:
                self.state = SimpleButton.STATE_IDLE

        return False

    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surface_down, self.loc)

        else:
            self.window.blit(self.surface_up, self.loc)
