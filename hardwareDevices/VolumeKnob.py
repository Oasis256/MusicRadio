import time

# Import the ADS1x15 module.
import Adafruit_ADS1x15

# Alsa Audio
import alsaaudio
m = alsaaudio.Mixer('PCM')


class VolumeKnob():
    # Reads the knob to control system volume.  Also checks for off, incase power needs to be cut to system, lights, etc.

    def __init__(self):
        self.gain = 1
        self.thresh = .35
        self.divisor = 32.96
        self.val0 = 0
        self.isOff = False

        # Create an ADS1015 ADC (12-bit) instance.
        self.adc = Adafruit_ADS1x15.ADS1015()

    def tick(self):
        while True:
            # Read ADC channel 0 for volume.
            val1 = self.adc.read_adc(0, gain=self.gain) / self.divisor
            deltaVal = val1 - val0
            if deltaVal > self.thresh or deltaVal < -self.thresh:
                # print deltaV
                val0 = val1
                m.setvolume(int(val2) + 50)

            if val1 == 0:
                self.isOff = True
            else:
                self.isOff = False

            time.sleep(0.25)

    def getIsOff(self):
        return self.isOff

