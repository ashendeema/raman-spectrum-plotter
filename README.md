# Raman Spectrum Plotter

A Python tool for plotting Raman spectra from `.dat` files.

## Author

Ashen Deemantha Liyanage

Zayak's Lab
Department of Physics and Astronomy
Bowling Green State University (BGSU)

## Description

This script automatically:

* Detects all `.dat` files in the current directory
* Uses filenames as legend labels
* Plots multiple Raman spectra on the same figure
* Applies customizable colors
* Fills the area under each spectrum
* Saves a high-resolution PNG image automatically

## Requirements

```bash
pip install -r requirements.txt
```

## Input Format

Each `.dat` file should contain two columns:

```text
RamanShift    Intensity
100.0         0.12
101.0         0.15
102.0         0.11
...
```

## Usage

Place the script inside a folder containing Raman spectra:

```bash
python raman_plotter.py
```

The script will automatically detect all `.dat` files and generate:

```text
Raman spectrum of filename.png
```

## Features

* Automatic file discovery
* Multiple spectra comparison
* Publication-quality figures
* Times New Roman formatting
* Customizable color scheme
* Automatic figure saving

## Example

```text
sample1.dat
sample2.dat
sample3.dat
```

produces a single comparison plot with legends automatically generated from the filenames.

## Citation

If you use this software in your research, please cite:

Ashen Deemantha Liyanage, Raman Spectrum Plotter, GitHub Repository.

=======
# raman-spectrum-plotter
Automatic Raman spectrum plotting tool for computational spectroscopy.

