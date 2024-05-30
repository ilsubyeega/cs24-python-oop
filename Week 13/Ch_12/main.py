""" homework

- 카드 16개로 바꾸기 (Done)
- 버튼 포지션 변경 (Done)
- 0점 이하일 경우 게임 오버 (Done)
- 뉴 게임이면 스코어 0으로 초기화 (Done)
- 게임 오버시 버튼 비활성화 (Done)
"""
import pygame
from pygame.locals import *
import sys
import pygwidgets
from game import *

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

background = pygwidgets.Image(window, (0, 0),
                            'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 220),
                            'New Game', width=100, height=45)
newGameButton.disable()

higherButton = pygwidgets.TextButton(window, (540, 220),
                            'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 220),
                            'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 220),
                            'Quit', width=100, height=45)

oGame = Game(window)

while True:

    for event in pygame.event.get():
        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()
            newGameButton.disable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                newGameButton.enable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                newGameButton.enable()


    background.draw()

    oGame.draw()

    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)