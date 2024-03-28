class DimmerListenableSwitch:
    def __init__(self):
        self.is_on = False
        self.brightness = 0
        self.listenable = False

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

    def enable_listen(self):
        self.listenable = True

    def disable_listen(self):
        self.listenable = False

    def show(self):
        print('The light is', 'on' if self.is_on else 'off')
        print('The brightness is', self.brightness)
        print('Listenable:', self.listenable)


switch = DimmerListenableSwitch()
switch.turn_on()
switch.raise_brightness()
switch.raise_brightness()
switch.raise_brightness()
switch.enable_listen()
switch.show()
