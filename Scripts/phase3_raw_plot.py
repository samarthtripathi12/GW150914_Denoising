# -------------------------------
# Phase 3: Load and visualize GW150914 H1 raw strain
# -------------------------------

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

# File path
file = r"C:\Users\window11\Desktop\ligo_gravitational\GW150914_Denoising\H-H1_LOSC_4_V2-1126259446-32.hdf5"

if not os.path.exists(file):
    raise FileNotFoundError("HDF5 file not found")

# Load data
with h5py.File(file, 'r') as hf:
    strain = hf['strain/Strain'][:]   # ✅ CORRECT PATH

# Sampling rate
fs = 4096
N = len(strain)
time = np.arange(N) / fs

# Plot
plt.figure(figsize=(12, 4))
plt.plot(time, strain, color='black', linewidth=0.8)
plt.title("GW150914 H1 Raw Strain (32 seconds)")
plt.xlabel("Time [s]")
plt.ylabel("Strain")
plt.grid(True)

# Save output
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/Phase3_Raw_H1.png", dpi=300)
plt.show()

print("✅ Phase 3 complete: Raw strain plotted and saved.")
