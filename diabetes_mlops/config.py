import os

class Config:
    # Rutas relativas
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'raw', 'diabetes_data_upload.csv')
    MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'trained_model.pkl')
    MLFLOW_URI = 'http://127.0.0.1:5000'

    # Parámetros del modelo
    RANDOM_STATE = 42
    TEST_SIZE = 0.2
    CV_FOLDS = 5

    # Columnas de características
    NUMERIC_FEATURES = ['Age']
    CATEGORICAL_FEATURES = [
        'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
        'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
        'Itching', 'Irritability', 'delayed healing', 'partial paresis',
        'muscle stiffness', 'Alopecia', 'Obesity'
    ]
