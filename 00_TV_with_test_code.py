# TV pilot class

class TV:
    def __init__(self, brand, location):  # brand, location - initialization parameters
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False
        # Some default list of channels
        self.channelList = [2, 4, 5, 10, 15, 22, 89]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        # constants
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM // 2  # starting volume // - integer division

    def power(self):
        self.isOn = not self.isOn  # toggle

    def volumeUp(self):
        if not self.isOn:
            return  # if TV is off don't change the volume
        if self.isMuted:
            self.isMuted = False  # changing the volume unmutes the TV
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1

    def volumeDown(self):
        if not self.isOn:
            return  # if TV is off don't change the volume
        if self.isMuted:
            self.isMuted = False  # changing the volume unmutes the TV
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1

    def channelUp(self):
        if not self.isOn:
            return  # if TV is off don't change the channel
        self.channelIndex += 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0  # wrapping around the list of channels

    def channelDown(self):
        if not self.isOn:
            return  # if TV is off don't change the channel
        self.channelIndex -= 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1  # wrapping around the list of channels

    def mute(self):
        if not self.isOn:
            return  # if TV is off don't mute it
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        # if channel don't exist on the list - do nothing

    def showInfo(self):
        print()
        print("TV status:")
        print(f'    Brand: {self.brand}')
        print(f'    Location: {self.location}')
        if self.isOn:
            print('    TV is on')
            print(f'    Channel is: {self.channelList[self.channelIndex]}')
            if self.isMuted:
                print(f'    Volume is: {self.volume} (sound is muted)')
            else:
                print(f'    Volume is: {self.volume}')
        else:
            print('    TV is off')


# Main code
oTV = TV("samsung", "bedroom")
oTV2 = TV("Sony", "kitchen")

oTV.power()
oTV.showInfo()

oTV2.power()
oTV2.showInfo()

oTV.channelUp()
oTV.channelUp()
oTV.volumeUp()
oTV.volumeUp()
oTV.showInfo()

oTV.power()
oTV.showInfo()
oTV.power()
oTV.showInfo()

oTV.volumeDown()
oTV.mute()
oTV.showInfo()

oTV.setChannel(10)
oTV.mute()
oTV.showInfo()
