import numpy as np
import pickle

# loading our trained model
load_model = pickle.load(open('E:/Computational Assignment/productivity.sav', 'rb'))

input_data = (1, 1, 4, 8, 0.8, 26.16, 1108, 7080, 98, 0, 0, 0, 59)

# changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# standardize the input data
# std_data = scaler.transform(input_data_reshaped)

prediction = load_model.predict(input_data_reshaped)
print('Your Productivity =', prediction)