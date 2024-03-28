class TV:
    def __init__(self, size, brand, location):
        self.isOn = False
        self.isMuted = False
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM // 2

        self.size = size
        self.brand = brand
        self.location = location

    def power(self):
        self.isOn = not self.isOn

    def volume_up(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volume_down(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channel_up(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex == self.nChannels:
            self.channelIndex = 0

    def channel_down(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def set_channel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)

    def show_info(self):
        print()
        print('TV Status:')
        print('    Brand:', self.brand)
        print('    Location:', self.location)
        print('    Size:', self.size)
        if self.isOn:
            print('    TV is: On')
            print('    Channel is:', self.channelList[self.channelIndex])
            if self.isMuted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


if __name__ == '__main__':
    instance = TV(40, 'SAMSUNG', 'Chungju')

    instance.power()
    instance.show_info()

    instance.channel_up()
    instance.channel_up()

    instance.volume_up()
    instance.volume_up()

    instance.show_info()

    instance.power()
    instance.show_info()

    instance.volume_down()
    instance.mute()
    instance.show_info()

    instance.set_channel(11)
    instance.mute()
    instance.show_info()