'''@author: Sri Hari S'''

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)
linear=pickle.load('admission.pickle','rb')

@app.route('/')
def welcome():
    return 'welcome to Admission prediction app'

@app.route('/prediction',methods=['GET'])
def admission_prediction():
    """Let's predict admission in top university based on score get by the exams.
    _ _ _
    
    parameters:
        - name: GRE_Score
          in: query
          type: number
          required: true
        - name: TOEFL_Score
          in: query
          type: number
          required: true
        - name: University_Rating
          in: query
          type:number
          required: true
        - name: SOP
          in: query
          type: number
          required: true
        - name: LOR
          in: query
          type: number
          required: true
        - name: CGPA
          in: query
          type: number
          required: true
        - name: Research
          in: query
          type: integer
          required: flase

    responses:
         200: 
             description: The output values
    
    """
    GRE Score=request.args.get('GRE_Score')
    TOEFL Score=request.args.get('TOEFL_Score')
    University Rating = request.args.get('University_Rating')
    SOP = request.args.get('SOP')
    LOR = request.args.get('LOR')
    CGPA = request.args.get('CGPA')
    Research=request.args.get('Research')
    predition=linear.predict([['GRE_Score','TOEFL_Score','University_Rating','SOP','LOR','CGPA']])
    return 'The expected percentage of admission' + str(prediction)
    
@app.route('/predict_file',methods=['POST'])
def prediction_file:
    """predict the admission
    
    parameter:
      - name: file
        in:formData
        type:file
        required: true
        
    responses:
         200: 
             description: The output values
      
    """
    
    df_file=pd.read_csv(request.file.get('file'))
    prediction=linear.predict(df_file)
    return str(list(prediction))

if __name__='__main__':
    app.run()

