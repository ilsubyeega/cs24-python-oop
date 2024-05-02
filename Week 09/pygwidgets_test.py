#  Demo of pygwidgets capabilities
#
#  4/17  Developed by Irv Kalb

"""
another input
homework button
custom radio: add very high button
default radio: pizza, chicken, hamburger, green onion pancakes
image collection: pizza, chicken, hamburger, green onion pancakes

해물파전
"""
# 1 - Import libraries
import os
import sys

# The next line is here just in case you are running from the command line
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
from pygame.locals import *
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
FRAMES_PER_SECOND = 30


# The function and Test class and method below are not required.
# These are only here as a demonstration of how you could use a callback approach to handling events if you want to.

# Define a function to be used as a "callBack"
def myFunction(theNickname):
    if theNickname is None:
        print('In myFunction, a button was clicked')
    else:
        print('In myFunction, the button named', theNickname, 'was clicked')


# Define a class with a method to be used as a "callBack"
class Test():
    def myMethod(self, theNickname):
        if theNickname is None:
            print('In myMethod, a button was clicked')
        else:
            print('In myMethod, the button named', theNickname, 'was clicked')


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()  # create a clock object
oTest = Test()

# 4 - Load assets: image(s), provided_sounds,  etc.
# HOMEWORK: Change background
oBackgroundImage = pygwidgets.Image(window, (0, 0), 'images/aj-McsNra2VRQQ-unsplash.jpg')
oDisplayTextTitle = pygwidgets.DisplayText(window, (0, 20), 'pygwidgets example by Irv Kalb',
                                           fontSize=36, width=640, textColor=BLACK, justified='center')

oInputTextA = pygwidgets.InputText(window, (20, 100), 'Default input text',
                                   textColor=WHITE, backgroundColor=BLACK,
                                   fontSize=24, width=250)

oInputTextB = pygwidgets.InputText(window, (20, 200), initialFocus=True,
                                   textColor=(0, 0, 255),
                                   fontSize=28)  # add: , mask='*' for passwords

# HOMEWORK: Add another input text

oInputTextC = pygwidgets.InputText(window, (20, 240), 'Please input name or so.',
                                   textColor=(150, 150, 150),
                                   fontSize=16)

oDisplayTextA = pygwidgets.DisplayText(window, (20, 300), 'Here is some display text',
                                       fontSize=24, textColor=WHITE, justified='center')

oDisplayTextB = pygwidgets.DisplayText(window, (20, 400), 'Here is some display text',
                                       fontSize=24, textColor=BLACK, backgroundColor=WHITE)

oRestartButton = pygwidgets.CustomButton(window, (100, 430),
                                         'provided_images/restartButtonUp.png',
                                         down='provided_images/restartButtonDown.png',
                                         over='provided_images/restartButtonOver.png',
                                         disabled='provided_images/restartButtonDisabled.png',
                                         soundOnClick='provided_sounds/blip.wav',
                                         nickname='restartButton',
                                         callBack=myFunction)  # callBack here is not required

# oCheckBoxA controls the availability the custom radio buttons
# oCheckBoxB controls the availability of the text radio buttons
oCheckBoxA = pygwidgets.CustomCheckBox(window, (450, 110), value=True,
                                       on='provided_images/checkBoxOn.png', off='provided_images/checkBoxOff.png',
                                       onDown='provided_images/checkBoxOnDown.png',
                                       offDown='provided_images/checkBoxOffDown.png',
                                       onDisabled='provided_images/checkBoxOnDisabled.png',
                                       offDisabled='provided_images/checkBoxOffDisabled.png')

oRadioCustom1 = pygwidgets.CustomRadioButton(window, (500, 150), 'Custom Group',
                                             on='provided_images/radioLowOn.png', off='provided_images/radioLowOff.png',
                                             onDown='provided_images/radioLowOnDown.png',
                                             offDown='provided_images/radioLowOffDown.png',
                                             onDisabled='provided_images/radioLowOnDisabled.png',
                                             offDisabled='provided_images/radioLowOffDisabled.png',
                                             value=True, nickname='Low')

oRadioCustom2 = pygwidgets.CustomRadioButton(window, (500, 180), 'Custom Group',
                                             on='provided_images/radioMedOn.png', off='provided_images/radioMedOff.png',
                                             onDown='provided_images/radioMedOnDown.png',
                                             offDown='provided_images/radioMedOffDown.png',
                                             onDisabled='provided_images/radioMedOnDisabled.png',
                                             offDisabled='provided_images/radioMedOffDisabled.png',
                                             value=False, nickname='Med')

oRadioCustom3 = pygwidgets.CustomRadioButton(window, (500, 210), 'Custom Group',
                                             on='provided_images/radioHighOn.png',
                                             off='provided_images/radioHighOff.png',
                                             onDown='provided_images/radioHighOnDown.png',
                                             offDown='provided_images/radioHighOffDown.png',
                                             onDisabled='provided_images/radioHighOnDisabled.png',
                                             offDisabled='provided_images/radioHighOffDisabled.png',
                                             value=False, nickname='High')

oRadioCustom4 = pygwidgets.CustomRadioButton(window, (500, 240), 'Custom Group',
                                             on='images/radioVeryHighOn.png',
                                             off='images/radioVeryHighOff.png',
                                             onDown='images/radioVeryHighOnDown.png',
                                             offDown='images/radioVeryHighOffDown.png',
                                             onDisabled='images/radioVeryHighOnDisabled.png',
                                             offDisabled='images/radioVeryHighOffDisabled.png',
                                             value=False, nickname='VeryHigh')

oCheckBoxB = pygwidgets.TextCheckBox(window, (450, 295), 'Allow Radio Buttons')

oRadioText1 = pygwidgets.TextRadioButton(window, (462, 320), 'Default Group', 'Pizza',
                                         value=False)

oRadioText2 = pygwidgets.TextRadioButton(window, (462, 336), 'Default Group', 'Chicken',
                                         value=True)

oRadioText3 = pygwidgets.TextRadioButton(window, (462, 352), 'Default Group', 'Hamburger',
                                         value=False)

oRadioText4 = pygwidgets.TextRadioButton(window, (462, 368), 'Default Group', 'Green onion pancakes',
                                         value=False)

oStatusButton = pygwidgets.TextButton(window, (480, 390), 'Show Status',
                                      callBack=oTest.myMethod)  # callBack here is not required

oDragger = pygwidgets.Dragger(window, (300, 200),
                              'provided_images/dragMeUp.png',
                              'provided_images/dragMeDown.png',
                              'provided_images/dragMeOver.png',
                              'provided_images/dragMeDisabled.png',
                              nickname='My Dragger')

oPythonIcon = pygwidgets.Image(window, (15, 500), 'provided_images/pythonIcon.png')

oImageCollection = pygwidgets.ImageCollection(window, (400, 490),
                                              {'start': 'imageStart.jpg',
                                               'left': 'imageLeft.jpg',
                                               'right': 'imageRight.jpg',
                                               'up': 'imageUp.jpg',
                                               'down': 'imageDown.jpg'},
                                              'start', path='provided_images/')

oFoodImageCollection = pygwidgets.ImageCollection(window, (260, 490),
                                                  {'pizza': 'pizza.png',
                                                   'chicken': 'chicken.png',
                                                   'hamburger': 'hamburger.png',
                                                   'green onion pancakes': 'green_onion_pancakes.png'},
                                                  'pizza', path='images/')

oImageInstructions = pygwidgets.DisplayText(window, (400, 595), 'Click then type l, r, d, u, s, or Space')

oIconInstructions = pygwidgets.DisplayText(window, (15, 595),
                                           'Click then up or down arrow to resize,\n' +
                                           'left or right arrow to rotate, \n' +
                                           'h or v to flip horizontal or vertical')

oFrisbeeImage = pygwidgets.Image(window, (562, 2), 'provided_images/frisbee.png')

# Homework Add Button
# on active, show the image, but if not, hide the image.
oHomeworkButton = pygwidgets.TextButton(window, (300, 430), 'Homework')

# 5 - Initialize variables
counter = 0
angle = 0
pct = 100

# 6 - Loop forever
while True:

    # 7 - Check for and handle events

    for event in pygame.event.get():
        # check if the event is the close button
        if event.type == pygame.QUIT:
            # if it is quit, the program
            pygame.quit()
            sys.exit()

        if oInputTextA.handleEvent(event):  # pressed Return or Enter
            theText = oInputTextA.getValue()
            print('The text of oInputTextA is: ' + theText)

        if oInputTextB.handleEvent(event):  # pressed Return or Enter
            theText = oInputTextB.getValue()
            print('The text of oInputTextB is: ' + theText)

        # homework: another input
        if oInputTextC.handleEvent(event):
            print(f'The text of oInputTextC is: {oInputTextC.getValue()}')

        if oRestartButton.handleEvent(event):  # clicked
            counter = 0
            print('Content of first input text is:', oInputTextA.getValue())
            print('Content of second input text is:', oInputTextB.getValue())

        # HOMEWORK
        oHomeworkButton.handleEvent(event)

        if oCheckBoxA.handleEvent(event):  # toggled
            aOn = oCheckBoxA.getValue()
            print('oCheckBoxA was clicked, new value is:', aOn)
            if aOn:
                oRadioCustom1.enable()
                oRadioCustom2.enable()
                oRadioCustom3.enable()
                oRadioCustom4.enable()
            else:
                oRadioCustom1.disable()
                oRadioCustom2.disable()
                oRadioCustom3.disable()
                oRadioCustom4.disable()
        if oRadioCustom1.handleEvent(event):  # selected
            print('Radio button custom1 was clicked')

        if oRadioCustom2.handleEvent(event):  # selected
            print('Radio button custom2 was clicked')

        if oRadioCustom3.handleEvent(event):  # selected
            print('Radio button custom3 was clicked')

        if oRadioCustom4.handleEvent(event):  # selected
            print('Radio button custom4 was clicked')

        if oCheckBoxB.handleEvent(event):  # toggled
            bOn = oCheckBoxB.getValue()
            print('oCheckBoxB was clicked, new value is:', bOn)
            if bOn:
                oRadioText1.enableGroup()  # disable all buttons in this group
                # could alternatively have have used (does the same as):
                # oRadioText1.enable()
                # oRadioText2.enable()
                # oRadioText3.enable()
            else:
                oRadioText1.disableGroup()  # enable all radio buttons in group that contains this radio button
                # could alternatively have used (does the same as):
                # oRadioText1.disable()
                # oRadioText2.disable()
                # oRadioText3.disable()

        if oRadioText1.handleEvent(event):  # selected
            print('Radio button text1 was clicked')

        if oRadioText2.handleEvent(event):  # selected
            print('Radio button text2 was clicked')

        if oRadioText3.handleEvent(event):  # selected
            print('Radio button text3 was clicked')

        if oRadioText4.handleEvent(event):  # selected
            print('Radio button text4 was clicked')

        if oStatusButton.handleEvent(event):  # clicked
            nickname = oRadioCustom1.getSelectedRadioButton()
            print('The currently selected custom Radio Button is:', nickname)
            nickname = oRadioText1.getSelectedRadioButton()
            print('The currently selected Text Radio Button is:', nickname)

        if oDragger.handleEvent(event):
            print('Done dragging, dragger nickname was:', oDragger.getNickname())
            print('  Mouse up at:', oDragger.getMouseUpLoc())
            print('  Dragger is now located at', oDragger.getLoc())

        if oPythonIcon.handleEvent(event):
            print('Got click on the Python icon')

        if oImageCollection.handleEvent(event):
            print('Got click on image collection')

        if oFoodImageCollection.handleEvent(event):
            print('Got click on food image collection')

        if oFrisbeeImage.handleEvent(event):
            print('Got click on the frisbee image')

        if event.type == pygame.KEYDOWN:
            if oPythonIcon.getFocus():
                if event.key == pygame.K_h:
                    oPythonIcon.flipHorizontal()
                elif event.key == pygame.K_v:
                    oPythonIcon.flipVertical()
            if oImageCollection.getFocus():
                if event.key == pygame.K_l:
                    oImageCollection.replace('left')
                elif event.key == pygame.K_r:
                    oImageCollection.replace('right')
                elif event.key == pygame.K_u:
                    oImageCollection.replace('up')
                elif event.key == pygame.K_d:
                    oImageCollection.replace('down')
                elif event.key == pygame.K_s:
                    oImageCollection.replace('start')
                elif event.key == pygame.K_SPACE:
                    oImageCollection.replace('')

            if oFoodImageCollection.getFocus():
                if event.key == pygame.K_p:
                    oFoodImageCollection.replace('pizza')
                elif event.key == pygame.K_c:
                    oFoodImageCollection.replace('chicken')
                elif event.key == pygame.K_h:
                    oFoodImageCollection.replace('hamburger')
                elif event.key == pygame.K_g:
                    oFoodImageCollection.replace('green onion pancakes')

    homework_should_draw_image = oHomeworkButton.state != 'armed'

    keyPressedList = pygame.key.get_pressed()
    if keyPressedList[pygame.K_LEFT]:
        oPythonIcon.rotate(-5)
    if keyPressedList[pygame.K_RIGHT]:
        oPythonIcon.rotate(5)

        # If we wanted to keep track of the angle, we could start with:  angle = 0
        # Then for every left arrow:  angle = angle + 5
        # and for every right arrow:  angle = angle - 5
        # Finally, call:  oPythonIcon.rotateTo
    if keyPressedList[pygame.K_UP]:
        scaleFromCenter = not (keyPressedList[pygame.K_LSHIFT] or keyPressedList[pygame.K_RSHIFT])
        pct = pct + 10
        oPythonIcon.scale(pct, scaleFromCenter=scaleFromCenter)
        # print('Scaling up to', pct, '%')
    if keyPressedList[pygame.K_DOWN]:
        scaleFromCenter = not (keyPressedList[pygame.K_LSHIFT] or keyPressedList[pygame.K_RSHIFT])
        if pct > 0:
            pct = pct - 10
        oPythonIcon.scale(pct, scaleFromCenter=scaleFromCenter)
        # print('Scaling down to', pct, '%')

    # 8  Do any "per frame" actions
    counter = counter + 1
    oDisplayTextA.setValue('Here is some centered display text.\n' +
                           'Showing the \nnumber of frames.\nLoop counter:' + str(counter))
    oDisplayTextB.setValue('Here is some display text.  Loop counter:' + str(counter))

    # 9 - Clear the window and draw background if enabled
    window.fill((0, 0, 0))
    if homework_should_draw_image:
        oBackgroundImage.draw()

    # 10 - Draw all window elements
    oPythonIcon.draw()
    oDisplayTextTitle.draw()
    oInputTextA.draw()
    oInputTextB.draw()
    oInputTextC.draw()
    oDisplayTextA.draw()
    oDisplayTextB.draw()
    oRestartButton.draw()
    oCheckBoxA.draw()
    oRadioCustom1.draw()
    oRadioCustom2.draw()
    oRadioCustom3.draw()
    oRadioCustom4.draw()
    oCheckBoxB.draw()
    oRadioText1.draw()
    oRadioText2.draw()
    oRadioText3.draw()
    oRadioText4.draw()
    oStatusButton.draw()
    oDragger.draw()
    oImageCollection.draw()
    oFoodImageCollection.draw()
    oFrisbeeImage.draw()
    oImageInstructions.draw()
    oIconInstructions.draw()
    oHomeworkButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
