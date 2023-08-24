# Churn Prediction

This repository contains a churn prediction that focuses on predicting customer churn using a machine learning approach. This involves data preprocessing, feature engineering, model building, optimization, and deployment using Flask.

## Overview

The goal of this project is to predict customer churn using a dataset named 'customer_churn_large_dataset.xlsx'. The project follows these main steps:

1. **Data Preprocessing**: The dataset is loaded and undergoes preprocessing to handle missing values and transform categorical features into numerical ones.

2. **Feature Engineering**: New features are created to capture important aspects of customer behavior, such as data usage patterns, subscription value, and more.

3. **Model Building**: Different machine learning models, including a neural network, Logistic Regression, Random Forest, and XGBoost classifiers, are trained and evaluated to predict customer churn.

4. **Model Optimization**: Hyperparameter tuning is performed on the Logistic Regression model using GridSearchCV to enhance its performance.

5. **Model Deployment**: A Flask web application is developed to deploy the churn prediction model, allowing users to interactively predict churn based on their inputs.

## Files and Folders

- `customer_churn_large_dataset.xlsx`: Contains the original dataset.
- `Churn_Prediction.ipynb`: Jupyter notebooks showcasing the project's step-by-step approach.
- `churn.h5`: Pre-trained neural network model in HDF5 format.
- `app.py`: Flask web application for model deployment.
- `templates/`: HTML templates for rendering user interface.
- `requirements.txt`: List of required packages for reproducing the environment.

## How to Use

1. Install the required packages using `pip install -r requirements.txt`.
2. Run the Flask app using `python app.py`.
3. Access the app in your web browser by going to `http://localhost:5001`.

## Acknowledgments

This project demonstrates the end-to-end process of churn prediction, from data preprocessing to deployment. It utilizes various machine learning techniques and showcases how to create a user-friendly web interface using Flask.

Feel free to explore the provided notebooks and adapt the code to your specific use case.
