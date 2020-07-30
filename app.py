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
    RAM = int(request.form['RAM'])
    HDD = int(request.form['HDD'])
    SSD1 = int(request.form['SSD1'])
    SSD2 = int(request.form['SSD2'])
    OS = int(request.form['OS'])
    CHIPSET = int(request.form['CHIPSET'])
    SCREEN_SIZE = int(request.form['SCREEN_SIZE'])
    RESOLUTION = int(request.form['RESOLUTION'])
    GRAPHICS_CARD = int(request.form['GRAPHICS_CARD'])
    GPU_MEMORY = int(request.form['GPU_MEMORY'])
    #prediction = model.predict([[RAM,HDD,SSD1,SSD2,OS,CHIPSET,SCREEN_SIZE,RESOLUTION,GRAPHICS_CARD,GPU_MEMORY]])
    List=[RAM,HDD,SSD1,SSD2,OS,CHIPSET,SCREEN_SIZE,RESOLUTION,GRAPHICS_CARD,GPU_MEMORY]
    array=np.array(List)
    array1=np.reshape(array,(1,-1))
    #output = round(prediction[0], 2)
    prediction=model.predict(array1)
    print(prediction)
    return render_template('index.html', prediction_text='LAPTOP VALUE should be : Rs. {}'.format(prediction))
    
    

if __name__ == "__main__":
    app.run(debug=True)