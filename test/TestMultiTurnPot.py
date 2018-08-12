import sys

sys.path.append("../hardwareDevices")

from MultiTurnPot import MultiTurnPot

def TurnNotifier(deltaVal):
    print ("Delta Turn=" + str(deltaVal))

mtpot = MultiTurnPot(1,.25)
mtpot.registerCallback(TurnNotifier)


while True:
    mtpot.tick()
    sleep(.25)