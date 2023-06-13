import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__,template_folder="template")  # assign Flask = app
model = pickle.load(open('model.pkl', 'rb'))  ### import model 

@app.route('/')  
def home():
    return render_template('index2.html')  ## read index.html file

@app.route('/predict',methods=['POST'])  # transfer data from html to python / server
def predict():
	float_features = [float(x) for x in request.form.values()]  # Request for data values
	final_features = np.array(float_features)
	final_features_reshape = final_features.reshape(1, -1)
	prediction = [model.predict(final_features_reshape)]

	return render_template('index2.html',prediction_text="The Ultimate Tensile Strength of given composition is {} MPA".format(prediction[0][0]))
	
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)