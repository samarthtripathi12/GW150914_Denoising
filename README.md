ravitational Wave Signal Denoising — GW150914

Computational Physics · Signal Processing · Experimental Validation

Abstract

This project reconstructs the first direct detection of gravitational waves (GW150914) using real LIGO interferometer data.
Through a structured, phase-wise computational pipeline, the raw detector strain is transformed into a clean astrophysical signal using frequency-domain analysis, band-pass filtering, and quantitative validation.

The work demonstrates how weak spacetime perturbations are extracted from extreme noise environments, combining time-domain analysis, Fourier methods, filtering theory, and signal-to-noise validation, supported by static plots and visual progression summaries.

Scientific Motivation

Gravitational waves are not directly visible in detector data. Their detection requires:

Careful frequency-domain reasoning

Noise suppression without signal distortion

Quantitative validation beyond visual inspection

This project answers:

Where the GW150914 signal resides in frequency space

How filtering reveals the chirp morphology

How signal quality improves objectively after denoising

Repository Structure

GW150914_Denoising/
│
├── Scripts/
│   ├── phase1_data_loading.py
│   ├── phase2_raw_time_domain.py
│   ├── phase3_fft_analysis.py
│   ├── phase4_bandpass_filter.py
│   ├── phase5_export_denoised_csv.py
│   └── create_gif_and_metrics.py
│
├── Data/
│   └── H-H1_LOSC_4_V2-1126259446-32.hdf5
│
├── Plots/
│   ├── phase2_raw_strain.png
│   ├── phase3_fft_spectrum.png
│   ├── phase4_filtered_strain.png
│   ├── phase4_overlay_raw_vs_filtered.png
│   ├── denoising_progress.gif
│   └── snr_metrics.csv
│
├── Denoised.csv
└── README.md

Development Progression

v1.0 — Raw strain visualization

v2.0 — Frequency-domain (FFT) analysis

v3.0 — Band-pass filtering

v4.0 — CSV-based reproducibility

v5.0 — Quantitative metrics + visual denoising summary

Phase-wise Scientific Breakdown
Phase 1 — Data Acquisition & Parsing
Scientific Question

“How is real gravitational-wave detector data structured?”

Description

The official LIGO LOSC HDF5 dataset for GW150914 is loaded, and strain data is extracted along with sampling metadata.

Outputs

In-memory strain array

Time axis

What This Establishes

Correct handling of real experimental data

Foundation for all subsequent analysis

Phase 2 — Raw Time-Domain Inspection
Scientific Question

“Is the gravitational wave visible in raw detector data?”

Description

The raw strain is plotted in the time domain.

Static Output

Plots/phase2_raw_strain.png

Observation

The signal is completely buried in noise, with no visible chirp structure.

What This Demonstrates

Direct visualization is insufficient

Necessity of signal processing

Phase 3 — Frequency-Domain Analysis (FFT)
Scientific Question

“Where does the signal exist in frequency space?”

Description

A Fast Fourier Transform (FFT) is applied to the raw strain to identify dominant frequency components.

Static Output

Plots/phase3_fft_spectrum.png

Observation

The GW150914 signal occupies a specific frequency band, justifying targeted filtering.

What This Demonstrates

Proper use of Fourier methods

Physical interpretation of frequency content

Phase 4 — Band-Pass Filtering & Signal Recovery
Scientific Question

“Can noise be suppressed without destroying the signal?”

Description

A band-pass filter isolates the frequency range associated with the inspiral–merger signal.

Static Outputs

Plots/phase4_filtered_strain.png

Plots/phase4_overlay_raw_vs_filtered.png

Observation

The chirp structure becomes clearly visible after filtering.

What This Demonstrates

Noise suppression effectiveness

Preservation of physical signal morphology

Phase 5 — Denoised Signal Export (Reproducibility)
Scientific Question

“Can the cleaned signal be reused and independently verified?”

Description

The raw and filtered signals are exported to a structured CSV file.

Output

Denoised.csv

Format

time, raw_strain, filtered_strain

What This Demonstrates

Reproducibility

Separation of processing and analysis

Phase 6 — Quantitative Validation (Metrics)
Scientific Question

“Is the signal objectively improved after filtering?”

Metrics Computed

Peak Signal-to-Noise Ratio (SNR)

Mean Squared Error (MSE)

Output

Plots/snr_metrics.csv

What This Demonstrates

Scientific rigor beyond visuals

Objective improvement measurement

Phase 7 — Denoising Progression Visualization (GIF)
Purpose

To visually summarize the entire denoising pipeline in a reviewer-friendly format.

Frames Included

Raw noisy strain (time domain)

FFT amplitude spectrum

Overlay of raw (blue) and filtered (orange) strain

Note:
This GIF is stage-based, not animated motion.
Each frame represents a distinct processing phase, which is scientifically correct and intentional.

Output

Plots/denoising_progress.gif

Final Results Summary
Aspect	Before Filtering	After Filtering
Noise Level	High	Suppressed
Chirp Visibility	Hidden	Clearly visible
Peak SNR	Lower	Higher

(Exact numerical values in snr_metrics.csv)

Requirements

Python 3.11+

NumPy

SciPy

Matplotlib

h5py

imageio

Conclusion

This project presents a complete, reproducible reconstruction of GW150914, demonstrating:

Real experimental data handling

Frequency-domain reasoning

Signal denoising and validation

Static and visual communication of results

The work reflects research-level computational physics practice, suitable for academic evaluation and technical portfolios.
