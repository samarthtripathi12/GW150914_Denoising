# Gravitational Wave Signal Extraction from LIGO Data

Simulates the extraction and analysis of gravitational wave signals from LIGO H1 data using Python, with FFT, band-pass filtering, SNR computation, and optional high-pass validation.

---

## Abstract

This project simulates the detection and processing of gravitational wave signals from experimental LIGO data. It progressively explores signal analysis under:

1. **Raw data visualization**  
2. **Merger zoom and chirp identification**  
3. **Frequency-domain analysis via FFT**  
4. **Band-pass filtering and waveform recovery**  
5. **Signal-to-noise ratio analysis**  
6. **High-pass SNR validation**  

The simulations combine numerical data processing, visualization, and statistical validation to demonstrate real gravitational wave signatures and detection significance.

---

## Why This Project

- Provides a hands-on demonstration of experimental data handling.  
- Highlights signal processing techniques such as FFT and band-pass filtering.  
- Demonstrates quantitative assessment using SNR and high-pass validation.  
- Verifies the ability to extract a clean gravitational waveform from noisy data.  
- Combines static plots, animations, and metrics tables to bridge theory and computation.

---

## Development Iterations

- **v1.0:** Raw HDF5 data loaded, basic time-domain visualization.  
- **v2.0:** Band-pass filtering applied; waveform recovery achieved.  
- **v3.0:** SNR computation implemented; merger detection confirmed.  
- **v4.0:** High-pass SNR validation added; GIF creation for visualization.  

---

## Verification

- Raw HDF5 file exists and is accessible.  
- Full strain plot generated correctly.  
- Band-pass filtered waveform matches expected chirp structure.  
- SNR peak corresponds to merger time (~32s window).  
- High-pass filtered SNR curve stronger than original SNR.  
- Metrics (Max SNR, MSE) confirm waveform recovery and quantitative improvement.  

---

## Requirements

- Python 3.11+  
- NumPy  
- Matplotlib  
- h5py  
- (Optional) Numba for faster computation  

---

## Phase 1 — Data Acquisition

**Scientific Question:**  
“Can we acquire raw LIGO strain data correctly?”

**Description:**  
- Raw data downloaded from LIGO H1 repository.  
- Single HDF5 file (`H-H1_LOSC_4_V2-1126259446-32.hdf5`) contains 32 seconds of strain data.  

**Implementation:**  
- No scripts required for this phase.  
- Only data acquisition.  

**Static Plot:**  
 None  

**Animation:**  
 None  

**Key Features:**  
- Confirms successful download and integrity of raw data.  

**End-state / Outputs:**  
- File: `H-H1_LOSC_4_V2-1126259446-32.hdf5`  

**What This Proves:**  
- Correct acquisition of raw LIGO data.

---

## Phase 2 — Raw Data Load & Full Time Plot

**Scientific Question:**  
“Can we read and visualize the raw strain signal?”  

**Description:**  
- Time-domain plot of full 32-second strain.  
- Extremely noisy signal.  

**Implementation:**  
- Script: `Scripts/phase2_raw_plot.py`  
- Plot: Time (s) vs Strain  

**Static Plot:**  
![Phase 2: Raw Strain](plots/phase2_raw_plot_h1.png)  

**Animation:**  
 None  

**Key Features:**  
- Demonstrates ability to read HDF5 data.  
- Establishes baseline for noisy waveform.

**End-state / Outputs:**  
- Code: `Scripts/phase2_raw_plot.py`  
- Plot: `Plots/phase2_raw_plot_h1.png`  

**What This Proves:**  
- Can load experimental data and visualize noisy strain signals.

---

## Phase 3 — Merger Zoom (Chirp Visibility)

**Scientific Question:**  
“Can we identify the merger chirp in noisy data?”  

**Description:**  
- Zoom-in near merger time.  
- Oscillations increase to a peak and decay.  

**Implementation:**  
- Script: `Scripts/phase3_zoom_chirp.py`  
- Time-domain plot (zoomed)  

**Static Plot:**  
![Phase 3: Merger Zoom](plots/phase3_zoomed_chirp_h1.png)  

**Animation:**  
 None  

**Key Features:**  
- Shows gravitational wave structure despite noise.  

**End-state / Outputs:**  
- Code: `Scripts/phase3_zoom_chirp_h1.py`   
- Plot: `plots/phase3_zoomed_chirp_h1.png`   

**What This Proves:**  
- Can visualize signal evolution near merger.

---

## Phase 4 — FFT & Frequency-Domain Analysis

**Scientific Question:**  
“What is the frequency content of the noisy signal?”  

**Description:**  
- Frequency-domain analysis via FFT.  
- Identifies dominant frequency range (~20–500 Hz).  

**Implementation:**  
- Script: `Scripts/phase4_fft_flter.py`   
- Plot: Frequency (Hz) vs Amplitude  

**Static Plot:**  
![Phase 4: FFT Spectrum](plots/phase4_fft_spectrum.png)  

**Animation:**  
 None  

**Key Features:**  
- Diagnoses noise dominance at low frequencies.  
- Establishes frequency range for band-pass filtering.  

**End-state / Outputs:**  
- Code: `Scripts/phase4_fft_filter.py`  
- Plot: `plots/phase4_fft_spectrum.png`  

**What This Proves:**  
- Can perform FFT and identify signal frequency characteristics.

---

## Phase 5 — Band-Pass Filtering & Signal Recovery

**Scientific Question:**  
“Can we extract the clean gravitational waveform from noisy data?”  

**Description:**  
- Apply band-pass filter using FFT.  
- Retain frequencies ~20–500 Hz.  
- Inverse FFT to return to time domain.  

**Implementation:**  
- Script: `Scripts/phase5_bandpass_filter.py`  
- Plot two curves: original noisy vs filtered signal  

**Static Plot:**  
![Phase 5: Cleaned vs Noisy](plots/phase5_h1_frequency_vs_strain.png)  

**Animation:**  
 None  

**Key Features:**  
- Chirp now clearly visible.  
- Time-domain comparison of raw and filtered signals.  

**End-state / Outputs:**  
- Code: `Scripts/phase5_bandpass_filter.py`  
- Plot: `plots/phase5_h1_frequency_vs_strain.png`  

**What This Proves:**  
- Band-pass filtering successfully recovers the gravitational wave signal.

---

## Phase 6 — SNR / Detection Significance

**Scientific Question:**  
“How significant is the detected signal?”  

**Description:**  
- Compute SNR from filtered signal.  
- Peak SNR corresponds to merger.  

**Implementation:**  
- Script: `Scripts/phase6_matched_filter.py`  
- Plot: Time vs SNR  

**Static Plot:**  
![Phase 6: SNR vs Time](plots/phase6_snr.png)  

**Animation:**  
 None  

**Key Features:**  
- Converts physics into statistical detection significance.  

**End-state / Outputs:**  
- Code: `Scripts/phase6_matched_filter.py`  
- Plot: `Plots/plots/phase6_snr.png`  

**What This Proves:**  
- Confirms gravitational wave detection via SNR.

---

## Phase 6b — High-Pass Validation (Optional, Stronger Analysis)

**Scientific Question:**  
“Does high-pass filtering improve detection clarity?”  

**Description:**  
- Compare original SNR vs high-pass filtered SNR.  
- Filtered SNR peak stronger and cleaner.  

**Implementation:**  
- Script: `Scripts/phase6_5_highpass_validation.py`  
- Plot: Time vs SNR (two curves)  

**Static Plot:**  
![Phase 6b: High-Pass SNR](plots/phase6_5_snr_validation.png)  

**Animation (GIF of Comparison):**  
![Denoising GIF](plots/denoising_progress.gif)  

**Key Features:**  
- Original (blue) vs high-pass (orange) SNR comparison.  

**End-state / Outputs:**  
- Code: `Scripts/phase6_5_highpass_validation.py`  
- Plot: `Plots/phase6-5_snr_validation.png`  
- GIF: `Plots/denoising_progress.gif`  
- Metrics CSV: `Plots/snr_metrics.csv`  

**Metrics Table Example:**  

| Metric       | Raw SNR | Filtered SNR | Notes                  |
|-------------|---------|--------------|------------------------|
| Max SNR     | 3.854   | 4.016        | Peak enhancement       |
| MSE (strain)| 1.23e-17 | -           | Signal reconstruction  |

---

## Step-by-Step Computational Pipeline

1. **Load raw HDF5 data** → visualize full strain waveform.  
2. **Zoom near merger** → identify chirp structure.  
3. **FFT analysis** → identify frequency range of signal.  
4. **Band-pass filter** → remove unwanted frequencies.  
5. **Inverse FFT** → recover time-domain signal.  
6. **Compute SNR** → evaluate detection significance.  
7. **High-pass validation (optional)** → compare SNR improvement.  
8. **Generate plots, GIFs, metrics table** → document results.  

---

## Conclusion

This project demonstrates **gravitational wave signal extraction** from experimental LIGO data, progressing from:

1. Raw noisy strain (Phase 2)  
2. Merger zoom & chirp identification (Phase 3)  
3. Frequency-domain diagnosis (Phase 4)  
4. Band-pass filtering & waveform recovery (Phase 5)  
5. SNR computation (Phase 6)  
6. Optional high-pass SNR validation (Phase 6b)  

- Numerical methods successfully extracted the gravitational waveform.  
- SNR analysis quantifies detection significance.  
- GIFs and metrics provide a visually compelling and quantitative presentation.  

The work combines **experimental data handling, signal processing, statistical analysis, and visualization** to deliver a polished, research-level demonstration of gravitational wave signal detection.
