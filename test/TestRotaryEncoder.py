import sys

sys.path.append("../hardwareDevices")

from RotaryEncoder import RotaryEncoder
from time import sleep


def PushNotifier(self):
    print ("Button was pressed!")

def RotateNotifier(num):
    if num > 1 or num < -1:
	print ("Bogus number: " + str(num))
    else:
    	print ("Encoder was rotated " + str(num) + " times")

rotenc = RotaryEncoder(16, 20, 12)
rotenc.registerPressCallback(PushNotifier)
rotenc.registerRotateCallback(RotateNotifier)

while True:
    rotenc.tick()
    sleep(.01)
