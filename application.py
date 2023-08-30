from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predictdata',methods=['POST','GET'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            CRIM = request.form.get('CRIM'),
            ZN = request.form.get('ZN'),
            INDUS = request.form.get('INDUS'),
            CHAS = request.form.get('CHAS'),
            NOX = request.form.get('NOX'),
            RM = request.form.get('RM'),
            AGE = request.form.get('AGE'),
            DIS = request.form.get('DIS'),
            RAD = request.form.get('RAD'),
            TAX = request.form.get('TAX'),
            PTRATIO = request.form.get('PTRATIO'),
            B = request.form.get('B'),
            LSTAT = request.form.get('LSTAT'),
        )
        pred_df = data.get_data_as_data_frame()
        print('Before Prediction')
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])
    
        




if __name__=="__main__":
    app.run(host="0.0.0.0")    