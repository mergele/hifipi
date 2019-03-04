# -----------------------------------------------------------------------------
# hifipi-test - test to access the basic volumio functions for 
# * volume and playback control
# * playlist selection
# in order to build a simple button and rotation-encoder based player for my
# little daugter
# -----------------------------------------------------------------------------
#                             C R E D I T S
# -----------------------------------------------------------------------------
# Great thanks to Martin O'Hanlon, stuffaboutcode.com for supporting me with 
# the KY040 Python Class which helped me to quickstart into python :_) 
# -----------------------------------------------------------------------------
import os
import RPi.GPIO as GPIO
from time import sleep

class KY040:
    global volume
    CLOCKWISE = 0
    ANTICLOCKWISE = 1
    
    def __init__(self, clockPin, dataPin, switchPin,
                 rotaryCallback, switchCallback):
        #persist values
        self.clockPin = clockPin
        self.dataPin = dataPin
        self.switchPin = switchPin
        self.rotaryCallback = rotaryCallback
        self.switchCallback = switchCallback

        #setup pins
        GPIO.setup(clockPin, GPIO.IN)
        GPIO.setup(dataPin, GPIO.IN)
        GPIO.setup(switchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def start(self):
        GPIO.add_event_detect(self.clockPin,
                              GPIO.FALLING,
                              callback=self._clockCallback,
                              bouncetime=250)
        GPIO.add_event_detect(self.switchPin,
                              GPIO.FALLING,
                              callback=self._switchCallback,
                              bouncetime=300)

    def stop(self):
        GPIO.remove_event_detect(self.clockPin)
        GPIO.remove_event_detect(self.switchPin)
    
    def _clockCallback(self, pin):
        if GPIO.input(self.clockPin) == 0:
            data = GPIO.input(self.dataPin)
            if data == 1:
                self.rotaryCallback(self.ANTICLOCKWISE)
            else:
                self.rotaryCallback(self.CLOCKWISE)

    def _switchCallback(self, pin):
        if GPIO.input(self.switchPin) == 0:
            self.switchCallback()

#test
if __name__ == "__main__":
    
    mutestate = 0

    CLOCKPIN = 5
    DATAPIN = 6
    SWITCHPIN = 13

    def rotaryChange(direction):
        if direction == 1: # LINKS / DECREMENT
            print "turned left" + str(direction)
            os.system("curl 'localhost:3000/api/v1/commands/?cmd=volume&volume=minus'")
        else:
            print "turned right" + str(direction)
            os.system("curl 'localhost:3000/api/v1/commands/?cmd=volume&volume=plus'")

    def switchPressed():
        global mutestate
        if mutestate == 0:
            mutestate = 1
            os.system("curl 'localhost:3000/api/v1/commands/?cmd=volume&volume=mute'")
        else:
            mutestate = 0
            os.system("curl 'localhost:3000/api/v1/commands/?cmd=volume&volume=unmute'")
       
        print "mute/unmute button pressed"


    GPIO.setmode(GPIO.BCM)
    
    ky040 = KY040(CLOCKPIN, DATAPIN, SWITCHPIN,
                  rotaryChange, switchPressed)

    ky040.start()

    try:
        while True:
            sleep(0.1)
    finally:
        ky040.stop()
        GPIO.cleanup()
