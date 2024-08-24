Rain Prediction Project 🌧️

This project aims to predict daily rainfall using historical weather data from the Hong Kong Observatory, spanning from 1992 to 2024. The aim is to find a model which can predict if and how much it will rain based on other conditions. Multiple machine learning models were developed and evaluated, focusing on rain prediction.The methodology is as follows:

DATASET:
The dataset is from the Hong Kong Observatory, spanning from 1992 to 2024, with data including: mean temperautre, relative humdiity, date, total sunlight and mean amount of cloud and total rainfall. Simple data cleaning and pre-processing was conducted, including normalizing features in relative humidity and mean amount of cloud; as well as turning total rainfall into a categorical attribute to aid in model development. It must be noted that the dataset is highly skewed in total rainfall, namely most of the data sets had total rainfall at 0. 

MODELS:
 Decision Trees, Random Forests, kNN and XGBoost models were used to find each model's efficiency towards predicting rain. The key metric here is the F1 score rather than accuracy score as the dataset is highly skewed. GridSearchCV was used to tune each model and the F1 score for the best set of parameters in each model is compared to see which one is best.

FINDINGS:

Efficiency for each model is ranked below:

Random Forest > XGBoost > Decision Tree > kNN

All models posted a mediocre F1 score, which suggests insufficient tuning and feature extraction.

One interesting thing during the training process is that while some models perform much better with tuning(e.g. Decision Trees), others such as XGBoost actually performed worse upon tuning hyperparameters. This may be due to poor hyperparameter tuning.

Relative humidity was the most important feature during training, but all models posted mediocre F1 scores of between 70-73%, which is not bad but could be a lot better.



