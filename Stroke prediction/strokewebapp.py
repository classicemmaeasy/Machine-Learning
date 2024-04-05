# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:31:51 2024

@author: Emmanuel
"""

import numpy as np 
import streamlit as st
import pickle


lomodel=pickle.load(open("C:/Users/HP\Desktop/data/Stroke prediction/stroke-model.sav", 'rb'))
#std_model=pickle.load(open("C:/Users/HP\Desktop/data/Stroke prediction/stdfile.sav", 'rb'))


#input_data=[0,60.0,0,0,0,3,0,100.54,30.1,0]
def stroke_model(input_data):
 
    data_to_array= np.asarray(input_data)
    
    data_reshaped= data_to_array.reshape(1,-1)
    
  #  std_data=std_model.transform(data_reshaped)
    
    prediction=lomodel.predict(data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        print('the person is not a strokes patient')
    else:
         print('the person is a stroke patient')
         
#stroke_model(input_data)


def main():
    #giving a title 
    st.title('Stroke Prediction Web App')
    
    #getting the input data  from the user

    gender= st.text_input('Enter your gender')
    age= st.text_input('Enter your age')
    hypertension= st.text_input('Hypertension level')
    heart_disease=st.text_input('Heart Disease Yes=1 & NO=0')
    ever_married=st.text_input('Ever Married')
    work_type=st.text_input('Work Type')
    Residence_type=st.text_input('Residence_type')
    avg_glucose_level=st.text_input('Avg Glucose')
    bmi=st.text_input('BMI Value')
    smoking_status=st.text_input('Smoking status')
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    if st.button('Stroke Test Result'):
        user_input=[gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]
        user_input=[float(x) for x in user_input]
        diagnosis= stroke_model([user_input])
    
    st.success(diagnosis)
    
if __name__=='__main__':
    main()