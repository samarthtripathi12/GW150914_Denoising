import numpy as np
import h5py
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# =========================
# Load strain data
# =========================
filename = "H-H1_LOSC_4_V2-1126259446-32.hdf5"

with h5py.File(filename, 'r') as f:
    strain = f['strain']['Strain'][:]
    dt = f['strain']['Strain'].attrs['Xspacing']
    fs = 1.0 / dt

time = np.arange(len(strain)) * dt

# =========================
# High-pass filter (30 Hz)
# =========================
def highpass(data, cutoff, fs, order=4):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    return filtfilt(b, a, data)

filtered_strain = highpass(strain, cutoff=30, fs=fs)

# =========================
# Simple SNR proxy
# =========================
snr_raw = np.abs(strain) / np.std(strain)
snr_filtered = np.abs(filtered_strain) / np.std(filtered_strain)

# =========================
# Plot comparison
# =========================
plt.figure(figsize=(10,5))
plt.plot(time, snr_raw, label="Original SNR", alpha=0.6)
plt.plot(time, snr_filtered, label="High-pass filtered SNR (>30 Hz)", linewidth=2)

plt.xlabel("Time (s)")
plt.ylabel("Signal-to-Noise Ratio")
plt.title("SNR Comparison Before and After Low-Frequency Noise Suppression")
plt.legend()
plt.xlim(0, 32)

plt.tight_layout()
plt.savefig("phase6_5_snr_validation.png", dpi=300)
plt.show()