import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Alsa Audio
import alsaaudio
m = alsaaudio.Mixer('PCM')


class VolumeKnob:
    # Reads the knob to control system volume.  Also checks for off, incase power needs to be cut to system, lights, etc.

    def __init__(self, AtoDPin, volumeOffCallback, debugOn):
        self.gain = 1
        self.thresh = .35
        self.divisor = 32.96
        self.val0 = 0
        self.AtoDPin = AtoDPin
        self.offCallback = volumeOffCallback
	self.debugOn = debugOn

        # Create an ADS1015 ADC (12-bit) instance.
        self.adc = Adafruit_ADS1x15.ADS1015()

    def tick(self):
        # Should be called at 4 Hz?

        # Read ADC channel AtoAPin for volume.
        val1 = self.adc.read_adc(self.AtoDPin, gain=self.gain) / self.divisor
        deltaVal = val1 - self.val0
        if deltaVal > self.thresh or deltaVal < -self.thresh:
            # print deltaV
            self.val0 = val1
            m.setvolume(int(val1) + 50)
	    if self.debugOn == True:
                print("Volume = " + str(int(val1) + 50))

        if val1 == 0:
            self.offCallback

