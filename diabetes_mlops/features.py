from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from category_encoders import BinaryEncoder
from config import Config


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

