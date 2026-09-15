from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from spec import Spectrogram


class Instrument(ABC):

    def __init__(self, sampling_frequency=44100):
        self.sampling_frequency = sampling_frequency
        self.wave = None
        self.support = None

    @abstractmethod
    def build(self):
        pass

    def plot_wave(self,filename=None):
        wave_norm = self.wave / np.max(np.abs(self.wave))
        if self.wave is None:
            self.build()
        plt.figure(figsize=(10, 3))
        plt.plot(self.support, wave_norm, color="black", linewidth=0.5)
        plt.xlabel("Time (s)")
        plt.ylabel("Normalized Amplitude")
        plt.title("Waveform")
        plt.tight_layout()
        if filename :
            plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.show()

    def plot_spectogram(self,filename=None):  
        if self.wave is None:
            self.build()
        wave_norm = self.wave / np.max(np.abs(self.wave))
        spec = Spectrogram(wave_norm,self.sampling_frequency)
        spec.plot(filename)

    def store_audio(self, filename):
        if self.wave is None:
            self.build()
        wave_norm = self.wave / np.max(np.abs(self.wave))
        wavfile.write(filename, self.sampling_frequency, np.int16(wave_norm * 32767))

    