import sys
from ball import *
from text import *
from button import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 60

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (20, 20),
                              'Program has run through this many loops: ', WHITE)
oFrameCountDisplay = SimpleText(window, (440, 20), '', WHITE)
oRestartButton = SimpleButton(window, (20, 60),
                              'assets/restartUp.png', 'assets/restartDown.png')
frame_counter = 0

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handle_event(event):
            frame_counter = 0

    oBall.update()
    frame_counter = frame_counter + 1

    # homework: add minutes and seconds to frame counter display.
    # unsafe: retrieve minutes and seconds based on frame_counter
    # will be broke if game lags.
    minutes = frame_counter // FRAMES_PER_SECOND // 60
    seconds = frame_counter // FRAMES_PER_SECOND % 60

    oFrameCountDisplay.set_value(f'{minutes:02}m{seconds:02}s ({frame_counter} frames)')

    window.fill(BLACK)

    oBall.draw()
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)