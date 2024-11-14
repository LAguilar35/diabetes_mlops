from typing import List
from fastapi import FastAPI, HTTPException
import pickle
from pydantic import BaseModel
import uvicorn

with open('trained_model.pkl', "rb") as f:
    model = pickle.load(f)

class DiabetesData(BaseModel):
    features = List[float]
    # Age: int
    # Gender: str
    # Polyuria: str
    # Polydipsia: str
    # sudden_weight_loss: str
    # weakness: str
    # Polyphagia: str
    # Genital_thrush: str
    # visual_blurring: str
    # Itching: str
    # Irritability: str
    # delayed_healing: str
    # partial_paresis: str
    # muscle_stiffness: str
    # Alopecia: str
    # Obesity: str
    # result: bool

app = FastAPI()

@app.post("/predict")
def predict(data: DiabetesData):
    pred = model.predict([data])
    return {"result": int(pred)}    


@app.get('/')
def read_root():
    return {"message": "API para predecir riesgo de presentar Diabetes"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)