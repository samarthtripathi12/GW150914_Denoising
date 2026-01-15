import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate

# Load strain data
with h5py.File("H-H1_LOSC_4_V2-1126259446-32.hdf5", "r") as f:
    strain = f["strain/Strain"][:]
    fs = 4096  # Sampling rate

# Create a simple chirp template
t = np.linspace(0, 1, fs)
template = np.sin(2 * np.pi * (30 * t + 200 * t**2))

# Matched filtering via correlation
correlation = correlate(strain, template, mode="same")
snr = correlation / np.std(correlation)

# Time axis
time = np.arange(len(snr)) / fs

# Plot SNR
plt.figure(figsize=(10, 4))
plt.plot(time, snr)
plt.xlabel("Time (s)")
plt.ylabel("Signal-to-Noise Ratio (SNR)")
plt.title("Phase 6: Matched Filtering Result")
plt.grid(True)
plt.tight_layout()
plt.show()
