"""
Universal Raman Spectrum Plotter

Author:
Ashen Deemantha Liyanage

Affiliation:
Zayak's Lab
Department of Physics and Astronomy
Bowling Green State University

Description:
Automatically finds and plots Raman spectra from .dat files.
"""

# -------------------------------
# Raman Spectrum Plotter
# Automatically finds all .dat files in the folder
# Uses filename as legend label
# Customizable colors + filled curves
# -------------------------------

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import glob
import os

# -------------------------------
# 1. Set font style and size
# -------------------------------
rcParams['font.family'] = 'Times New Roman'
rcParams['font.size'] = 14

# -------------------------------
# 2. Define custom colors
# -------------------------------
colors = ["blue", "red", "green", "orange", "purple"]

# -------------------------------
# 3. Find all .dat files
# -------------------------------
files = sorted(glob.glob("*.dat"))

if not files:
    print("⚠️ No .dat files found in this folder.")
    exit()

# -------------------------------
# 4. Create plot
# -------------------------------
plt.figure(figsize=(8,5))

for i, f in enumerate(files):
    data = np.loadtxt(f)
    raman_shift = data[:, 0]
    intensity = data[:, 1]

    # Label from filename
    label = os.path.splitext(f)[0]

    # Choose color
    color = colors[i % len(colors)]

    # Plot line
    plt.plot(raman_shift, intensity, lw=1.5, color=color, label=label)

    # Fill under curve (light color using transparency)
    plt.fill_between(raman_shift, intensity, color=color, alpha=0.2)

# -------------------------------
# 5. Labels
# -------------------------------
plt.xlabel("Raman Shift (cm$^{-1}$)")
plt.ylabel("Intensity (a.u.)")

# -------------------------------
# 6. Title and save name
# -------------------------------
dataset_names = [os.path.splitext(f)[0] for f in files]

if len(dataset_names) == 1:
    title_name = f"Raman spectrum of {dataset_names[0]}"
else:
    title_name = "Raman spectrum of " + " and ".join(dataset_names)

plt.title(title_name)
save_name = title_name + ".png"

# -------------------------------
# 7. Axis limits (edit if needed)
# -------------------------------
#plt.xlim(1050, 1600)
# plt.ylim(0, 30)

# -------------------------------
# 8. Final touches
# -------------------------------
#plt.grid(True)
plt.legend(loc="upper right")
plt.tight_layout()

# Save figure
plt.savefig(save_name, dpi=300)

# Show plot
plt.show()

print(f"✅ Plot saved as {save_name}")

