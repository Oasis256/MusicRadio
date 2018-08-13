import sys

sys.path.append("../hardwareDevices")

from RotaryEncoder import RotaryEncoder
from time import sleep


def PushNotifier():
    print ("Button was pressed!")

def RotateNotifier(num):
    print ("Encoder was rotated " + num + " times")

rotenc = RotaryEncoder(20, 16, 12)
rotenc.registerPressCallback(PushNotifier)
rotenc.registerRotateCallback(RotateNotifier)

print ("Hello?")
while True:
    rotenc.tick()
    sleep(.01)
