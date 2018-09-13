from rtlsdr import RtlSdr
import numpy as np
import scipy.signal as signal
import scipy.io
from scipy.io import wavfile

import matplotlib
import time
import pyaudio
import sys
import os
import threading
import vlc
from contextlib import closing

class populateRadioData(object):


    def grabRaw(self, F_station):

        global num
        num = 2
        test = 	16384

        print("num at start =", num)

        while True:

                sdr = RtlSdr() 
                sdr.sample_rate = sample_rate = 240000
                sample_rate_fm = 240000
                sdr.center_freq = F_station
                sdr.gain = 4
                iq_samples = sdr.read_samples(test)

                iq_comercial = signal.decimate(iq_samples, sample_rate//sample_rate_fm)

                angle_comercial = np.unwrap(np.angle(iq_comercial))
                demodulated_comercial = np.diff(angle_comercial)

                audio_rate = 48000
                audio_comercial = signal.decimate(demodulated_comercial, \
                sample_rate_fm//audio_rate, zero_phase=True)

                print("num after process =", num)

                if num % 2 == 0:
                    
                    audio_comercial = np.int16(1e4*audio_comercial)
                    wavfile.write("comercial_demodulated.wav", rate=audio_rate, data=audio_comercial)
                    num = num + 1
                    print ("num after saved to wav in wav ",num)
                    print("File comercial demodulated 1 done")

                else :
                    audio_comercial = np.int16(1e4*audio_comercial)
                    wavfile.write("comercial_demodulated1.wav", rate=audio_rate, data=audio_comercial)
                    num = num + 1
                    print ("File comercial demodulated 2 done")
                    print("num afer save to wav in wav 2",num)
                    
                sdr.close()    
                time.sleep(.7)
           

class populatePlayBack(object):
    
        
    def playBack(self, file1 ,file2):
  
        while True:
        
            print("Starting PlayBack")

            playlist = [file1, file2]

            for song in playlist:
                player = vlc.MediaPlayer(song)
                player.play()

            time.sleep(1.5)
          
    
if __name__ == "__main__":
    
    station = 101.1e6
    file1 = "comercial_demodulated.wav"
    file2="comercial_demodulated1.wav"

    t1 = threading.Thread(target=populateRadioData.grabRaw, args=(populateRadioData, station))   
    #t2 = threading.Thread(target=populatePlayBack.playBack, args=(populatePlayBack, file1, file2))

    t1.setDaemon(True)
    #t2.setDaemon(True)

    t1.start()
    #t2.start()

    #populatePlayBack.playBack(populateRadioData)
        
        
        
