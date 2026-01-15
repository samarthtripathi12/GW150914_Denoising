# --------------------------------
# Phase 4: Zoom into GW150914 merger chirp
# --------------------------------

import h5py
import numpy as np
import matplotlib.pyplot as plt
import os

# File path
file = r"C:\Users\window11\Desktop\ligo_gravitational\GW150914_Denoising\H-H1_LOSC_4_V2-1126259446-32.hdf5"

# Load strain
with h5py.File(file, 'r') as hf:
    strain = hf['strain/Strain'][:]

fs = 4096
N = len(strain)
time = np.arange(N) / fs

# -------------------------------
# Merger occurs near center
# Zoom ±0.1 seconds around center
# -------------------------------
center_index = N // 2
window = int(0.1 * fs)

zoom_strain = strain[center_index - window : center_index + window]
zoom_time = time[center_index - window : center_index + window]

# -------------------------------
# Plot zoomed chirp
# -------------------------------
plt.figure(figsize=(10, 4))
plt.plot(zoom_time, zoom_strain, color='blue', linewidth=1)
plt.title("GW150914 H1 – Zoomed Black Hole Merger Chirp")
plt.xlabel("Time [s]")
plt.ylabel("Strain")
plt.grid(True)

# Save
os.makedirs("plots", exist_ok=True)
plt.savefig("plots/Phase4_Zoomed_Chirp_H1.png", dpi=300)
plt.show()

print("✅ Phase 4 complete: Merger chirp isolated and plotted.")
