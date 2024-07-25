import streamlit as st
import pandas as pd
import pickle

# Memuat model dari file model.pkl
with open('model7.pkl', 'rb') as file:
    model = pickle.load(file)

# Judul dan deskripsi aplikasi
st.title('Prediksi Penjualan Produk')
st.write('PBerdasarkan Data Penjualan Historis')

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
    st.write('Data yang di inputkan:')
    st.write(input_df)
    
    # Lakukan prediksi menggunakan model
    predicted_sales = model.predict(input_df)
    
    return predicted_sales[0]

# Form input untuk prediksi
with st.form(key='prediction_form'):
    gender = st.selectbox('Gender', options=['Male', 'Female'])
    age = st.number_input('Usia', min_value=0, max_value=100, step=5)
    product_category = st.selectbox('Kategori Produk', options=['Beauty', 'Clothing', 'Electronics'])
    month = st.number_input('Bulan', min_value=1, max_value=12, step=1)
    year = st.number_input('Tahun', min_value=2000, max_value=2100, step=1)
    submit_button = st.form_submit_button(label='Predict')

# Memproses prediksi ketika tombol submit ditekan
if submit_button:
    predicted_sales = predict_sales(gender, age, product_category, month, year)
    st.write(f'Prediksi Total Penjualan: {predicted_sales}')
