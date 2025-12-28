import streamlit as st
import joblib
import numpy as np

# Load model & encoder
model = joblib.load('model.pkl')
district_mean_price = joblib.load('district_mean_price.pkl')

st.title("🏠 Prediksi Harga Rumah Tangerang")

st.sidebar.header("Input Properti")

# ========================
# INPUT USER
# ========================

district = st.sidebar.selectbox(
    "District", 
    district_mean_price.index
)

facilities = st.sidebar.number_input(
    "Jumlah Fasilitas", 0, 20, 5
)

bedrooms = st.sidebar.number_input(
    "Bedrooms", 0, 10, 3
)

bathrooms = st.sidebar.number_input(
    "Bathrooms", 0, 10, 2
)

land_size = st.sidebar.number_input(
    "Land Size (m²)", 30, 1000, 120
)

building_size = st.sidebar.number_input(
    "Building Size (m²)", 30, 1000, 90
)

carports = st.sidebar.number_input(
    "Carports", 0, 5, 1
)

electricity = st.sidebar.number_input(
    "Electricity (VA)", 900, 10000, 2200
)

maid_bedrooms = st.sidebar.number_input(
    "Maid Bedrooms", 0, 3, 0
)

maid_bathrooms = st.sidebar.number_input(
    "Maid Bathrooms", 0, 3, 0
)

floors = st.sidebar.number_input(
    "Floors", 1, 5, 1
)

property_condition = st.sidebar.selectbox(
    "Condition",
    options=[0, 1, 2, 3, 4],
    format_func=lambda x: [
        "Butuh Renovasi",
        "Bagus",
        "Bagus Sekali",
        "Sudah Renovasi",
        "Baru"
    ][x]
)

garages = st.sidebar.number_input(
    "Garages", 0, 5, 0
)

furnishing = st.sidebar.selectbox(
    "Furnishing",
    options=[0, 1, 2],
    format_func=lambda x: [
        "Unfurnished",
        "Semi Furnished",
        "Furnished"
    ][x]
)

district_encoded = district_mean_price[district]

# ========================
# URUTAN INPUT SESUAI MODEL
# ========================

input_data = np.array([[
    facilities,          # 0
    bedrooms,            # 1
    bathrooms,           # 2
    land_size,           # 3
    building_size,       # 4
    carports,            # 5
    electricity,         # 6
    maid_bedrooms,       # 7
    maid_bathrooms,      # 8
    floors,              # 9
    property_condition,  # 10
    garages,             # 11
    furnishing,          # 12
    district_encoded     # 13
]])

# ========================
# PREDIKSI
# ========================

if st.button("Prediksi Harga"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Perkiraan Harga Rumah: Rp {prediction:,.0f}")
