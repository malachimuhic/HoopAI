
<p align="center">
  <img src="https://github.com/user-attachments/assets/3ff5369a-ad47-4cab-9391-d314a5020a6a" alt="image" width="300"/>
</p>

# HoopAI

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1lPP1bG8vJhbFGHK5jLk6nwOFgfX5hIgT?usp=sharing)

https://github.com/malachimuhic/HoopAI

HoopsAI is a machine learning project designed to predict NBA game outcomes based on historical team performance data.
Using rolling statistics and feature engineering, HoopsAI builds models to forecast both point differentials and win/loss results for NBA matchups.

# Installation
To run this project, install the required Python packages:

```pip install nba_api pandas numpy scikit-learn xgboost matplotlib seaborn shap tqdm```

# Project Overview

The main steps in this project are:

1. Data Collection:
Download NBA regular season game logs from 2000–2025 using the NBA API.

2. Feature Engineering:
Compute 5-game and 10-game rolling averages for key team statistics (e.g., rebounds, assists, turnovers).

3. Feature Construction:
Create matchup-level feature differences between teams without leaking future game outcomes.

4. Regression Modeling:
Predict the point differential between two teams using models like Ridge, Random Forest, and XGBoost.

5. Classification Modeling:
Predict the win/loss outcome using Logistic Regression, Random Forest Classifier, and XGBoost Classifier.

6. Model Evaluation & Tuning:
Use metrics like MAE, RMSE, R², accuracy, F1, and ROC AUC, along with Grid Search for hyperparameter optimization.

# Example Results
1. Regression (Point Differential Prediction):
    * Evaluated using MAE, RMSE, R²

2. Classification (Win/Loss Prediction):
    * Evaluated using Accuracy, F1 Score, ROC AUC

3. Baseline vs Model Comparison:
    * Models consistently outperform dummy baselines

# Future Directions
* Add player-level modeling (injury reports, roster depth)

* Incorporate betting line data for enhanced predictions

* Develop a live prediction web app

* Explore deep learning models or graph neural networks (GNNs)
