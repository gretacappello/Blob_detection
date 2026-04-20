# Blob Detection in WISPR Images

Detection of blobs in WISPR images using a deep-learning algorithm.

This repository provides tools to evaluate density-enhancement blobs in images from the **Wide-field Imager for Solar Probe (WISPR)** onboard **Parker Solar Probe (PSP)**.

---

## Overview

The provided trained model (`best.pt`) has been developed to detect blobs in static WISPR images and achieves an accuracy of **89%**.

A scientific publication describing the method is currently in preparation.

---

## Getting Started

### 1. Convert FITS Files to PNG

Before running the detection model, convert your `.fits` files into `.png` format using the provided conversion script (fits_png_converter.py).

This step is required to ensure compatibility with the deep-learning pipeline.

### 2. Prepare Your Dataset

Save all converted `.png` files into a folder of your choice.

Example:

```bash
dataset/images/test/
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

* evaluated images with bounding boxes
* confusion matrix
* precision / recall / mAP scores
* detection summaries

---

## Model Performance

| Metric   | Value |
| -------- | ----- |
| Accuracy | 89%   |

---

## Applications

This model has been applied statistically to **Parker Solar Probe / WISPR Encounters 1–25**.

Additional scientific results will be published soon.

---

## Repository Structure

```bash
Blob_detection/
│── evaluate_MLblobs.py
│── best.pt
│── convert_fits_to_png.py
│── dataset/
│   └── images/
│── outputs/
```

---

## Requirements

Install dependencies:

```bash
pip install ultralytics opencv-python matplotlib numpy astropy
```

---

## Citation

If you use this repository in your research, please cite the upcoming publication (to be announced).

---

## Contact

**Greta Cappello**
University of Graz
📧 [greta.cappello@uni-graz.at](mailto:greta.cappello@uni-graz.at)
