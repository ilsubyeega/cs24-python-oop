from Page_286 import *
import pygame

class Star(Balloon):
    _starImage = pygame.image.load('images/yellowBalloon.png') # LETS JUST USE THE YELLOW BALLOON IMAGE FOR NOW.
    
    def __init__(self, window, maxWidth, maxHeight, ID):
        starImage = pygwidgets.Image(window, (0, 0), Star._starImage)
        super().__init__(window, maxWidth, maxHeight, ID, starImage, 'STAR', 40, 5)
        
        
        
    
        
        