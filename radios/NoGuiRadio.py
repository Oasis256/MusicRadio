import sys
import threading

sys.path.append("../radioFreq")
sys.path.append("../config")
sys.path.append("../hardwareDevices")
sys.path.append("../network")

from time import sleep

from GqrxCtrl import GqrxCtrl
from RadioConfig import RadioConfig
from RadioCtrl import RadioCtrl
from MultiTurnPot import MultiTurnPot
from RotaryEncoder import RotaryEncoder
from VolumeKnob import VolumeKnob

global freq

def MultiTurnPotHandler(deltaVal):
	if deltaVal > 0:
		#radioCtrl.increaseFrequency((deltaVal % 10) * 1000)
		print ("Increasing frequency by: " + str((deltaVal %10) * 1000))
		
	elif deltaVal < 0:
		#radioCtrl.decreaseFrequency((deltaVal % 10) * 1000)
		print ("Decreasing frequency by: " + str((deltaVal %10) * 1000))
	


def RotaryBtnHandler(self):
    radioCtrl.setNextBand()
    demod = radioCtrl.getCurrDemod
    freq = radioCtrl.getCurrFreqency
    gqrx.gqrxSetDemodMode(demod)
    gqrx.gqrxTuneFreq(freq)


def RotaryRotateHandler(num):
    if num > 1 or num < -1:
        print ("Bogus number: " + str(num))
    else:
        if num == 1:
            freq = radioCtrl.getNextFrequency
        elif num == -1:
            freq = radioCtrl.getPrevFrequency
        gqrx.gqrxTuneFreq(freq)


def VolumeOffHandler(self):
    print ("Volume is at 0!")


# Create Radio Config object
radioConfig = RadioConfig()

# Create new radio controller object
radioCtrl = RadioCtrl(radioConfig)

# Create new multi turn pot handler
mtpot = MultiTurnPot(1, 10)
mtpot.registerCallback(MultiTurnPotHandler)


def mtpotThread():
    while True:
    	mtpot.tick()
    	sleep(.25)


# Create rotary encoder handler
rotenc = RotaryEncoder(16, 20, 12)
rotenc.registerPressCallback(RotaryBtnHandler)
rotenc.registerRotateCallback(RotaryRotateHandler)


def rotencThread():
    while True:
    	rotenc.tick()
    	sleep(.01)


# Create volume knob handler
volknob = VolumeKnob(0, VolumeOffHandler, True)


def volknobThread():
    while True:
    	volknob.tick()
    	sleep(.25)


# Setup GQRX
gqrx = GqrxCtrl(sys.argv[1], True)

thread1 = threading.Thread(target=mtpotThread)
thread2 = threading.Thread(target=rotencThread)
thread3 = threading.Thread(target=volknobThread)

# Start all threads
thread1.start()
thread2.start()
thread3.start()

thread3.join()
thread2.join()
thread1.join()
