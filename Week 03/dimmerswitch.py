class DimmerSwitch:
    def __init__(self):
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def raise_brightness(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lower_brightness(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print('The light is', 'on' if self.is_on else 'off')
        print('The brightness is', self.brightness)

switch = DimmerSwitch()
switch.turn_on()
switch.raise_brightness()
switch.raise_brightness()
switch.raise_brightness()
switch.show()
