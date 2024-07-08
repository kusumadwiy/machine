import streamlit as st
import pandas as pd
import pickle

# Memuat model dari file model.pkl
with open('model2.pkl', 'rb') as file:
    model = pickle.load(file)

# Judul dan deskripsi aplikasi
st.title('Sales Prediction App')
st.write('Prediksi total penjualan berdasarkan gender, usia, kategori produk, bulan, dan tahun.')

# Input form untuk prediksi
st.sidebar.header('Masukkan Data untuk Prediksi')
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])
age = st.sidebar.slider('Usia', 18, 100, 30)
product_category = st.sidebar.selectbox('Kategori Produk', ['Beauty', 'Clothing', 'Electronics'])
month = st.sidebar.slider('Bulan', 1, 12, 1)
year = st.sidebar.slider('Tahun', 2000, 2030, 2023)

# Fungsi untuk melakukan prediksi total penjualan
def predict_sales(gender, age, product_category, month, year):
    # Transformasi input menjadi nilai numerik yang sesuai
    gender_num = 2 if gender.lower() == 'female' else 1
    product_category_num = 1 if product_category.lower() == 'beauty' else 2 if product_category.lower() == 'clothing' else 3
    
    # Buat data input untuk prediksi
    input_data = {
        'Gender': [gender_num],
        'Age': [age],
        'Product Category': [product_category_num],
        'Month': [month],
        'Year': [year]
    }
    
    # Buat DataFrame dari data input
    input_df = pd.DataFrame(input_data)
    
    # Debugging: cetak DataFrame input
    st.write('DataFrame Input untuk Prediksi:')
    st.write(input_df)
    
    # Lakukan prediksi menggunakan model
    predicted_sales = model.predict(input_df)
    
    return predicted_sales[0]

# Tombol untuk melakukan prediksi
if st.sidebar.button('Prediksi'):
    predicted_sales = predict_sales(gender, age, product_category, month, year)
    st.write(f'Prediksi Total Penjualan: {predicted_sales}')
