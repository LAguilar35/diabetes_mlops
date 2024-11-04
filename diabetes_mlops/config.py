import os

class Config:
    """
    Clase de configuración para la aplicación de análisis de datos de diabetes.

    Esta clase contiene las rutas de archivos, parámetros del modelo y las características
    que se utilizarán en el análisis y modelado de datos relacionados con la diabetes.

    Atributos:
        BASE_DIR (str): Ruta base del directorio del archivo actual.
        DATA_PATH (str): Ruta al archivo CSV que contiene los datos de diabetes.
        MODEL_PATH (str): Ruta al archivo del modelo entrenado.
        MLFLOW_URI (str): URI del servidor MLflow para el seguimiento de experimentos.
        RANDOM_STATE (int): Semilla utilizada para la aleatorización.
        TEST_SIZE (float): Proporción del conjunto de datos que se utilizará para pruebas.
        CV_FOLDS (int): Número de pliegues para la validación cruzada.
        NUMERIC_FEATURES (list): Lista de características numéricas.
        CATEGORICAL_FEATURES (list): Lista de características categóricas.
    """
    # Rutas relativas
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    """
    Ruta base del directorio del archivo actual.
    """

    DATA_PATH = os.path.join(BASE_DIR, '..', 'data', 'raw', 'diabetes_data_upload.csv')
    """
    Ruta al archivo CSV que contiene los datos de diabetes.

    El archivo se espera que esté ubicado en el directorio 'data/raw' 
    en relación con el directorio base.
    """

    MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'trained_model.pkl')
    """
    Ruta al archivo del modelo entrenado.

    El archivo se espera que esté ubicado en el directorio 'models' 
    en relación con el directorio base.
    """

    MLFLOW_URI = 'http://127.0.0.1:5000'
    """
    URI del servidor MLflow para el seguimiento de experimentos.

    Se utiliza para registrar parámetros, métricas y modelos.
    """

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
    RESULT_FEATURE = ['class']

    # Parámetros para las pruebas
    DTYPE = 'dtype'
    INT_DTYPE = 'int64'
    OBJECT_DTYPE = 'object'
    RANGE = 'range'
    MIN = 'min'
    MAX = 'max'
    OPTIONS = 'options'

    SCHEMA = {
        'Age': {
            RANGE: {
                MIN: 16,
                MAX: 90
            },
            DTYPE: INT_DTYPE
        },
        'Gender': {
            OPTIONS: ['Male', 'Female'],
            DTYPE: OBJECT_DTYPE
        },
        'Polyuria': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Polydipsia': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'sudden weight loss': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'weakness': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Polyphagia': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Genital thrush': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'visual blurring': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Itching': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Irritability': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'delayed healing': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'partial paresis': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'muscle stiffness': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Alopecia': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'Obesity': {
            OPTIONS: ['No', 'Yes'],
            DTYPE: OBJECT_DTYPE
        },
        'class': {
            OPTIONS: ['Positive', 'Negative'],
            DTYPE: OBJECT_DTYPE
        }
    }

    ENABLED_PARAMS = {
        'LogisticRegression': {
            'classifier__C': 10,
            'classifier__solver': 'lbfgs',
            'classifier__max_iter': 100
        },
        'RandomForest': {
            'classifier__n_estimators': 50,
            'classifier__max_depth': 20,
            'classifier__min_samples_split': 10
        },
        'XGBClassifier': {
            'classifier__n_estimators': 200,
            'classifier__max_depth': 10,
            'classifier__learning_rate': 0.001
        }
    }