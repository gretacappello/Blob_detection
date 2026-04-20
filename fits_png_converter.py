import os
import glob
import re
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt

# ==================================================
# INPUT / OUTPUT PATHS
# ==================================================
fits_folder = "/content/drive/MyDrive/input_fits_files"
output_folder = "/content/drive/MyDrive/output_png_files"

os.makedirs(output_folder, exist_ok=True)

# ==================================================
# FIND FITS FILES
# ==================================================
file_list = sorted(glob.glob(os.path.join(fits_folder, "*.fits")))

print(f"Found {len(file_list)} FITS files")

total = 0

# ==================================================
# CONVERT FITS TO PNG
# ==================================================
for file_path in file_list:

    # Read FITS image
    img_data = fits.getdata(file_path)

    # Replace NaNs
    img_data = np.nan_to_num(img_data, nan=0.0)

    # Contrast stretch using percentiles
    vmin, vmax = np.percentile(img_data, (2, 97))

    if vmax <= vmin:
        vmin = float(np.min(img_data))
        vmax = float(np.max(img_data) + 1e-6)

    # Normalize to 0-255
    img_scaled = ((img_data - vmin) / (vmax - vmin) * 255)
    img_scaled = np.clip(img_scaled, 0, 255).astype(np.uint8)

    # Output filename
    base = os.path.basename(file_path)
    name = os.path.splitext(base)[0]

    out_png = os.path.join(output_folder, f"{name}.png")

    # Save PNG
    plt.imsave(out_png, img_scaled, cmap="gray", origin="lower")

    total += 1

    if total % 20 == 0:
        print(f"Processed {total} images...")

print(f"Done. Converted {total} FITS files to PNG.")
