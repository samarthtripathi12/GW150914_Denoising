# Gravitational Wave Signal Denoising — GW150914 H1

## Introduction
This project demonstrates the denoising and analysis of a real gravitational wave signal detected by LIGO (event GW150914, H1 detector).  
The goal is to recover the binary black hole merger signal from noisy data, applying FFT-based filtering and signal processing techniques.  

**Why this project:**  
- Uses **real Nobel Prize-winning physics data** from LIGO.  
- Demonstrates advanced **signal processing** without needing complex general relativity.  
- Showcases the ability to **handle data, reduce noise, and visualize results professionally**.  

**What I learned:**  
- How to access and process LIGO HDF5 strain data.  
- Data visualization and interpretation of gravitational wave signals.  
- Applying FFT, band-pass, and high-pass filters.  
- Comparing signal-to-noise ratios before and after denoising.  
- Producing professional-quality plots for scientific communication.

---

## Folder Structure

GW150914_Denoising/
├─ scripts/ # Python scripts for each phase
├─ plots/ # Generated images
├─ H-H1_LOSC_4_V2-1126259446-32.hdf5 # Raw strain data
├─ README.md # Project description

yaml
Copy code

---

## Project Phases

### Phase 1 — Data Acquisition
**Goal:** Obtain real LIGO gravitational wave strain data.  
**Tasks:**  
- Download HDF5 file from LIGO Open Science Center (H1 detector, 4 kHz, 32 seconds).  

**End Result / Demonstrate:**  
- Raw HDF5 file available locally (`H-H1_LOSC_4_V2-1126259446-32.hdf5`).  
- Demonstrates ability to **access and handle real experimental datasets**.

---

### Phase 2 — Data Exploration & Visualization
**Goal:** Understand the raw strain data.  
**Tasks:**  
- Load HDF5 file in Python.  
- Plot full 32-second signal.  
- Identify the binary black hole merger peak.  

**End Result / Demonstrate:**  
- Raw strain plot (`phase3_raw_plot.png`).  
- Zoomed-in merger plot (`phase4_zoom_chirp.png`).  
- Shows ability to **visually interpret raw experimental data**.

---

### Phase 3 — Data Preprocessing
**Goal:** Prepare data for denoising.  
**Tasks:**  
- Align time array with strain samples.  
- Normalize or remove unnecessary metadata.  

**End Result / Demonstrate:**  
- Clean strain array ready for FFT filtering.  
- Shows understanding of **data preparation techniques**.

---

### Phase 4 — FFT & Band-Pass Filtering
**Goal:** Isolate the gravitational wave signal and remove noise.  
**Tasks:**  
- Apply FFT to transform data to frequency domain.  
- Apply band-pass filter (e.g., 20–500 Hz).  
- Apply inverse FFT to recover cleaned waveform.  

**End Result / Demonstrate:**  
- Denoised strain array.  
- Frequency spectrum showing filtered signal (`phase5_fft_filtered.png`).  
- Demonstrates **signal processing skills and understanding of noise vs signal**.

---

### Phase 5 — Comparison & Visualization
**Goal:** Show the effectiveness of denoising.  
**Tasks:**  
- Plot before vs after denoising.  
- Highlight the merger in a zoomed-in view.  

**End Result / Demonstrate:**  
- Before vs after plot (`phase5_fft_filtered.png`).  
- Shows **clear improvement and highlights the binary black hole merger event**.

---

### Phase 6 — Matched Filter / SNR
**Goal:** Present final results professionally.  
**Tasks:**  
- Compute signal-to-noise ratio (SNR) using matched filtering.  
- Plot SNR vs time.  

**End Result / Demonstrate:**  
- SNR plot (`phase6_snr.png`).  
- Shows **final signal clarity and peak detection**.  
- Demonstrates **mastery of the data pipeline and analysis**.

---

### Phase 6.5 — Optional Robustness Check
**Goal:** Verify robustness of noise suppression.  
**Tasks:**  
- Apply high-pass filter (>30 Hz).  
- Compare SNR before and after filter.  

**End Result / Demonstrate:**  
- SNR comparison plot (`phase6_5_snr_validation.png`).  
- Shows **handling low-frequency noise and verification of results**.

---

## Final Conclusion
- Successfully denoised a real gravitational wave signal from LIGO (GW150914 H1).  
- Binary black hole merger event clearly visible.  
- Demonstrates **full pipeline**: raw data → processing → filtering → visualization → professional presentation.  

**Deliverables included:**  
- Plots: `phase3_raw_plot.png`, `phase4_zoom_chirp.png`, `phase5_fft_filtered.png`, `phase6_snr.png`, `phase6_5_snr_validation.png`.  
- Raw HDF5 data: `H-H1_LOSC_4_V2-1126259446-32.hdf5`.  

---

## LIGO Data Source
- [GW150914 H1 strain data](https://www.gw-openscience.org/events/GW150914/)  

---

## How to Run
1. Install Python packages: `numpy`, `scipy`, `matplotlib`, `h5py`.  
2. Run scripts in order:
```bash
python scripts/phase3_raw_plot.py
python scripts/phase4_zoom_chirp.py
python scripts/phase5_fft_filter.py
python scripts/phase6_matched_filter.py
python scripts/phase6_5_highpass_validation.py