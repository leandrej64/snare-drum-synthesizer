import numpy as np 

from snare import Snare
from generator import Generator
from reader import Reader

if __name__ == "__main__":
    

    """drum snare target"""

    target = Reader("audio/target.wav")
    #target.plot_spectogram(filename="figures/target_spectogram.pdf")
    #target.plot_wave(filename="figures/target_wave.pdf")
    

    """sample example"""

    snare = Snare(180,30)
    #snare.plot_spectogram(filename="figures/sample_spectogram.pdf")
    #snare.plot_wave(filename="figures/sample_wave.pdf")
    snare.store_audio('audio/sample.wav')


    """uncomment to generate broad samples""" 
  
    
    # decays = np.linspace(10,50,10)
    # frequencies = np.linspace(150,250,50)
    # parameters = [{'name':f"f_{f:.2f}_d_{d:.2f}", 'list':[f,d]} for d in decays for f in frequencies]
    # generator = Generator(Snare,parameters,max_workers=50)
    # generator.generate()
    
    



