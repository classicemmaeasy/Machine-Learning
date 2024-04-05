# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 23:33:45 2024

@author: Emmanuel
"""

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st

#loading the model
loaded_model=pickle.load(open('C:/Users/HP/Desktop/data/spam mail deployment/Nspam_model.sav', 'rb'))
tf_model=pickle.load(open('C:/Users/HP/Desktop/data/spam mail deployment/tf_model.sav', 'rb'))


#input_data=["I place all ur points on e cultures module already."]

#creating a function fro prediction
#input_data=["Congrats! 1 year special cinema pass for 2 is yours. call 09061209465 now! C Suprman V, Matrix3, StarWars3, etc "]
feature_ext= TfidfVectorizer(max_df=1, stop_words='english', lowercase='True')
def mail_prediction(input_data):
    trans_data= tf_model.transform(input_data)

    pred=loaded_model.predict(trans_data)

    print(pred) 

    if (pred[0] == 1):
            return "it is a ham  mail"
    else:
            return "It is a spam mail"
        
#mail_prediction(input_data)


def main():
    #giving a title 
    st.title('Spam Mail Prediction')
    
    #getting the input data  from the user

    mail= st.text_input('Enter a mail text')
    
    #code for prediction
    flag=''
    
    #creating a button for prediction
    if st.button('Flag Mail pred.result'):
        flag= mail_prediction([mail])
    
    st.success(flag)
    
if __name__=='__main__':
    main()