# Dimmer switch class

class DimmerSwitch:
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1

    # for debugging
    def show(self):
        print(f"Switch is on?: {self.switchIsOn}")
        print(f"Brightness level: {self.brightness}")


# Main code

oDimmer = DimmerSwitch()
oDimmer.turnOn()
i = 0
while i < 5:
    oDimmer.raiseLevel()
    i += 1
oDimmer.show()
while i > 2:
    oDimmer.lowerLevel()
    i -= 1
oDimmer.turnOff()
oDimmer.show()
