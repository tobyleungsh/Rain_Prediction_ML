Rain Prediction Project 🌧️

This project aims to predict daily rainfall using historical weather data from the Hong Kong Observatory, spanning from 1992 to 2024. Multiple machine learning models were developed and evaluated, focusing on predicting whether it will rain on a given day.

Project Overview

	•	Data Source: Daily weather data from the Hong Kong Observatory (1992 - 2024).
	•	Models Developed:
	•	Decision Tree
	•	Random Forest
	•	k-Nearest Neighbors (kNN)
	•	XGBoost
	•	Evaluation Metric: Models were evaluated using the F1 score.

Key Findings

	•	Best Performing Model: The Random Forest model performed the best, but all models exhibited mediocre F1 scores.
	•	Challenges:
	•	Imbalanced Dataset: The dataset imbalance likely contributed to the mediocre performance of all models.
	•	Feature Engineering: Insufficient feature extraction limited the models’ predictive power.
	•	Hyperparameter Tuning: XGBoost underperformed, which may be due to suboptimal hyperparameter tuning using GridSearchCV instead of more advanced techniques like Bayesian Optimization.
	•	Feature Importance: Relative humidity was identified as the most significant feature in the Random Forest model, although its impact was minimal due to limited feature extraction.

Conclusion

While the Random Forest model outperformed other models, the results indicate that further improvements are needed, particularly in handling dataset imbalance and improving feature engineering.
