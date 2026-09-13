from instrument import Instrument
import numpy as np

class Snare(Instrument):

    def __init__(self,frequency,decay,sampling_frequency=44100,duration=0.3,impact=0.01):
        super().__init__()
        self.frequency = frequency
        self.decay = decay 
        self.sampling_frequency = sampling_frequency 
        self.duration = duration
        self.impact = impact
        self.support = np.linspace(0,duration,int(duration*sampling_frequency))
        self.peaks = None
        self.wave = None

    
    def get_peaks(self) :
        self.peaks = np.array([int((1/(4*self.frequency) + k*1/(2*self.frequency)) * self.sampling_frequency)
                          for k in range(0, int(self.duration*self.sampling_frequency/self.frequency))])


    def build(self):
        enveloppe_exp = np.array([np.exp(-self.decay*np.abs(t-self.impact)) for t in self.support])
        main_wave = np.array([np.sin(t*2*np.pi*self.frequency) for t in self.support]) * enveloppe_exp
        
        if self.peaks is None:
           self.get_peaks()

        t_1 = self.peaks[0]
        target_index = min(15, len(self.peaks) - 1) 
        t_5 = self.peaks[target_index]
        
        if t_5 > t_1:
            beta = np.log(1000) / (t_5 - t_1)
            A = 0.01 * np.exp(-beta * t_1)
        else:
            beta = 0
            A = 1
            
        for peak in self.peaks[1:]:
            noise = Noise(20, duration=(1 / (2 * self.frequency)),sampling_frequency=44100)
            noise.build()
            n = len(noise.wave)
            prob = min(A * np.exp(beta * peak), 1.0)
            bernoulli_mask = np.random.binomial(1, prob, size=n)
            padding = noise.wave * bernoulli_mask * enveloppe_exp[peak] * 0.5
            start_idx = int(peak - n/2)
            end_idx = start_idx + n
            if start_idx >= 0 and end_idx < len(main_wave):
                main_wave[start_idx:end_idx] += padding

        self.wave = main_wave
        return main_wave


class Noise(Instrument): 
    def __init__(self,decay,duration=0.1,sampling_frequency=44100):
        self.decay=decay
        self.sampling_frequency = sampling_frequency
        self.support = np.linspace(0,duration,int(duration*sampling_frequency))
        self.duration = duration 
        self.wave = None

    def build(self) : 
        impact = self.duration/2
        self.wave = np.array([np.random.uniform(-1,1)*np.exp(-np.abs(t-impact)*self.decay) for t in self.support])
        