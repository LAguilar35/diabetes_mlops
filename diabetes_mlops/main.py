from typing import List
from fastapi import FastAPI, HTTPException
import joblib
from pydantic import BaseModel
import uvicorn
import pandas as pd

with open('trained_model.pkl', "rb") as f:
    model = joblib.load(f)

class DiabetesData(BaseModel):
    Age: int
    Gender: str
    Polyuria: str
    Polydipsia: str
    sudden_weight_loss: str
    weakness: str
    Polyphagia: str
    Genital_thrush: str
    visual_blurring: str
    Itching: str
    Irritability: str
    delayed_healing: str
    partial_paresis: str
    muscle_stiffness: str
    Alopecia: str
    Obesity: str

app = FastAPI()

@app.post("/predict")
def predict(data: DiabetesData):
    new_data = [data.Age, data.Gender, data.Polyuria, data.Polydipsia, data.sudden_weight_loss, 
                data.weakness, data.Polyphagia, data.Genital_thrush, data.visual_blurring, data.Itching, 
                data.Irritability, data.delayed_healing, data.partial_paresis, data.muscle_stiffness, 
                data.Alopecia, data.Obesity]
    cols = ['Age','Gender','Polyuria','Polydipsia','sudden weight loss',
            'weakness','Polyphagia','Genital thrush','visual blurring','Itching',
            'Irritability','delayed healing','partial paresis','muscle stiffness','Alopecia',
            'Obesity']
    df = pd.DataFrame([new_data], columns=cols)

    pred = model.predict(df)
    return {"result": "Diabetes: {}".format('Yes' if int(pred) == 1 else 'No')}    


@app.get('/')
def read_root():
    return {"message": "API para predecir riesgo de presentar Diabetes"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)