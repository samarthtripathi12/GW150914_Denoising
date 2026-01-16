# Gravitational Wave Signal Denoising (GW150914 H1)

---

## **Introduction**

This project demonstrates **gravitational wave signal denoising** using real data from LIGO’s H1 detector for the binary black hole merger **GW150914**.  

The goal of the project is to:  

- Analyze a noisy gravitational wave signal.  
- Apply signal processing techniques to isolate the waveform.  
- Visualize and compare the raw and denoised signals.  
- Quantitatively evaluate improvements using signal-to-noise ratio (SNR).  

---

## **Project Workflow & Phases**

### **Phase 1 – Data Acquisition**
**Objective:** Obtain real strain data.  

**Output:**  
- Raw HDF5 file available locally (`Data/H-H1_LOSC_4_V2-1126259446-32.hdf5`)  

---

### **Phase 2 – Data Exploration & Visualization**
**Objective:** Understand and visualize the raw signal.  

**Outputs:**  
- **Raw signal:**  
![RawSignal](Plots/RawSignal.png)  
- **Merger zoom:**  
![MergerZoom](Plots/MergerZoom.png)  

---

### **Phase 3 – Data Preprocessing**
**Objective:** Prepare data for denoising.  

**Output:**  
- Cleaned strain array ready for FFT filtering.  

---

### **Phase 4 – FFT & Band-Pass Filtering**
**Objective:** Isolate the gravitational wave signal from noise.  

**Outputs:**  
- **Frequency spectrum after filtering:**  
![FilteredSpectrum](Plots/FilteredSpectrum.png)  

---

### **Phase 5 – Comparison & Visualization**
**Objective:** Show effect of denoising.  

**Outputs:**  
- **Before vs after denoising:**  
![BeforeAfter](Plots/BeforeAfter.png)  

---

### **Phase 6 – SNR Analysis**
**Objective:** Evaluate denoising performance quantitatively.  

**Outputs:**  
- **SNR over time:**  
![SNR](Plots/SNR_Plot.png)  

---

### **Phase 6.5 – High-Pass Noise Suppression**
**Objective:** Remove low-frequency noise and highlight improvement.  

**Outputs:**  
- **SNR comparison before and after high-pass filtering:**  
![SNR_HighPass](Plots/SNR_HighPass.png)  

---

## **Folder Structure**
GW150914_Denoising/
│
├── Scripts/ # Python code for each phase
│ ├── phase3_raw_plot.py
│ ├── phase4_zoom_chirp.py
│ ├── phase5_fft_filter.py
│ ├── phase6_matched_filter.py
│ └── phase6_5_highpass_validation.py
│
├── Plots/ # Generated images
│ ├── RawSignal.png
│ ├── MergerZoom.png
│ ├── BeforeAfter.png
│ ├── FilteredSpectrum.png
│ └── SNR_HighPass.png
│
├── Data/ # Original HDF5 dataset
│ └── H-H1_LOSC_4_V2-1126259446-32.hdf5
│
└── README.md # This file


---

## **Key Learnings**

- Handling real experimental data.  
- Applying FFT, filtering, and inverse FFT for denoising.  
- Visualizing raw, filtered, and SNR-enhanced signals.  
- Comparing signals quantitatively.  
- Structuring a reproducible scientific workflow.  

---

## **Conclusion**

The project demonstrates **denoising of a gravitational wave signal**:  

- Binary black hole merger is clearly visible in the denoised waveform.  
- Signal processing improves signal clarity and SNR.  
- The workflow is reproducible and fully documented with scripts, plots, and data.  

**Deliverables:**  
