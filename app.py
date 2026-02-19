import streamlit as st
import pandas as pd
import numpy as np
import joblib
from datetime import datetime

# Load saved files
model = joblib.load(open('car_price_model.pkl', 'rb'))
scaler = joblib.load(open('scaler.pkl', 'rb'))
model_columns = joblib.load(open('model_columns.pkl', 'rb'))

st.title("🚗 Used Car Price Valuation System")

st.write("Enter car details to predict its fair market price")

# ---- User Inputs ----
brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Honda", "Toyota", "Ford"])
model_selected = st.selectbox("Make", list(['Corolla', 'Civic', 'Mustang', 'Swift', 'Sonata', 'Nexon',
       'Scorpio', 'Polo', 'A4', 'X1', 'C-Class', 'Endeavour', 'Creta',
       'Harrier', 'Ertiga', 'City', 'Tiguan', 'Q3', '5 Series', 'GLC',
       'Innova', 'Figo', 'Verna', 'Altroz', 'Thar', 'Passat', 'A6', 'X3',
       'E-Class', 'Fortuner', 'Aspire', 'Elantra', 'Safari', 'Vitara',
       'WR-V', 'Ameo', 'A3', '7 Series', 'GLE', 'Yaris', 'Ranger',
       'Santro', 'Tigor', 'S-Cross', 'BR-V', 'T-Roc', 'Q7', 'X5', 'GLA',
       'Camry', 'Venue', 'Tiago', 'XUV300', 'Vento', 'A5', '3 Series',
       'Innova Crysta', 'EcoSport'], ))
fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.selectbox("Owner Type", ["First", "Second", "Third"])

year = st.number_input("Manufacturing Year", 2000, datetime.now().year, 2018)
km_driven = st.number_input("Kilometers Driven", 0, 300000, 50000)
mileage = st.number_input("Mileage (km/l)", 5, 40, 18)
engine = st.number_input("Engine (CC)", 800, 5000, 1200)
power = st.number_input("Power (BHP)", 30, 400, 80)
seats = st.number_input("Seats", 2, 10, 5)

# ---- Convert Inputs to Model Format ----
if st.button("Predict Price"):
    car_age = datetime.now().year - year

    input_dict = {
        'Kilometers_Driven': km_driven,
        'Mileage': mileage,
        'Engine': engine,
        'Power': power,
        'Seats': seats,
        'Car_Age': car_age
    }

    # Convert categorical into one-hot columns
    for col in model_columns:
        if col.startswith("Brand_"):
            input_dict[col] = 1 if col == f"Brand_{brand}" else 0
        elif col.startswith("Model_"):
            input_dict[col] = 1 if col == f"Model_{model_selected}" else 0

        elif col.startswith("Fuel_Type_"):
            input_dict[col] = 1 if col == f"Fuel_Type_{fuel}" else 0
        elif col.startswith("Transmission_"):
            input_dict[col] = 1 if col == f"Transmission_{transmission}" else 0
        elif col.startswith("Owner_Type_"):
            input_dict[col] = 1 if col == f"Owner_Type_{owner}" else 0

    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=model_columns, fill_value=0)

    # Scale (safe even if model doesn’t need it)
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)[0]

    st.success(f"💰 Estimated Car Price: ₹ {prediction:,.0f}")