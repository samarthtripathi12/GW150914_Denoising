# Gravitational Wave Signal Extraction (GW150914)

Extracting and validating the first directly detected gravitational wave using real LIGO interferometer data.

---

## Abstract

This project analyzes real gravitational wave strain data from the LIGO Hanford (H1) detector corresponding to the historic **GW150914** event.  
It progressively reconstructs the gravitational wave signal buried in detector noise using a complete scientific pipeline:

- Time-domain strain analysis  
- Frequency-domain (FFT) characterization  
- Band-pass filtering and denoising  
- Quantitative validation using Signal-to-Noise Ratio (SNR)

The project bridges **General Relativity, experimental physics, and computational signal processing**, reproducing the essential steps used by real gravitational-wave observatories.

---

## Why This Project

- Uses **real LIGO interferometer data**
- Demonstrates **how gravitational waves are detected experimentally**
- Connects **Einstein’s General Relativity to observational evidence**
- Shows the **full pipeline from raw noise to physical signal**
- Emphasizes **scientific rigor through quantitative metrics**

---

## Development Iterations

- **v1.0:** Raw strain visualization (signal fully buried in noise)  
- **v2.0:** Frequency-domain identification via FFT  
- **v3.0:** Band-pass filtering and denoising  
- **v4.0:** Quantitative validation using SNR metrics  

---

## Verification

- Event: **GW150914**
- Detector: **LIGO Hanford (H1)**
- Recovered chirp matches published LIGO results
- SNR improves after filtering
- Results consistent with LOSC documentation

---

## Requirements

- Python 3.11+
- NumPy
- SciPy
- Matplotlib
- h5py

---

## Phase 1: Raw Gravitational Wave Strain

**Scientific Question:**  
What does the LIGO detector actually record?

**Description:**  
Raw strain data is loaded directly from the LIGO HDF5 file with no preprocessing.  
The gravitational wave signal is completely buried inside detector noise.

**Implementation:**

- Load strain and time arrays
- Plot time-domain strain

**Static Plot:**  
`Plots/phase1_raw_strain.png`

**Key Features:**

- Time vs strain
- No visible chirp
- Noise-dominated signal

**End-state / Outputs:**

- Code: `Scripts/phase1_load_strain.py`
- Static plot: `Plots/phase1_raw_strain.png`

**What This Proves:**

- Gravitational waves are **not visually detectable** without signal processing.

---

## Phase 2: Frequency-Domain Analysis (FFT)

**Scientific Question:**  
Where does the gravitational wave signal exist in frequency space?

**Description:**  
A Fast Fourier Transform (FFT) is applied to the raw strain to identify frequency bands containing physical signal content.

**Implementation:**

- FFT computation
- Amplitude spectrum visualization

**Static Plot:**  
`Plots/phase2_fft_spectrum.png`

**Key Features:**

- Frequency-localized signal content
- Noise-dominated regions clearly identified

**End-state / Outputs:**

- Code: `Scripts/phase2_fft_analysis.py`
- Static plot: `Plots/phase2_fft_spectrum.png`

**What This Proves:**

- Gravitational wave signals are **frequency-localized**, enabling effective filtering.

---

## Phase 3: Band-Pass Filtering & Denoising

**Scientific Question:**  
Can the gravitational wave be recovered from noise?

**Description:**  
A band-pass filter is applied using the frequency range identified in Phase 2, isolating the gravitational wave signal.

**Implementation:**

- SciPy band-pass filter
- Reconstruction of filtered strain

**Static Plot:**  
`Plots/phase3_filtered_strain.png`

**Overlay Plot:**  
`Plots/phase3_raw_vs_filtered.png`

**Key Features:**

- Clear chirp structure
- Direct comparison of raw vs filtered signal

**End-state / Outputs:**

- Code: `Scripts/phase3_bandpass_filter.py`
- Static plots:
  - `Plots/phase3_filtered_strain.png`
  - `Plots/phase3_raw_vs_filtered.png`
- Data file: `Denoised.csv`

**What This Proves:**

- The gravitational wave signal can be recovered **without distorting physical information**.

---

## Phase 4: Quantitative Validation (SNR & Metrics)

**Scientific Question:**  
Is the recovered signal statistically significant?

**Description:**  
Signal-to-noise ratio (SNR) is computed before and after filtering to quantitatively validate improvement.

**Implementation:**

- Numerical SNR calculation
- Metric export to CSV

**Metrics Output:**  
`Plots/snr_metrics.csv`

**Key Features:**

- Objective numerical validation
- Clear improvement after filtering

**End-state / Outputs:**

- Code: `Scripts/phase4_snr_metrics.py`
- Metrics file: `Plots/snr_metrics.csv`

**What This Proves:**

- The recovered signal is **statistically meaningful**, not a visual artifact.

---

## Phase 5: Phase-Wise Visualization (Pipeline Summary)

**Scientific Question:**  
Can the full detection pipeline be summarized visually?

**Description:**  
Representative outputs from each phase are combined into a phase-wise visualization.

**Animation:**  
`Plots/denoising_progress.gif`

**Note:**  
This animation is **phase-based, not motion-based**.  
Each frame represents a distinct computational stage, which is scientifically correct.

**End-state / Outputs:**

- Animation: `Plots/denoising_progress.gif`

**What This Proves:**

- The gravitational-wave detection pipeline is **transparent and reproducible**.

---

## Step-by-Step Computational Pipeline

1. Load raw LIGO strain data  
2. Visualize time-domain strain  
3. Perform FFT analysis  
4. Design band-pass filter  
5. Recover filtered signal  
6. Compute SNR metrics  
7. Export quantitative results  
8. Generate phase-wise visualization  

---

## Conclusion

This project reconstructs the first directly detected gravitational wave using real LIGO interferometer data.  
Starting from raw detector noise, the signal is extracted through frequency analysis, filtering, and quantitative validation.

The work combines **computational physics, experimental data analysis, validation, and visualization** to deliver a fully reproducible, scientifically rigorous gravitational-wave detection pipeline.
