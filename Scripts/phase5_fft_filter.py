# ----------------------------------------
# Phase 5: FFT and Band-Pass Filtering
# ----------------------------------------

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.signal import butter, filtfilt

# File path
file = r"C:\Users\window11\Desktop\ligo_gravitational\GW150914_Denoising\H-H1_LOSC_4_V2-1126259446-32.hdf5"

# Load strain
with h5py.File(file, 'r') as hf:
    strain = hf['strain/Strain'][:]

fs = 4096
N = len(strain)
time = np.arange(N) / fs

# -------------------------------
# FFT (Frequency Domain)
# -------------------------------
fft_vals = np.fft.rfft(strain)
freqs = np.fft.rfftfreq(N, 1/fs)

# Plot frequency spectrum
plt.figure(figsize=(10, 4))
plt.semilogy(freqs, np.abs(fft_vals))
plt.title("GW150914 H1 Frequency Spectrum")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)

os.makedirs("plots", exist_ok=True)
plt.savefig("plots/Phase5_Frequency_Spectrum.png", dpi=300)
plt.show()

# -------------------------------
# Band-pass filter (30–300 Hz)
# -------------------------------
lowcut = 30
highcut = 300
order = 4

b, a = butter(order, [lowcut/(fs/2), highcut/(fs/2)], btype='band')
filtered = filtfilt(b, a, strain)

# Zoom around merger again
center = N // 2
window = int(0.1 * fs)

t_zoom = time[center-window:center+window]
raw_zoom = strain[center-window:center+window]
filt_zoom = filtered[center-window:center+window]

# Plot comparison
plt.figure(figsize=(10, 4))
plt.plot(t_zoom, raw_zoom, label="Raw", alpha=0.5)
plt.plot(t_zoom, filt_zoom, label="Filtered", linewidth=2)
plt.title("GW150914 H1 – Filtered vs Raw Chirp")
plt.xlabel("Time [s]")
plt.ylabel("Strain")
plt.legend()
plt.grid(True)

plt.savefig("plots/Phase5_Filtered_Chirp_H1.png", dpi=300)
plt.show()

print("✅ Phase 5 complete: FFT and filtering successful.")