class DimmerSwitch:
    def __init__(self, label):
        self.label = label
        self.is_on = False
        self.brightness = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def raise_level(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lower_level(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    def show(self):
        print('Label:', self.label)
        print('Light is on?', self.is_on)
        print('Brightness is:', self.brightness)
        print()


if __name__ == '__main__':
    oDimmer1 = DimmerSwitch('Dimmer1')
    oDimmer1.turn_on()
    oDimmer1.raise_level()
    oDimmer1.raise_level()

    oDimmer2 = DimmerSwitch('Dimmer2')
    oDimmer2.turn_on()
    oDimmer2.raise_level()
    oDimmer2.raise_level()
    oDimmer2.raise_level()

    oDimmer3 = DimmerSwitch('Dimmer3')

    oDimmer1.show()
    oDimmer2.show()
    oDimmer3.show()