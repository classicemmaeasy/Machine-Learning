# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:19:47 2024

@author: Emmanuel
"""

import numpy as np
import pickle
import streamlit as st


#loading the model
loaded_model=pickle.load(open('C:/Users/HP/Desktop/data/diabetics deployment/trained_model.sav', 'rb'))

#creating a function fro prediction

def diabetics_prediction(input_data):
    
    data_to_array= np.asarray(input_data)

    data_reshaped= data_to_array.reshape(1,-1)

    prediction= loaded_model.predict(data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return'the person is not diabetic'
    else:   
        return'the person is diabetic'
        
def main():
    #giving a title 
    st.title('Diabetics Prediction Web App')
    
    #getting the input data  from the user

    Pregnancies= st.text_input('Number of Pregnancies')
    Glucose= st.text_input('Glucose level')
    BloodPressure= st.text_input('Blood Pressure level')
    SkinThickness=st.text_input('Skin Thickness level')
    Insulin=st.text_input('Insulin level')
    BMI=st.text_input('BMI level')
    DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction Value')
    Age=st.text_input('Age Value')
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Diabetics Test Result'):
        diagnosis= diabetics_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
if __name__=='__main__':
    main()