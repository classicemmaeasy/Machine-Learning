# -*- coding: utf-8 -*-
"""
#Created on Fri Feb  9 14:11:23 2024

#@author: Emmanuel
#"""


import numpy as np 
import streamlit as st
import pickle


lomodel=pickle.load(open("C:/Users/HP/Downloads/gideon - Copy/gideon - Copy/stk-mod.sav", 'rb'))



#input_data=[1,3,1,0,1,0.0,0.81818182,2,0,2,0.0,0.181818182,0.0,2,2]
def stroke_mod(input_data):
    data_to_array= np.asarray(input_data)
    
    data_reshaped= data_to_array.reshape(1,-1)
    
    prediction= lomodel.predict(data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        return'you have a low risk of developing ischemic stroke'
    if (prediction[0] == 1):
        return'you have a Moderate risk of developing ischemic stroke'
    if (prediction[0] == 2):
        return'you have a high risk of developing ischemic stroke'
 
         
#stroke_mod(input_data)

def main():
    #giving a title 
    st.title('Ischemic Stroke Prediction Web App')
    name=st.text_input('Enter your name')
    #getting the input data  from the user
    gender = st.selectbox(
    'Gender:    (male=1 female=2)',('1','2'))
    age = st.selectbox(
    'age:    (20 -29yrs =0 ; 30-39yrs = 1 ; 40 -59yrs = 2 ; 60 and Above = 3)',('1','2', '3'))
    #age=st.text_input('Enter your age')
    heart_disease= st.selectbox(
    'have ever have a heart disease:  (Yes=1 ; No=0)',('1','0'))
    work_type= st.selectbox('what is your work type: (Never_work = 0 ; Former_worker = 1 ;  private = 2 ;  public = 3)', ('0','1','2','3'))
    smoking_status= st.selectbox(
    'what is your smoking status    (Never_Smoked=0 ;  Formerly_smoke=1 ;  Stay_around_smokers=2 ; Currently Smoking =3)',('0','1','2','3'))
    systolic= st.selectbox(
    'systolic value:  (120-129=0 ; 130-139=0.181818  ; 140-149=0.363636 ;  180=1)',('0','0.181818','0.363636','1'))
    diastolic= st.selectbox(
    'diastolic value:  (120-129= 0.81818182;  130-139=0.727273  ; 140-149=0.545455  ; 180=0.09090909)',('0','0.727273','0.545455','0.09090909'))
    diabetes= st.selectbox(
    'what is your diabetics status: Gestational:  (diabetes=0 ; Type 1 diabets=1 ;  Prediabetes=2 ; Type_2_Diabetes= 3)',('0','1','2','3'))
    family_histroy= st.selectbox(
    'did you ever have a stroke your family history  (No=0 ; Yes=1)',('0','1',))
    alchohol= st.selectbox(
    'Do you take alcohol  (Never=0 ; Moderate=1 ; Binge=2 ; Heavy =3)',('0','1','2','3'))
    BMI= st.selectbox(
    'BMI    (<18.5=0 ; 18.5-24.9 =0.278261;  25 - 29.9 =0.56087 ;  30 and above =1) ',('0','0.278261','0.56087','1'))
    high_cholesterol= st.selectbox('high cholesterol value:  (20mg/dl=1.909090909  ; <100mg/dl= 0.454545455 ; 100mg/dl - 129mg/dl=0.181818182  ; 130mg/dl or above= 0.090909091)',('1.909090909','0.454545455','0.181818182','0.090909091'))
    avg_glucose_level= st.selectbox('what is your average glucose level:  (1%-4.9% =0 ;  5%-5.6% = 0.727273 ;  5.7%-6.4% = 0.927273 ;  6.5% or higher = 1)',('0','0.727273','0.927273','1'))
    slep_apnea= st.selectbox('what type of sleep apnea do you have  (Never = 0 ; Obstructrual=1 ;  Central=2s ; Mixed or complex=3)',('0','1','2','3'))
    other_risk= st.selectbox('Other risk  (Vision problem=0; Numbness on one side=1; Weakness_on_one_side=2; Paralysis_on_one_side=3)',('0','1','2','3'))
    #code for prediction
    diagnose=''
    
    #creating a button for prediction
    if st.button('ischemic stroke prediction'):
        user_input=[gender,age,heart_disease,work_type,smoking_status,systolic,diastolic,diabetes,family_histroy,alchohol,BMI,high_cholesterol,avg_glucose_level,slep_apnea,other_risk]
        user_input=[float(x) for x in user_input]
        diagnose= stroke_mod([user_input])
    
    st.success('Hello!'+'     '+name+'    '+diagnose)
    
if __name__=='__main__':
    main()

