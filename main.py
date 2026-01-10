from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import List,Annotated, Literal
import pickle
import pandas as pd
from model.predict import predict_output
from schema.user_input import UserInput
from model.predict import predict_output,model,MODEL_VERSION
from schema.prediction_response import PredictionResponse


#importing the ml model 
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

#model flow
MODEL_VERSION = "1.0.0"

app = FastAPI()


#human readable home endpoint
@app.get('/')
def home():
    return {'insurance premium_predictor': 'API is running'}

#machine readable health check endpoint
@app.get('/health')
def health_check():
    return {'status': 'OK',
            'version': 'MODEL_VERSION',
            'model_loaded': 'True'}


@app.post('/predict', response_model = PredictionResponse)
def predict_premium(data: UserInput):

    user_input ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }

    try:

      prediction = predict_output(user_input)

      return JSONResponse(status_code=200, content={'response': prediction})

    except Exception as e:

      return JSONResponse(status_code=500, content={'error': str(e)})

