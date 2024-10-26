import pickle
import numpy as np
import streamlit as st
import os

# Load model yang telah disimpan
model_path = 'penyakit_jantung.sav'  # Gantilah dengan path absolut yang sesuai
model = pickle.load(open(model_path, 'rb'))

# Judul web
st.title('Prediksi Penyakit Jantung')

# Membuat kolom untuk input data
col1, col2, col3 = st.columns(3)

with col1:
    age = st.text_input('Umur', '0')

with col2:
    sex = st.selectbox('Jenis Kelamin', ('0', '1'))  # 0 untuk Female, 1 untuk Male

with col3:
    cp = st.selectbox('Jenis Nyeri Dada', ('0', '1', '2', '3'))

with col1:
    trestbps = st.text_input('Tekanan Darah', '0')

with col2:
    chol = st.text_input('Nilai Kolesterol', '0')

with col3:
    fbs = st.selectbox('Gula Darah > 120 mg/dl', ('0', '1'))  # 1 jika True, 0 jika False

with col1:
    restecg = st.selectbox('Hasil Elektrokardiografi', ('0', '1', '2'))

with col2:
    thalach = st.text_input('Detak Jantung Maksimum', '0')

with col3:
    exang = st.selectbox('Induksi Angina', ('0', '1'))  # 1 jika True, 0 jika False

with col1:
    oldpeak = st.text_input('ST Depression', '0')

with col2:
    slope = st.selectbox('Slope', ('0', '1', '2'))

with col3:
    ca = st.selectbox('Nilai CA', ('0', '1', '2', '3', '4'))

with col1:
    thal = st.selectbox('Nilai Thal', ('0', '1', '2', '3'))

# Variabel untuk menampilkan hasil prediksi
heart_diagnosis = ''

# Tombol untuk melakukan prediksi
if st.button('Prediksi Penyakit Jantung'):
    try:
        # Mengonversi input ke tipe float
        input_data = [
            float(age), float(sex), float(cp), float(trestbps), float(chol), 
            float(fbs), float(restecg), float(thalach), float(exang), 
            float(oldpeak), float(slope), float(ca), float(thal)
        ]

        # Melakukan prediksi
        heart_prediction = model.predict([input_data])

        # Menentukan hasil prediksi
        if heart_prediction[0] == 0:
            heart_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'
        else:
            heart_diagnosis = 'Pasien Terkena Penyakit Jantung'

        # Menampilkan hasil
        st.success(heart_diagnosis)

    except ValueError:
        st.error("Masukkan semua nilai dengan benar dalam format numerik.")

