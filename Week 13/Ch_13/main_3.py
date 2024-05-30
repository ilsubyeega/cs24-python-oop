import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
TIMER_LENGTH = 2.5  

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Click Start to start a ' +
                                       str(TIMER_LENGTH) + '-second timer:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

startButton = pygwidgets.TextButton(window, (180, 100), 'Start')

clickMeButton = pygwidgets.TextButton(window, (320, 100), 'Click Me')

timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Message showing during timer',
                                      fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()  
oTimer = pyghelpers.Timer(TIMER_LENGTH)  

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            oTimer.start()  
            startButton.disable()
            timerMessage.show()
            print('Starting timer')

        if clickMeButton.handleEvent(event):
            print('Other button was clicked')

    if oTimer.update():  
        startButton.enable()
        timerMessage.hide()
        print('Timer ended')

    window.fill(WHITE)

    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND) 