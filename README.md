# Detection of blobs in WISPR images using a deep-learning algorithm

This repository provides tools to evaluate density-enhancement blobs in images from the **Wide-field Imager for Solar Probe (WISPR)** onboard **Parker Solar Probe (PSP)**.

---

## Overview

The provided trained model (`best.pt`) has been trained to detect blobs in static WISPR images. 
In this repository, we provide the trained model for detection only.
A scientific publication describing the method is currently under revision in ApJ.

------

## Requirements

Install dependencies:

```bash
pip install ultralytics opencv-python matplotlib numpy astropy
```
------

## Getting Started

### 0. Dowload the right fits files

The model has been trained on LW data from WISPR, so we highly suggest to use it on the fits file that can be dowloaded here: https://wispr.nrl.navy.mil/data/rel/fits/LW

### 1. Convert FITS Files to PNG

Before running the detection model, convert your `.fits` files into `.png` format using the provided conversion script (fits_png_converter.py).

This step is required to ensure compatibility with the deep-learning pipeline.

### 2. Prepare Your Dataset

Save all converted `.png` files into a folder of your choice.

Example:

```bash
dataset/images/evaluation_dataset/
```

### 3. Configure the Evaluation Script

Open:

```bash
evaluate_MLblobs.py
```

and modify:

* the path to your input images folder
* the path to the trained model weights (`best.pt`)
* the desired output directory

### 4. Run the Detection

```bash
python evaluate_MLblobs.py
```

### 5. Outputs

The script automatically saves:

* ALL evaluated images with bounding boxes
* detection summaries

---

## Applications

This model has been applied statistically to **Parker Solar Probe / WISPR Encounters 1–25**.

See paper in ApJ: ...

---

## Citation

If you use this repository in your research, please cite the upcoming publication (to be announced).

---

## Contact

**Greta Cappello**
NASA GSFC
📧 [greta.cappello@nasa.gov](mailto:greta.cappello@nasa.gov)
