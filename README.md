# Snare Drum Synthesizer

## Overview

First version of a personal drum snare synthesizer.

Fully empirical: starting from a target acoustic waveform, with no prior background in audio synthesis, the goal is to iteratively approximate that wave.

## Getting started

**Prerequisites:** `numpy`, `scipy`, `matplotlib`

The target sample is available at `audio/target.wav`.

`main.py` synthesizes a snare hit using a set of "good" parameters, then sweeps the frequency and decay parameters to generate a batch of samples.

```bash
python main.py
```

Uncomment the last block in `main.py` to generate the full dataset (saved to `samples/`, not versioned).

See `snare_synthesizer.pdf` in this repo for the full synthesis method.
