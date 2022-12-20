import pickle
import numpy as np

def survey_input(dict_input):
    data = []
    for key, value in dict_input.items():
        data.append(int(value))
    return np.array(data).reshape(1,-1)

def xgb_predict(input_data):
    # Use the model to make a prediction
    with open('xgb_reg.pkl', 'rb') as f:
        data = pickle.load(f)
    return data.predict(input_data)

if __name__ == '__main__':
    input_data = np.array([45, 0, 0, 0, 0, 155, 57, 0, 1, 0]).reshape(1,-1)
    print(xgb_predict(input_data))