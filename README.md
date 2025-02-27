# Cancer Analysis Project

## Overview
This project focuses on analyzing cancer-related data using statistical and machine learning techniques. The goal is to identify patterns, perform predictive modeling, and visualize key insights that can help in understanding cancer characteristics.

## Objectives
- Perform **exploratory data analysis (EDA)** to uncover trends and patterns.
- Apply **statistical methods** and **machine learning models** to predict cancer outcomes.
- Visualize key findings using **ggplot2**, **grid.arrange()**, and other visualization tools.
  

## Dataset
- **Source:** [https://www.kaggle.com/datasets/erdemtaha/cancer-data]
- **Format:** CSV file with features such as:
  - ID: Represents a unique ID of each patient.
  - Diagnosis: Indicates the type of cancer. This property can take the values "M" (Malignant - Benign) or "B" (Benign - Malignant).
  - radius_mean
  - texture_mean
  - perimeter_mean
  - area_mean
  - smoothness_mean
  - compactness_mean
  - concavity_mean
  - concave points_mean: Represents the mean values of the cancer's visual characteristics.



Other features contain specific ranges of average values of the features of the cancer image:

  - radius_mean
  - texture_mean
  - perimeter_mean
  - area_mean
  - smoothness_mean
  - compactness_mean
  - concavity_mean
  - concave points_mean

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- **R** (version 4.4.2)
- **RStudio** (Optional but recommended)
- **Positron IDE** (To run the notebook)
- **Required R Packages:**
  ```r
install.packages(c("tidyverse", "skimr", "tidymodels", "corrplot", "GGally", "viridis", "patchwork", "scales",  
   "gridExtra", "ggridges", "vip", "ggbiplot", "factoextra", "finetune", "kernlab", "ranger", "xgboost", "janitor",  
   "Boruta", "PCAtest", "summarytools", "tictoc", "kableExtra", "ggpubr", "betacal"))

  ```

## Project Structure
```
CancerAnalysis/
│── datasets/          # Raw and processed datasets
│── scripts/           # R scripts for analysis & modeling
│── notebooks/         # Jupyter/R Markdown notebooks for EDA
│── results/           # Outputs (plots, models, reports)
│── README.md          # Project documentation
```

## Exploratory Data Analysis (EDA)
Performed EDA to understand data distribution and relationships:
- **Summary statistics** (`summary()`, `skimr::skim()`)
- **Feature distributions & correlations** (`ggpairs()`, `corrplot`, `GGally`)

## Modeling Approaches
### **Supervised Learning**
- **Logistic Regression**: Baseline classifier
- **Random Forest**: For feature importance analysis and classification
- **Support Vector Machines (SVM)**: For classification tasks
- **Xtreme Gradient Boosting**: For Classification tasks
- **Bart**
- **Naive Bayes**
- **K-Nearest Neighbors**
- **Decision Tree Classifier**

### **Unsupervised Learning**
- **Clustering** (K-Means, Hierarchical Clustering)
- **Dimensionality Reduction** Utilized the PCA algorithm to reduce the dimensions

## Visualization
- **ggplot2** for advanced visualizations.
- **gridExtra::grid.arrange()** to display multiple plots.

## Issues & Challenges
- `grid.arrange()` sometimes squishes plots, consider displaying them individually.
- Dataset imbalance affecting classification, handled with **SMOTE**.
- Missing data requiring imputation strategies.

## Future Work
- Deploy a **Shiny dashboard** for interactive exploration.
- Automate EDA and model training with **workflow automation tools**.

## Contribution
Contributions are welcome! Feel free to fork the repo, create a feature branch, and submit a pull request.

## License
[Apache 2.0]

## Contact
For any inquiries or collaborations, reach out to [Chris Olande] via email at [olandechris@gmail.com].

