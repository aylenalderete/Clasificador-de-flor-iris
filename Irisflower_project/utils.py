import numpy as np 
import joblib
import pickle


def preprocessdata(SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm):
    test_data = [[SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm] ]
    print(test_data, 'hola')
    trained_model = pickle.loads('modelo_entrenado.pkl')
    prediction = trained_model.predict(test_data) 

    return prediction 