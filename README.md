# Raman Spectrum Plotter (with Peak Analysis)

A simple Python tool to visualize Raman spectra from `.dat` files and automatically detect peaks.

This tool is designed for **research use in computational chemistry and physics**, especially for:

* DFT vibrational analysis (e.g., SIESTA)
* Raman spectrum comparison
* Molecule–surface interaction studies

---

# 👤 Author

**Ashen Deemantha Liyanage**
Zayak’s Lab
Department of Physics and Astronomy
Bowling Green State University (BGSU)

---

# 📊 What this tool does (simple explanation)

If you have Raman data files like:

```
100  0.12
120  0.18
140  0.30
```

This program will:

✔ Plot all spectra automatically
✔ Compare multiple datasets
✔ Detect Raman peaks automatically
✔ Save a publication-quality figure
✔ Export peak positions into a CSV file

---

# 💻 How to Install (VERY IMPORTANT)

## Step 1 — Install Python

Make sure you have Python installed:

👉 https://www.python.org/downloads/

Check by typing in terminal:

```bash id="pycheck"
python --version
```

or

```bash id="pycheck2"
python3 --version
```

---

## Step 2 — Install required libraries

Open terminal (Mac/Linux) or Command Prompt (Windows) and run:

```bash id="install1"
pip install numpy matplotlib scipy
```

If this does not work, try:

```bash id="install2"
pip3 install numpy matplotlib scipy
```

---

# 📁 How to Use

## Step 1 — Prepare your data

Put all `.dat` files in the SAME folder as the script.

Example:

```
raman_plotter.py
sample1.dat
sample2.dat
```

---

## Step 2 — Run the program

In terminal, go to the folder:

```bash id="run1"
cd path/to/your/folder
```

Then run:

```bash id="run2"
python raman_plotter.py
```

or

```bash id="run3"
python3 raman_plotter.py
```

---

# 📤 Output files

After running, you will get:

### 1. Raman plot image

```
raman_analysis.png
```

### 2. Peak data file

```
raman_peaks.csv
```

This CSV file can be opened in:

* Excel
* Origin
* Python
* MATLAB

---

# 📂 Example data

Check the `examples/` folder for sample files.

---

# ⚙️ Requirements

This program uses:

* numpy → numerical calculations
* matplotlib → plotting graphs
* scipy → peak detection

---

# 🔬 Scientific use cases

This tool is useful for:

* Raman spectroscopy analysis
* DFT vibrational mode assignment
* Surface adsorption studies
* Molecular comparison studies
* Photochemical systems (CuPc, BaTiO₃, etc.)

---

# ⚠️ Troubleshooting

### Problem: "command not found: python"

Use:

```bash
python3
```

---

### Problem: pip not working

Try:

```bash
python -m pip install numpy matplotlib scipy
```

---

# 📜 Citation

If you use this tool in research, please cite:

> Ashen Deemantha Liyanage
> Raman Spectrum Plotter (2026)
> GitHub: https://github.com/ashendeema/raman-spectrum-plotter

---

# 📄 License

MIT License — free to use, modify, and distribute.

