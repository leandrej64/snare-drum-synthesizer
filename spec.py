from scipy.signal import spectrogram
import matplotlib.pyplot as plt
import numpy as np

class Spectrogram:
    
    def __init__(self, wave, sampling_frequency=44100, nperseg=256, fmax=1000):
        self.sampling_frequency = sampling_frequency
        self.fmax = fmax
        f, t, sxx = spectrogram(wave, fs=sampling_frequency,
                                nperseg=nperseg,window='hann', scaling='spectrum')
    
        sxx_db = 10 * np.log10(sxx + 1e-12)
        mask = f <= fmax
        self.frequencies = f[mask]
        self.times = t * 1000 
        self.matrix = sxx_db[mask, :]

    def plot(self,filename=False):
        fig, ax = plt.subplots(figsize=(8, 5))
        im = ax.pcolormesh(
            self.times,
            self.frequencies,
            self.matrix,
            cmap="magma",
            shading="gouraud",
            rasterized=True
        )

        ax.set_xlabel("Time (ms)")
        ax.set_ylabel("Frequency (Hz)")
        ax.set_title(f"Time-Frequency Heatmap ({len(self.times)} slices)")
        fig.colorbar(im, ax=ax, label="Energy (dB)")
        fig.tight_layout()

        if filename :
            fig.savefig(filename, dpi=300, bbox_inches="tight")

        plt.show()
        plt.close(fig) 

