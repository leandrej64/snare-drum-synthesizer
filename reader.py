from instrument import Instrument
from scipy.io import wavfile
import numpy as np
class Reader(Instrument): 
    def __init__(self,filename):
            super().__init__()
            sampling_frequency, wave = wavfile.read(filename)
            self.sampling_frequency = sampling_frequency
            self.wave = wave
            self.support = np.linspace(0,self.wave.shape[0]/sampling_frequency,self.wave.shape[0])
          
    def build():
        return