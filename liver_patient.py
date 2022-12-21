import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('liver_patient.sav', 'rb'))

st.title('Prediksi Penyakit Liver (Prediction of Liver Diases)')

Age = st.number_input('Umur Pasien')

Total_Bilirubin = st.number_input('Jumlah Bilirubin')

Direct_Bilirubin = st.number_input('Bilirubin Yang Tidak Terkonjungsi')

Alkaline_Phosphotase = st.number_input('Jumlah Kadar ALP')

Alamine_Aminotransferase = st.number_input('Jumlah Enzim Dalam Darah')

Aspartate_Aminotransferase = st.number_input('Jumlah AST')

Total_Protiens = st.number_input('Jumlah Protein')

Albumin = st.number_input('Jumlah Protein Pada Darah')

Albumin_and_Globulin_Ratio = st.number_input('Rasio Albumin dan Globulin ')

liver_diagnosis =''

if st.button('Prediksi Pebyakit Liver'):
    liver_prediction = model.predict([[Age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
    
    if (liver_prediction[0]==1):
        liver_diagnosis = 'Pasien Tidak Terkena Penyakit Liver'
    else:
        liver_diagnosis = 'Pasien Terkena Penyakit Liver'
st.success(liver_diagnosis)
    
