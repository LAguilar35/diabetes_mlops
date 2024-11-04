from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from category_encoders import BinaryEncoder
from config import Config
import pandas as pd
import numpy as np


def create_pipeline():
    """Crea un pipeline de preprocesamiento.

    Este pipeline está compuesto por dos sub-pipelines:
    - Un pipeline para características numéricas que aplica escalado estándar.
    - Un pipeline para características categóricas que aplica codificación binaria.

    Returns:
        ColumnTransformer: Un objeto ColumnTransformer que aplica las transformaciones
        adecuadas a las características numéricas y categóricas del conjunto de datos.
    """
    numeric_pipeline = Pipeline([
        ('scaler', StandardScaler())
    ])

    categorical_pipeline = Pipeline([
        ('encoder', BinaryEncoder())
    ])

    preprocessor = ColumnTransformer([
        ('numeric', numeric_pipeline, Config.NUMERIC_FEATURES),
        ('categorical', categorical_pipeline, Config.CATEGORICAL_FEATURES)
    ])

    return preprocessor

def test_feature_engineering_process(preprocessor: ColumnTransformer, X_train, y_train):
    """Verifica los resultados obtenidos después del preprocesamiento"""
    preprocessor.set_output(transform='pandas')
    X_transformed_df = preprocessor.fit_transform(X_train, y_train)
    for column in X_transformed_df.columns:
        if 'numeric' in column:
            test_scaler(X_train, X_transformed_df, column)
        elif 'categorical' in column:
            test_encoder(X_transformed_df, column)

def test_scaler(data, transformed_data, column):
    """Verifica los valores obtenidos del StandardScaler"""
    try:
        assert data[column.replace('numeric__', '')].mean() > transformed_data[column].mean(),\
        "El promedio de la columna original {} es menor al promedio despues del escalado".format(column)
        assert np.isclose(transformed_data[column].std(), 1.0, atol=1e-2),\
        "La desviación estándar de la columna {} es {}".format(column, transformed_data[column].std())
    except AssertionError as ae:
        raise(ae)
    
def test_encoder(data, column):
    """Verifica los valores obtenidos del BinaryEncoder"""
    try:
        assert data[column].isin([1.0, 0.0]).all(),\
        "Los valores de la columna {} despues del codificado son diferentes a 0 o 1".format(column)
    except AssertionError as ae:
        raise(ae)