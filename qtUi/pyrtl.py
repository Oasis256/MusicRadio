# Contributed by SWAGLORD12
# from rtlsdr import RtlSdr
import time
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

global_freq = None

class RtlCalls(object):

    def __init__(self, freq):
        self.freq = freq
        
    def readline(self):
        global global_freq
        if global_freq is None:
            # Open radio file.
            radioFileRead = open('freq.txt', 'r')
            global_freq = radioFileRead.readline().rstrip()
            radioFileRead.close()
        return global_freq

    def loadRadioFreq(self):
        freq1 = RtlCalls.readline(RtlCalls)
        freq = float(freq1)
        RtlCalls.setRadiofreq(self, freq)
        return freq

    def setRadiofreq(self, freq):
        # The Radio freq value stored.
        # Open the json file holding the latest radio value
        # sdr = RtlSdr()
        # Use the latest value as your sample rate for your SDR device
        # sdr.sample_rate = freq
        freq1 = float(freq)
        print(freq1)
        return float(freq1)

    def RadioFreqUp(self, freq):
        # The Radio freq will change 1 value in the positive direction.
        freq1 = float(freq) + 10
        logger.info("Setting freq to: ")
        RtlCalls.setRadiofreq(RtlCalls, freq1)
        #RtlCalls.saveRadioFreq(RtlCalls, freq1)
        # return freq1

    #def RadioFreqDown(self, freq):
    #    # The Radio freq will change 1 value in the negative direction.
    #    freq1 = float(freq)
    #    freq1 -= 10
    #    logger.info("Setting freq to: ".format(freq))
    #    self.setRadiofreq(freq)
    #    self.saveRadioFreq(freq)
    #    return freq1

    def saveRadioFreq(self, freq):
        # Will save the state of the radio settings for future use.

        time.sleep(1)