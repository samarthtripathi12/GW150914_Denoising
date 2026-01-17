# ==============================
# Phase 5: Band-pass Filtering
# ==============================

import numpy as np
import h5py
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# ------------------------------
# Load LIGO H1 data
# ------------------------------
FILE_NAME = "H-H1_LOSC_4_V2-1126259446-32.hdf5"

with h5py.File(FILE_NAME, "r") as f:
    strain = f["strain"]["Strain"][:]
    sample_rate = f["strain"]["Strain"].attrs["SampleRate"]

time = np.arange(len(strain)) / sample_rate

# ------------------------------
# Band-pass filter (20–500 Hz)
# ------------------------------
lowcut = 20.0
highcut = 500.0
nyquist = 0.5 * sample_rate

low = lowcut / nyquist
high = highcut / nyquist

b, a = butter(4, [low, high], btype="band")
filtered_strain = filtfilt(b, a, strain)

# ------------------------------
# Save filtered data
# ------------------------------
np.savetxt(
    "phase5_filtered_signal.csv",
    np.column_stack((time, filtered_strain)),
    delimiter=",",
    header="time,filtered_strain",
    comments=""
)

# ------------------------------
# Plot comparison
# ------------------------------
plt.figure(figsize=(12, 5))
plt.plot(time, strain, color="gray", alpha=0.4, label="Raw signal")
plt.plot(time, filtered_strain, color="blue", label="Filtered signal")
plt.xlim(16.0, 17.0)   # zoom near merger
plt.xlabel("Time (s)")
plt.ylabel("Strain")
plt.title("Phase 5: Band-pass Filtered Gravitational Wave Signal")
plt.legend()
plt.tight_layout()

plt.savefig("phase5_filtered_waveform.png", dpi=300)
plt.show()

print("✅ Phase 5 complete.")
print("Saved files:")
print(" - phase5_filtered_signal.csv")
print(" - phase5_filtered_waveform.png")
