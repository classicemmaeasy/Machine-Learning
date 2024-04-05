# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 13:34:33 2024

@author: Emmanuel
"""


import numpy as np
import pickle
import streamlit as st

#load the model
loaded_model=pickle.load(open('C:/Users/HP/Desktop/data/HeartDisease Deployment/heartmod.sav', 'rb'))

#creating a function for prediction

#input_data=(58,0,2,120,340,0,1,172,0,0,2,0,2)

def HeartModel(input_data):
    np_data=np.asarray(input_data)
    
    Re_data=np_data.reshape(1,-1)
    prediction=loaded_model.predict(Re_data)
    print(prediction)
    
    if (prediction[0] == 0):
        return 'the person is not suffering from heart disease'
    else:
        return'the person is suffering from heart disease'
         
         
#HeartModel(input_data)


def main():
    #giving a title 
    st.title('Heart Disease Prediction Web App')
    
    #getting the input data  from the user

    Age= st.text_input('Enter your Age')
    Sex= st.text_input('Enter your Sex')
    cp= st.text_input('Cp value')
    trestbps=st.text_input('trestbps value')
    chol=st.text_input('chol value')
    fbs=st.text_input('fbs value')
    thalach=st.text_input('thalach value')
    restecg=st.text_input('restecg value')
    exang=st.text_input('exang Value')
    oldpeak=st.text_input('oldpeak Value')
    slope=st.text_input('slope Value')
    ca=st.text_input('Ca Value')
    thal=st.text_input('thal Value')
    
    #code for prediction
    diagnose=''
    
    #creating a button for prediction
    if st.button('Heart disease pred Test Result'):
        user_input=[Age,Sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        diagnose= HeartModel([user_input])
    
    
    st.success(diagnose)
    
if __name__=='__main__':
    main()