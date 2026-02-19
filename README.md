# 🚗 Car Price Prediction System
# 📌 Overview

This project is an end-to-end machine learning system designed to predict the price of used cars based on various features such as brand, model, fuel type, transmission, kilometers driven, and age. The system performs data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit for real-time predictions.

# 🎯 Objective

The main goal of this project is to build a reliable regression model that can estimate the market price of used cars and demonstrate a complete machine learning pipeline from data processing to deployment.

# 🛠️ Technologies Used

Python

Pandas, NumPy

Scikit-learn

Matplotlib, Seaborn

Streamlit

Joblib

# 📂 Project Workflow
1. Data Preprocessing

Loaded dataset using Pandas

Handled missing values

Created new feature: car age from manufacturing year

Converted categorical variables using one-hot encoding

2. Exploratory Data Analysis (EDA)

Analyzed relationships between features and price

Visualized price distribution

Identified important features affecting car price

3. Model Training

Trained and compared multiple regression models:

Linear Regression

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

4. Model Evaluation

Evaluated models using:

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

R² Score

Random Forest achieved the best performance.

5. Feature Importance Analysis

Identified top features influencing price prediction

Improved model interpretability

6. Model Deployment

Saved trained model using Joblib

Built Streamlit web application for real-time predictions

# 📊 Model Performance
Model	Performance
Linear Regression- 	Moderate
Decision Tree	- Good
Random Forest	- Best
Gradient Boosting - 	Good

Random Forest was selected as the final model.

# 💻 How to Run the Project
Step 1: Clone the repository
---
git clone https://github.com/yourusername/car-price-prediction.git
cd car-price-prediction
---
Step 2: Install dependencies
---
pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib
---
Step 3: Run Streamlit app
---
streamlit run app.py
---

# 📁 Project Structure
--- 
car-price-prediction/
│
├── cars.csv
├── app.py
├── car_price_model.pkl
├── scaler.pkl
├── model_columns.pkl
├── notebook.ipynb
└── README.md
--- 

# 📈 Key Skills Demonstrated

Data preprocessing and feature engineering

Machine learning model training and evaluation

Regression analysis

Feature importance analysis

Model serialization and deployment

Streamlit web application development

🚀 Future Improvements

Deploy model on cloud (AWS / Render / Railway)

Improve accuracy using hyperparameter tuning

Add database integration

Build REST API using Flask or FastAPI
