import numpy as np
import h5py
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# =========================
# PHASE 4: FFT + FILTERING
# =========================

# --------- FILE PATH ---------
file_path = "H-H1_LOSC_4_V2-1126259446-32.hdf5"

# --------- LOAD DATA ---------
with h5py.File(file_path, "r") as hf:
    strain = hf["strain/Strain"][:]
    time = hf["strain/Strain"].attrs["Xstart"] + \
           np.arange(len(strain)) * hf["strain/Strain"].attrs["Xspacing"]

fs = 4096  # Sampling rate (Hz)

# --------- FFT (Frequency Domain) ---------
fft_data = np.fft.fft(strain)
freqs = np.fft.fftfreq(len(strain), d=1/fs)

plt.figure(figsize=(8,4))
plt.plot(freqs[:len(freqs)//2], np.abs(fft_data[:len(freqs)//2]))
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("Phase 4: FFT of Raw LIGO Strain Data")
plt.tight_layout()
plt.savefig("plots/Phase4_FFT_Spectrum.png", dpi=300)
plt.show()

# --------- BANDPASS FILTER (20–500 Hz) ---------
lowcut = 20
highcut = 500

b, a = butter(
    N=4,
    Wn=[lowcut/(fs/2), highcut/(fs/2)],
    btype="band"
)

filtered_strain = filtfilt(b, a, strain)

# --------- PHASE 5 OUTPUT: TIME-DOMAIN COMPARISON ---------
plt.figure(figsize=(10,4))
plt.plot(time, strain, label="Raw strain", alpha=0.5)
plt.plot(time, filtered_strain, label="Filtered strain", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Strain")
plt.title("Phase 5: Before vs After Band-Pass Filtering")
plt.legend()
plt.tight_layout()
plt.savefig("plots/Phase5_BeforeAfter_Filtered.png", dpi=300)
plt.show()

# --------- SAVE FILTERED DATA ---------
np.savetxt(
    "plots/Denoised_Strain.csv",
    np.column_stack((time, filtered_strain)),
    delimiter=",",
    header="Time(s),Filtered_Strain",
    comments=""
)

print("✅ Phase 4 FFT plot saved")
print("✅ Phase 5 filtered waveform plot saved")
print("✅ Denoised strain CSV saved")

