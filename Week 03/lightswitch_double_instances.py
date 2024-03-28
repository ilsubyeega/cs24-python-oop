class LightSwitch:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show(self):
        print('The light is', 'on' if self.is_on else 'off')


switch_1 = LightSwitch()
switch_2 = LightSwitch()

switch_1.turn_on()
switch_2.turn_off()

switch_1.show()
switch_2.show()
