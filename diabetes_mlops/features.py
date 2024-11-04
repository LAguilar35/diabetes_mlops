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
    """
    Verifica los resultados obtenidos después de aplicar el preprocesador a los datos de entrenamiento.

    Parameters:
    preprocessor (ColumnTransformer): El preprocesador que aplica transformaciones a las características.
    X_train (pd.DataFrame): Datos de entrada de entrenamiento sin transformar.
    y_train (pd.Series): Etiquetas de entrenamiento asociadas a los datos.

    Returns:
    None

    Raises:
    AssertionError: Si alguna columna transformada no cumple con las pruebas de escalado o codificación.
    """
    preprocessor.set_output(transform='pandas')
    X_transformed_df = preprocessor.fit_transform(X_train, y_train)
    for column in X_transformed_df.columns:
        if 'numeric' in column:
            test_scaler(X_train, X_transformed_df, column)
        elif 'categorical' in column:
            test_encoder(X_transformed_df, column)

def test_scaler(data, transformed_data, column):
    """
    Verifica que los valores obtenidos después de aplicar el StandardScaler a una columna numérica sean correctos.

    Parameters:
    data (pd.DataFrame): Datos de entrada originales.
    transformed_data (pd.DataFrame): Datos de entrada transformados.
    column (str): Nombre de la columna transformada.

    Returns:
    None

    Raises:
    AssertionError: Si el promedio o la desviación estándar de la columna transformada no cumplen con las expectativas.
    """
    try:
        assert data[column.replace('numeric__', '')].mean() > transformed_data[column].mean(),\
        "El promedio de la columna original {} es menor al promedio despues del escalado".format(column)
        assert np.isclose(transformed_data[column].std(), 1.0, atol=1e-2),\
        "La desviación estándar de la columna {} es {}".format(column, transformed_data[column].std())
    except AssertionError as ae:
        raise(ae)
    
def test_encoder(data, column):
    """
    Verifica que los valores obtenidos después de aplicar el BinaryEncoder a una columna categórica sean correctos.

    Parameters:
    data (pd.DataFrame): Datos transformados que contienen la columna codificada.
    column (str): Nombre de la columna transformada.

    Returns:
    None

    Raises:
    AssertionError: Si los valores de la columna transformada no están en el conjunto {0, 1}.
    """
    try:
        assert data[column].isin([1.0, 0.0]).all(),\
        "Los valores de la columna {} despues del codificado son diferentes a 0 o 1".format(column)
    except AssertionError as ae:
        raise(ae)