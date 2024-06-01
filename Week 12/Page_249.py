"""
HOMEWORK:
Implement following input boxes.
- Input: dollar, euro amount
- Output: euro cent, euro only.
"""
import pygame
from pygame.locals import *
import sys
import pygwidgets
from Page_243 import *
from Page_246 import *

BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()
 
title = pygwidgets.DisplayText(window, (0, 40),
                'Demo of InputNumber and DisplayMoney fields',
                fontSize=36, width=WINDOW_WIDTH, justified='center')

inputCaption1 = pygwidgets.DisplayText(window, (20, 150),
                'Input dollar amount:', fontSize=24,
                width=190, justified='right')
inputField1 = InputNumber(window, (230, 150), '', width=150, initialFocus=True)


inputCaption2 = pygwidgets.DisplayText(window, (20, 200),
                'Input euro amount:', fontSize=24,
                width=190, justified='right')
inputField2 = InputNumber(window, (230, 200), '', width=150)

okButton = pygwidgets.TextButton(window, (430, 150), 'OK')

outputCaption1 = pygwidgets.DisplayText(window, (20, 300),
                'Output dollars & cents:', fontSize=24,
                width=190, justified='right')
moneyField1 = DisplayMoney(window, (230, 300), '', textColor=BLACK,
                backgroundColor=WHITE, width=150)

outputCaption2 = pygwidgets.DisplayText(window, (20, 340),
                'Output dollars only:', fontSize=24,
                width=190, justified='right')
moneyField2 = DisplayMoney(window, (230, 340), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False)

outputCaption3 = pygwidgets.DisplayText(window, (20, 380),
                'Output euros:', fontSize=24,
                width=190, justified='right')
moneyField3 = DisplayMoney(window, (230, 380), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False, multiplier=1.3)

outputCaption4 = pygwidgets.DisplayText(window, (20, 420),
                'Output euros & cents:', fontSize=24,
                width=190, justified='right')
moneyField4 = DisplayMoney(window, (230, 420), '', textColor=BLACK,
                backgroundColor=WHITE, width=150, multiplier=1.3)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        clicked = okButton.handleEvent(event)

        if inputField1.handleEvent(event) or clicked:
            try:
                theValue = inputField1.getValue()
            except ValueError:  
                inputField1.setValue('(not a number)')
            else:  
                theText = str(theValue)
                moneyField1.setValue(theText)
                moneyField2.setValue(theText)
                moneyField3.setValue(theText)
                moneyField4.setValue(theText)
            
        #if inputField2.handleEvent(event) or clicked:
        #    print("what")
        #    try:
        #        theValue = inputField2.getValue()
        #    except ValueError:  
        #        inputField2.setValue('(not a number)')
        #    else:  
        #        theText = str(theValue)
        #        moneyField1.setValue(theText)
        #        moneyField2.setValue(theText)
        #        moneyField3.setValue(theText)
        #        moneyField4.setValue(theText)

    window.fill(BACKGROUND_COLOR)

    title.draw()
    inputCaption1.draw()
    inputField1.draw()
    inputCaption2.draw()
    inputField2.draw()
    okButton.draw()
    outputCaption1.draw()
    moneyField1.draw()
    outputCaption2.draw()
    moneyField2.draw()
    outputCaption3.draw()
    moneyField3.draw()
    outputCaption4.draw()
    moneyField4.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)  