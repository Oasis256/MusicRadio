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
from threading import Thread
from contextlib import closing
#matplotlib.use('Agg') # necessary for headless mode
# see http://stackoverflow.com/a/3054314/3524528


class populateRadioData(object):

    def grabRaw(self, F_station):

        with closing(RtlSdr()) as sdr:  
            sdr.sample_rate = sample_rate = 240000
            sample_rate_fm = 240000
            sdr.center_freq = 101.1e6
            sdr.gain = 20
            iq_samples = sdr.read_samples(4976640)

            iq_comercial = signal.decimate(iq_samples, sample_rate//sample_rate_fm)

            angle_comercial = np.unwrap(np.angle(iq_comercial))
            demodulated_comercial = np.diff(angle_comercial)

            audio_rate = 48000
            audio_comercial = signal.decimate(demodulated_comercial, \
            sample_rate_fm//audio_rate, zero_phase=True)

            audio_comercial = np.int16(1e4*audio_comercial)
            wavfile.write("comercial_demodulated.wav", rate=audio_rate, data=audio_comercial)

 
    def playBack(self):

        #startup = 1
        #if startup == 1:
        #    time.sleep(7)
        #    startup += 1

        import wave
        chunk = 1024
        #open a wav format music  
        f = wave.open("comercial_demodulated.wav","rb")
        #instantiate PyAudio  
        p = pyaudio.PyAudio()  
        #open stream  
        stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)
     
        #read data  
        data = f.readframes(chunk)  

        #play stream  
        while data:  
            stream.write(data)      
            data = f.readframes(chunk)
                
            #stop stream  
            #stream.stop_stream()  
            #stream.close()  

            #close PyAudio  
            #p.terminate()
        
    
if __name__ == "__main__":
                    
    
    while True:
        station = 101.1e6
        t1 = Thread(target=populateRadioData.grabRaw(populateRadioData, station))
        t2 = Thread(target=populateRadioData.playBack(populateRadioData))
        t1.start()  
        t2.start()
        

        
        
        
