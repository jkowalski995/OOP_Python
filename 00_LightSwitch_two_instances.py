# 00_LightSwitch

class LightSwitch:
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on
        self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
        self.switchIsOn = False

    def show(self):  # for testing
        print(self.switchIsOn)


# Main code

oLightSwitch1 = LightSwitch()  # create the lightswitch object
oLightSwitch2 = LightSwitch()  # create another lightswitch object

# Test code

oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn()  # turn switch 1 on
# the switch 2 should stay off
oLightSwitch2.show()
oLightSwitch2.turnOn()
oLightSwitch1.show()
oLightSwitch2.show()
