# DNA-Data-Science: HELA Platinum Project

Investigation of Platinum-based drug efficiency interacting with EGFR protein (1M17).

## 🧬 Project Description
This project automates molecular docking data analysis. We compare the stability of the platinum ligand binding with the wild-type protein (HeLa) and the mutant form (Lung Cancer).

## 📊 Research Results
Based on manual measurements in PyMOL, the following data was obtained:
- **Cys794 (HeLa Standard):** 2.8 Å — optimal distance for stable binding.
- **L858R (Mutation):** 3.2 Å — critical increase in distance, reducing efficiency.

## 💻 Tech Stack
- **Python 3.11** (Pandas for data, Matplotlib for plotting)
- **PyMOL** (Visualization and measurements)
- **Git/GitHub** (Version control)

## 🚀 How to Run
1. Update data: `python3 scripts/reset_data.py`
2. Plot results: `python3 scripts/plot_results.py`
3. Generate report: `python3 scripts/generate_report.py`