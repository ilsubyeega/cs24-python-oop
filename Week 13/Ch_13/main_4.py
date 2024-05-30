import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oHeaderMessage = pygwidgets.DisplayText(window, (0, 50), 'Click Start to start a timer:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

oStartButton = pygwidgets.TextButton(window, (180, 100), 'Start')

oStopButton = pygwidgets.TextButton(window, (320, 100), 'Stop')

oTimerMessage = pygwidgets.DisplayText(window, (66, 160), 'getTimeInSeconds      getTimeInHHMMSS',
                                      fontSize=36, width=WINDOW_WIDTH)

oTimerDisplaySeconds = pygwidgets.DisplayText(window, (220, 190), '',
                                      fontSize=36, justified='right')
oTimerDisplayHHMMSS = pygwidgets.DisplayText(window, (356, 190), '',
                                      fontSize=36, justified='right')

oTimerMessage.hide()  
oTimer = pyghelpers.CountUpTimer()  


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oStartButton.handleEvent(event):
            oTimer.start() 
            oStartButton.disable()
            oTimerMessage.show()
            print('Starting timer')

        if oStopButton.handleEvent(event):
            print('Stop button was clicked')
            oTimerMessage.hide()
            oTimer.stop()
            oStartButton.enable()

    timeInSeconds = oTimer.getTimeInSeconds()
    timeInHHMMSS = oTimer.getTimeInHHMMSS(2)
    oTimerDisplaySeconds.setValue(str(timeInSeconds))
    oTimerDisplayHHMMSS.setValue(timeInHHMMSS)

    window.fill(WHITE)

    oHeaderMessage.draw()
    oStartButton.draw()
    oStopButton.draw()
    oTimerMessage.draw()
    oTimerDisplaySeconds.draw()
    oTimerDisplayHHMMSS.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
