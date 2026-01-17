# File: Scripts/create_gif_and_metrics.py
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import csv

# --- Ensure output folder exists ---
if not os.path.exists('Plots'):
    os.makedirs('Plots')

# --- Load data ---
data = np.loadtxt('Denoised.csv', delimiter=',', skiprows=1)
time = data[:,0]
raw = data[:,1]
filtered = data[:,2]

# --- Store frames ---
filenames = []

# --- Frame 1: Raw signal ---
plt.figure(figsize=(10,4))
plt.plot(time, raw, color='blue')
plt.title('Step 1: Raw Signal')
plt.xlabel('Time [s]')
plt.ylabel('Strain')
plt.ylim(np.min(raw)*1.1, np.max(raw)*1.1)
fname = 'Plots/frame1.png'
plt.savefig(fname)
filenames.append(fname)
plt.close()

# --- Frame 2: FFT spectrum ---
fft_vals = np.fft.rfft(raw)
freqs = np.fft.rfftfreq(len(raw), d=(time[1]-time[0]))
plt.figure(figsize=(10,4))
plt.plot(freqs, np.abs(fft_vals), color='green')
plt.title('Step 2: FFT Spectrum (Raw Signal)')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
fname = 'Plots/frame2.png'
plt.savefig(fname)
filenames.append(fname)
plt.close()

# --- Frame 3: Overlay Raw + Filtered ---
plt.figure(figsize=(10,4))
plt.plot(time, raw, color='blue', alpha=0.5, label='Raw')
plt.plot(time, filtered, color='orange', alpha=0.8, label='Filtered')
plt.title('Step 3: Raw + Filtered')
plt.xlabel('Time [s]')
plt.ylabel('Strain')
plt.ylim(np.min(raw)*1.1, np.max(raw)*1.1)
plt.legend()
fname = 'Plots/frame3.png'
plt.savefig(fname)
filenames.append(fname)
plt.close()

# --- Create GIF ---
images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('Plots/denoising_progress.gif', images, duration=2.0)
print("GIF created at Plots/denoising_progress.gif")

# --- Compute Metrics ---
max_raw = np.max(np.abs(raw))
max_filtered = np.max(np.abs(filtered))

snr_raw = np.max(np.abs(raw)) / np.std(raw)
snr_filtered = np.max(np.abs(filtered)) / np.std(filtered)

mse = np.mean((raw - filtered)**2)

print(f"Max amplitude - Raw: {max_raw:.5e}, Filtered: {max_filtered:.5e}")
print(f"SNR peak - Raw: {snr_raw:.3f}, Filtered: {snr_filtered:.3f}")
print(f"MSE (raw vs filtered): {mse:.5e}")

# --- Save Metrics CSV ---
with open('Plots/snr_metrics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Metric', 'Raw', 'Filtered'])
    writer.writerow(['Max Amplitude', max_raw, max_filtered])
    writer.writerow(['SNR Peak', snr_raw, snr_filtered])
    writer.writerow(['MSE (strain)', mse, '-'])

print("Metrics saved at Plots/snr_metrics.csv")
