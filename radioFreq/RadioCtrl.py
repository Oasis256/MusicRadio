import sys

sys.path.append("../config")

from RadioConfig import RadioConfig

radioCfg = RadioConfig()


class RadioCtrl:
    currentBandName = None  # type: object
    currentDemod = None  # type: object
    currentFrequency = None  # type: object
    radioCfg = None
    num_records = 0

    # Requires a datastore object from RadioConfig
    # Provides methods to change stations & bands.

    def __init__(self, radioCfg):
        self.radioCfg = radioCfg
        self.datastore = self.radioCfg.load("../config/RadioConfig.json")
        self.num_records = self.radioCfg.numRecords()
        self.currentIndex = 0
        self.currentFrequency = self.datastore["radio_config"]["stations"][self.currentIndex]["freq_start"]
        self.currentDemod = self.datastore["radio_config"]["stations"][self.currentIndex]["demod"]
        self.currentBandName = self.datastore["radio_config"]["stations"][self.currentIndex]["name"]

    @property
    def getCurrFreqency(self):
        # Call this any time, or specifically after changing to the next band.
        return self.currentFrequency

    @property
    def getCurrDemod(self):
        # Call this any time, or specifically after changing to the next band.
        return self.currentDemod

    @property
    def getCurrBandName(self):
        # Call this any time, or specifically after changing to the next band.
        return self.currentBandName

    @property
    def getNextFrequency(self):
        # Change to next frequency, 1 "jump" more
        self.currentFrequency += self.datastore["radio_config"]["stations"][self.currentIndex]["freq_jump"]

        # Check for rolling past the end of the allocated band.
        if self.currentFrequency > self.datastore["radio_config"]["stations"][self.currentIndex]["freq_end"]:
            self.currentFrequency = self.datastore["radio_config"]["stations"][self.currentIndex]["freq_start"]

        return self.currentFrequency

    @property
    def getPrevFrequency(self):
        # Change to previous frequency, 1 "jump" less
        self.currentFrequency -= self.datastore["radio_config"]["stations"][self.currentIndex]["freq_jump"]

        # Check for rolling past the end of the allocated band.
        if self.currentFrequency < self.datastore["radio_config"]["stations"][self.currentIndex]["freq_start"]:
            self.currentFrequency = self.datastore["radio_config"]["stations"][self.currentIndex]["freq_end"]

        return self.currentFrequency

    def setNextBand(self):
        # Change to next mode / band.  Increase our index by 1.
        self.currentIndex += 1
        if self.currentIndex > self.num_records - 1:
            self.currentIndex = 0

        self.currentFrequency = self.datastore["radio_config"]["stations"][self.currentIndex]["freq_start"]
        self.currentDemod = self.datastore["radio_config"]["stations"][self.currentIndex]["demod"]
        self.currentBandName = self.datastore["radio_config"]["stations"][self.currentIndex]["name"]
