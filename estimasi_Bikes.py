import pickle
import streamlit as st

model = pickle.load(open('estimasi_bikes.sav', 'rb'))

st.title('ESTIMASI HARGA SEPEDA')
kms_driven = st.number_input('Input Jarak Tempuh')
age = st.number_input('Input Umur Sepeda')
power = st.number_input('Input Kecepatan Sepeda')

predict = ' '

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[kms_driven, age, power]]
    )
    st.write ('Estimasi Harga Sepeda : ', predict)
    