# HOMEWORK: 별 하나 만들고 40점짜리이고 스피드는 겁나 빠르게 
import pygame
import random
from pygame.locals import *
import pygwidgets
from Page_281_BALLONCONSTANTS import *
from Page_286 import *
from Page_286_Star import *

class BalloonMgr():
    def __init__(self, window, maxWidth, maxHeight):
        self.window = window
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def start(self):
        self.balloonList = []
        self.nPopped = 0
        self.nMissed = 0
        self.score = 0

        for balloonNum in range(0, N_BALLOONS):
            randomBalloonClass = random.choice((BalloonSmall,
                                                                    BalloonMedium,
                                                                    BalloonLarge, Star))
            oBalloon = randomBalloonClass(self.window, self.maxWidth,
                                                        self.maxHeight, balloonNum)
            self.balloonList.append(oBalloon)


    def handleEvent(self, event):
        if event.type == MOUSEBUTTONDOWN:
            for oBalloon in reversed(self.balloonList):
                wasHit, nPoints = oBalloon.clickedInside(event.pos)
                if wasHit:
                    if nPoints > 0:
                        self.balloonList.remove(oBalloon)  
                        self.nPopped = self.nPopped + 1
                        self.score = self.score + nPoints
                    return

    def update(self):
        for oBalloon in self.balloonList:
            status = oBalloon.update()
            if status == BALLOON_MISSED:
                self.balloonList.remove(oBalloon)
                self.nMissed = self.nMissed + 1

    def getScore(self):
        return self.score

    def getCountPopped(self):
        return self.nPopped

    def getCountMissed(self):
        return self.nMissed

    def draw(self):
        for oBalloon in self.balloonList:
            oBalloon.draw()