import numpy as np
import pickle

#loading the model
loaded_model=pickle.load(open('C:/Users/HP/Desktop/data/diabetics deployment/trained_model.sav', 'rb'))



input_data=(8,183,64,0,0,23.3,0.672,32)

data_to_array= np.asarray(input_data)

data_reshaped= data_to_array.reshape(1,-1)

prediction= loaded_model.predict(data_reshaped)
print(prediction)

if (prediction[0] == 0):
    print('the person is not diabetic')
else:
     print('the person is diabetic')