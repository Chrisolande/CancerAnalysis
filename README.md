<div align="center">

# 🔬 Cancer Analysis Project

[![R version](https://img.shields.io/badge/R-v4.4.2-blue.svg)](https://www.r-project.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-orange.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-20BEFF.svg)](https://www.kaggle.com/datasets/erdemtaha/cancer-data)

*An advanced analytical approach to cancer data classification and visualization*

</div>

---

## 📋 Overview

This project leverages statistical and machine learning techniques to analyze cancer-related data. By identifying patterns, performing predictive modeling, and visualizing key insights, we aim to enhance understanding of cancer characteristics and support clinical decision-making.

## 🎯 Objectives

- 📊 Perform **exploratory data analysis (EDA)** to uncover trends and patterns
- 🧮 Apply **statistical methods** and **machine learning models** to predict cancer outcomes
- 📈 Visualize key findings using **ggplot2**, **grid.arrange()**, and other visualization tools

## 💾 Dataset

<table>
  <tr>
    <td><b>Source:</b></td>
    <td><a href="https://www.kaggle.com/datasets/erdemtaha/cancer-data">Cancer Data on Kaggle</a></td>
  </tr>
  <tr>
    <td><b>Format:</b></td>
    <td>CSV file</td>
  </tr>
</table>

### Key Features:

- **ID**: Unique identifier for each patient
- **Diagnosis**: Cancer type indicator ("M" for Malignant, "B" for Benign)
- **Feature means**: Measurements including radius, texture, perimeter, area, smoothness, compactness, concavity, and concave points
- **Feature ranges**: Additional metrics capturing specific ranges of average values from cancer images

## 🛠️ Installation & Setup

### Prerequisites

- **R** (version 4.4.2)
- **RStudio** (Optional but recommended)
- **Positron IDE** (To run the notebook)

### Required R Packages

```r
install.packages(c(
  # Data manipulation and visualization
  "tidyverse", "skimr", "corrplot", "GGally", "viridis", "patchwork",
  "scales", "gridExtra", "ggridges", "ggpubr", "ggbiplot",
  
  # Modeling and machine learning
  "tidymodels", "vip", "factoextra", "finetune", "kernlab", 
  "ranger", "xgboost", "Boruta", "PCAtest", "betacal",
  
  # Utilities
  "janitor", "summarytools", "tictoc", "kableExtra"
))
```

## 📁 Project Structure

```
CancerAnalysis/
│
├── 📂 datasets/          # Raw and processed datasets
├── 📂 scripts/           # R scripts for analysis & modeling
├── 📂 notebooks/         # Jupyter/R Markdown notebooks for EDA
├── 📂 results/           # Outputs (plots, models, reports)
└── 📄 README.md          # Project documentation
```

## 🔍 Exploratory Data Analysis (EDA)

We performed comprehensive EDA to understand data distribution and relationships:

- **Summary statistics** (`summary()`, `skimr::skim()`)
- **Feature distributions & correlations** (`ggpairs()`, `corrplot`, `GGally`)

## 🤖 Modeling Approaches

### Supervised Learning

| Model | Purpose |
|-------|---------|
| **Logistic Regression** | Baseline classifier |
| **Random Forest** | Feature importance & classification |
| **Support Vector Machines** | Classification with non-linear boundaries |
| **XGBoost** | Gradient boosting classification |
| **BART** | Bayesian Additive Regression Trees |
| **Naive Bayes** | Probabilistic classifier |
| **K-Nearest Neighbors** | Instance-based learning |
| **Decision Tree** | Interpretable classifier |

### Unsupervised Learning

- **Clustering** (K-Means, Hierarchical Clustering)
- **Dimensionality Reduction** (PCA) for feature space visualization

## 📊 Visualization

- **ggplot2** for advanced visualizations
- **gridExtra::grid.arrange()** to display multiple plots

![Sample Visualization](https://github.com/Chrisolande/CancerAnalysis/blob/main/results/confusion_matrix.png)
![Sample Visualization](https://github.com/Chrisolande/CancerAnalysis/blob/main/results/model_race_results.png)
![Sample Visualization](https://github.com/Chrisolande/CancerAnalysis/blob/main/results/Metric%20Distributions.png)

## ⚠️ Issues & Challenges

- `grid.arrange()` sometimes squishes plots, consider displaying them individually
- Dataset imbalance affecting classification, handled with **SMOTE**
- Missing data requiring imputation strategies

## 🔮 Future Work

- Deploy a **Shiny dashboard** for interactive exploration
- Automate EDA and model training with **workflow automation tools**
- Incorporate additional datasets for validation
- Explore deep learning approaches for image analysis

## 🤝 Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## 📬 Contact

<div align="center">
  
  <b>Chris Olande</b>
  
  [![Email](https://img.shields.io/badge/Email-olandechris%40gmail.com-red.svg)](mailto:olandechris@gmail.com)
  
</div>

---

<div align="center">
  <sub>Built with ❤️ by the Chris Olande</sub>
</div>