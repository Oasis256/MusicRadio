# Contributed by SWAGLORD12
from rtlsdr import RtlSdr
import time
import vlc
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

#global_freq = None

class setGuiCalls(object):

    sdr = RtlSdr()

    def readline(self):
        #global global_freq
        #if global_freq is None:
            # Open radio file.
        radioFileRead = open('freq.txt', 'r')
        global_freq = radioFileRead.readline().rstrip()
        radioFileRead.close()
        return global_freq

    def loadRadioFreq(self):
        freq1 = RtlCalls.readline(RtlCalls)
        freq = float(freq1)
        #RtlCalls.setRadiofreq(self)
        return freq

    def setRadioFreq(self, freq1):
        # The Radio freq value stored.
        # Open the json file holding the latest radio value
        # Use the latest value as your sample rate for your SDR device
        freq = freq1 * 10e5
        offset = 250000
        Fc = freq - offset
        self.sdr.sample_rate = int(1140000)
        self.sdr.center_freq = Fc
        #self.sdr.freq_correction = 60
        self.sdr.gain = 'auto'

        #samples = self.sdr.read_samples(int(8192000))

        print(freq1)
        return float(freq1)

    def RadioFreqUp(self, freq):
        # The Radio freq will change 1 value in the positive direction.
        add = 1
        freq1 = float(freq) + float(add)
        logger.info("Setting freq to: ")
        RtlCalls.saveRadioFreq(RtlCalls, freq1)
        time.sleep(.1)
        RtlCalls.setRadioFreq(RtlCalls, freq1)

    def RadioFreqDown(self, freq):
        # The Radio freq will change 1 value in the negative direction.
        sub = -1
        freq1 = float(freq) + float(sub)
        logger.info("Setting freq to: ")
        RtlCalls.saveRadioFreq(RtlCalls, freq1)
        time.sleep(.1)
        RtlCalls.setRadioFreq(RtlCalls, freq1)

    def saveRadioFreq(self, freq):
        # Will save the state of the radio settings for future use.
        # Open radio file.
        print (freq)
        radioFileWrite = open('freq.txt', 'w')
        radioFileWrite.write(str(freq))
        radioFileWrite.close()
