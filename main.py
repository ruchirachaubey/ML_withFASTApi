from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field,field_validator
from typing import List,Annotated, Literal
import pickle
import pandas as pd
from schema.user_input import UserInput


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


@app.post('/predict')
def predict_premium(data: UserInput):

    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])

    prediction = model.predict(input_df)[0]


    
    return JSONResponse(status_code=200, content={'predicted_category': prediction})

