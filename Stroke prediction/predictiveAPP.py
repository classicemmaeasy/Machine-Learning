# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:11:23 2024

@author: Emmanuel
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:31:51 2024

@author: Emmanuel
"""

import numpy as np 
import streamlit as st
import pickle


lomodel=pickle.load(open("C:/Users/HP/Desktop/gideon/stk-mod.sav", 'rb'))



input_data=[1,3,0,0,0,3,0.181818,0.727273,0,3,2,1.0,0.090909091,0.0,0,0,]
def stroke_model(input_data):
    data_to_array= np.asarray(input_data)
    
    data_reshaped= data_to_array.reshape(1,-1)
    
    prediction= lomodel.predict(data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        print('the person has a very low risk ischemic stroke')
    if (prediction[0] == 1):
        print('the person has a low risk ischemic stroke')
    if (prediction[0] == 2):
        print('the person has a high risk ischemic stroke')
    if (prediction[0] == 3):
        print('the person has a very high risk ischemic stroke')
         
stroke_model(input_data)

def main():
    #giving a title 
    st.title('Stroke Prediction Web App')
    
    #getting the input data  from the user
    Gender= st.text_input('Enter your gender')
    Age= st.text_input('Enter your age')
    Heart_disease= st.text_input('have ever have a heart disease')
    Ever_married=st.text_input('have you ever been married')
    Work_type=st.text_input('work type')
    Smoking_status=st.text_input('smoking status')
    Systolic=st.text_input('systolic value')
    Diastolic=st.text_input('diastolic value')
    Diabetics=st.text_input('diabetics Value')
    Family_history=st.text_input('Family history')
    Alchohol=st.text_input('alchohol')
    BMI=st.text_input('BMI Value')
    High_cholesterol=st.text_input('have you ever have a high cholesterol')
    
    #code for prediction
    diagnose=''
    
    #creating a button for prediction
    if st.button('Heart disease pred Test Result'):
        user_input=[Gender,Age,Heart_disease,Ever_married,Work_type ,Smoking_status,Systolic ,Diastolic ,Diabetics,Family_history,Alchohol,BMI,High_cholesterol]
        user_input=[float(x) for x in user_input]
        diagnose= stroke_model([user_input])
    
    
    st.success(diagnose)
    
if __name__=='__main__':
    main()

