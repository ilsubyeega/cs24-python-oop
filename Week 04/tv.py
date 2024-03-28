class TV:
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        self.channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.num_of_channels = len(self.channel_list)
        self.channel_index = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM // 2

    def power(self):
        self.is_on = not self.is_on

    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index + 1
        if self.channel_index == self.num_of_channels:
            self.channel_index = 0

    def channel_down(self):
        if not self.is_on:
            return
        self.channel_index = self.channel_index - 1
        if self.channel_index < 0:
            self.channel_index = self.num_of_channels - 1

    def mute(self):
        if not self.is_on:
            return
        self.is_muted = not self.is_muted

    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)

    def show_info(self):
        print()
        print('TV Status:')
        if self.is_on:
            print('    TV is: On')
            print('    Channel is:', self.channel_list[self.channel_index])
            if self.is_muted:
                print('    Volume is:', self.volume, '(sound is muted)')
            else:
                print('    Volume is:', self.volume)
        else:
            print('    TV is: Off')


if __name__ == '__main__':
    instance = TV()

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