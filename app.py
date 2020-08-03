# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:21:42 2020

@author: gokul
"""


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = np.array(int_features)
    #prediction = model.predict(final_features)
    #output = round(prediction[0], 2)
    
 
    return render_template('index.html', prediction_text='LAPTOP VALUE should be : Rs. {}'.format(final_features.type))
    
    

if __name__ == "__main__":
    app.run(debug=True)
