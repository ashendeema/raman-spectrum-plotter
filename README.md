# 📘 Raman Spectrum Plotter

The Raman Spectrum Plotter is a lightweight Python tool designed to automatically visualize Raman spectroscopy data stored in .dat files. It is developed for use in computational chemistry and physics workflows, particularly for analyzing vibrational spectra obtained from electronic structure calculations such as SIESTA or other DFT-based methods.

This tool removes the need for manual plotting and provides a fast, reproducible way to generate publication-quality Raman spectra comparisons.

# 👤 Author

Ashen Deemantha Liyanage
Zayak’s Lab
Department of Physics and Astronomy
Bowling Green State University (BGSU)

# 🔬 Purpose of the Tool

In Raman spectroscopy analysis, especially in computational studies, researchers often generate multiple .dat files representing different systems, geometries, or adsorption configurations. Manually plotting these datasets can be repetitive and error-prone.

This tool is designed to:

Automatically detect all Raman .dat files in a directory
Read and process spectral data without manual input
Plot multiple spectra on a single figure for direct comparison
Maintain consistent scientific visualization standards
Generate high-resolution figures suitable for publications

# 📁 Input Data Format

The program expects each .dat file to contain two numerical columns without headers:

Raman Shift (cm⁻¹)    Intensity (a.u.)
100.0                 0.12
101.0                 0.18
102.0                 0.10
Column 1 → Raman shift (cm⁻¹)
Column 2 → Intensity (arbitrary units)

Each file represents a separate Raman spectrum and will be plotted as an individual dataset.

# 💻 Installation Requirements

This script requires Python and a small set of scientific libraries.

Step 1: Install Python

Download and install Python from:

https://www.python.org/downloads/

Verify installation:

python --version

or

python3 --version
Step 2: Install required libraries

Install dependencies using pip:

pip install numpy matplotlib

If needed:

pip3 install numpy matplotlib

# 🚀 How to Use
Step 1: Prepare your working directory

Place the following in the same folder:

raman_plotter.py
One or more .dat Raman spectrum files

Example structure:

project_folder/
│
├── raman_plotter.py
├── spectrum_A.dat
├── spectrum_B.dat
├── spectrum_C.dat
Step 2: Run the script

Open a terminal in the project folder and execute:

python raman_plotter.py

or

python3 raman_plotter.py

# 📊 Output

After execution, the program will automatically generate:

1. Raman spectrum plot
Multiple spectra displayed in a single figure
Each dataset labeled using its filename
Filled curves for improved visual clarity
Consistent color scheme for easy comparison
2. High-resolution image file

The plot is saved automatically as a .png file with a descriptive name based on the datasets used.

# ⚙️ Key Features
Fully automatic file detection (*.dat)
Multi-spectrum comparison in a single plot
Publication-quality visualization using Matplotlib
Consistent scientific styling (Times New Roman font)
Automatic figure saving in high resolution (300 DPI)
No manual configuration required for standard use

# 🔬 Scientific Applications

This tool is particularly useful in:

Raman spectroscopy analysis of molecular systems
DFT-based vibrational mode comparisons
Surface adsorption studies (e.g., molecule–substrate interactions)
Photophysical and photochemical research
Computational materials science workflows

It is especially suitable for comparing spectral changes between different structural configurations or environments.

# ⚠️ Notes and Best Practices
Ensure .dat files contain only numeric data (no headers)
Keep all input files in the same directory as the script
Avoid missing or irregular columns in data files
Recommended for use with clean, pre-processed spectral outputs

# 📜 Citation

If you use this software in published research, please cite:

Ashen Deemantha Liyanage
Raman Spectrum Plotter (2026)
Zayak’s Lab, Bowling Green State University
GitHub Repository: https://github.com/ashendeema/raman-spectrum-plotter

# 📄 License

This project is released under the MIT License, allowing free use, modification, and distribution for academic and research purposes.

# 🌟 Summary

The Raman Spectrum Plotter provides a fast, reproducible, and publication-ready workflow for visualizing Raman spectral data. It is designed to reduce manual effort and improve consistency in computational spectroscopy analysis.
