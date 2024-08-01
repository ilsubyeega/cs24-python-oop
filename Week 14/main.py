# HOMEWORK
# - Create a `Go Left` and `Go Right` button.
# - Add sprite that affects from buttons above.
# ^ Lets just use `/images/player` for this purpose. (shouldve use runLeft/Right.png)

import pygame
from pygame.locals import *
import sys
import pygwidgets

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (220, 220, 220)

def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, animation ended')
    else:
        print('In myFunction, the animation with the nickname', theNickname, 'ended')

class CallBackTest():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('In myMethod, animation ended')
        else:
            print('In myMethod, the animation named', theNickname, 'ended')

pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

dinosaurAnimList = [
    (f'images/Dinowalk/f{i}.png', .1) for i in range(1, 18)
]

TRexAnimationList = [
    ('images/TRex/f{}.gif'.format(i), .1) for i in range(1, 11)
]

playerAnimList = {
    'left': [
        (f'images/player/walkL{i}.png', .1) for i in range(0, 9)
    ],
    'right': [
        (f'images/player/walkR{i}.png', .1) for i in range(0, 9)
    ],
    'front': [
        ('images/player/walkF0.png', .1)
    ]
}

oCallBackTest = CallBackTest()
oTitleText = pygwidgets.DisplayText(window, (110, 80), \
                                    'Animations                      SpriteSheetAnimations', fontSize=32)
oDinosaurAnimation = pygwidgets.Animation(window, (22, 145), dinosaurAnimList,
                                     autoStart=True, loop=False, callBack=myFunction, nickname='Dinosaur')
oPlayButton = pygwidgets.TextButton(window, (20, 240), "Play")
oPauseButton = pygwidgets.TextButton(window, (20, 280), "Pause")
oStopButton = pygwidgets.TextButton(window, (20, 320), "Stop")
oLoopCheckBox = pygwidgets.TextCheckBox(window, (20, 370), "Loop", value=False)
oShowCheckBox = pygwidgets.TextCheckBox(window, (20, 400), "Show", value=True)

oTRexAnimation = pygwidgets.Animation(window, (180, 140), TRexAnimationList, \
                                       autoStart=False, loop=False, nIterations=3, callBack=oCallBackTest.myMethod)
oInstructionsText = pygwidgets.DisplayText(window, (160, 320), '(Click image to activate)')

oEffectAnimation = pygwidgets.SpriteSheetAnimation(window, (400, 150), 'images/effect_010.png',
                                         35, 192, 192, .1, autoStart=True, loop=True)

oWalkAnimation = pygwidgets.SpriteSheetAnimation(window, (460, 335), 'images/male_walkcycle.png',
                            36, 64, 64, \
                            (.1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3, \
                             .1, .1, .1, .1, .1, .1, .1, .1, .3, .1, .1, .1, .1, .1, .1, .1, .1, .3), \
                             autoStart=False, loop=False)

oPlayerAnimationState = 'front'
oPlayerAnimation = pygwidgets.Animation(window, (320, 360), playerAnimList['front'], autoStart=False, loop=True)
oPlayerLeftAnimation = pygwidgets.Animation(window, (320, 360), playerAnimList['left'], autoStart=True, loop=True)
oPlayerRightAnimation = pygwidgets.Animation(window, (320, 360), playerAnimList['right'], autoStart=True, loop=True)
oPlayerLeftButton = pygwidgets.TextButton(window, (200, 360), "Go Left")
oPlayerRightButton = pygwidgets.TextButton(window, (200, 400), "Go Right")

oStartButton = pygwidgets.TextButton(window, (440, 400), "Start")

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.start()

        if oPauseButton.handleEvent(event):
            oDinosaurAnimation.pause()

        if oStopButton.handleEvent(event):
            oDinosaurAnimation.stop()

        if oLoopCheckBox.handleEvent(event):
            currentLoopState = oDinosaurAnimation.getLoop()
            oDinosaurAnimation.setLoop(not currentLoopState)

        if oShowCheckBox.handleEvent(event):
            showState = oDinosaurAnimation.getVisible()
            if showState:
                oDinosaurAnimation.hide()
            else:
                oDinosaurAnimation.show()

        if oStartButton.handleEvent(event):
            oWalkAnimation.start()

        if oDinosaurAnimation.handleEvent(event):
            oDinosaurAnimation.start()

        if oTRexAnimation.handleEvent(event):
            oTRexAnimation.start()
        
        if oPlayerLeftButton.handleEvent(event):
            oPlayerAnimationState = 'left'
            
        if oPlayerRightButton.handleEvent(event):
            oPlayerAnimationState = 'right'


    if oTRexAnimation.update():
        print('In main code - TRex animation ended')
    if oDinosaurAnimation.update():
        print('In main code - Dinosaur animation ended')
    if oEffectAnimation.update():
        print('In main code - Effect animation ended')
    if oWalkAnimation.update():
        print('In main code - Walk animation ended')
    
    oPlayerAnimation.update()
    oPlayerLeftAnimation.update()
    oPlayerRightAnimation.update()

    window.fill(BGCOLOR)

    oTitleText.draw()
    oDinosaurAnimation.draw()
    oPlayButton.draw()
    oPauseButton.draw()
    oStopButton.draw()
    oLoopCheckBox.draw()
    oShowCheckBox.draw()
    oTRexAnimation.draw()
    oInstructionsText.draw()
    oEffectAnimation.draw()
    oWalkAnimation.draw()
    oStartButton.draw()
    
    if oPlayerAnimationState == 'left':
        oPlayerLeftAnimation.draw()
    elif oPlayerAnimationState == 'right':
        oPlayerRightAnimation.draw()
    else:
        oPlayerAnimation.draw()
        
    oPlayerLeftButton.draw()
    oPlayerRightButton.draw()

    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)