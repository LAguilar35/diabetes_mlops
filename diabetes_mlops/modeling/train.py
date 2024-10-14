import mlflow
import mlflow.sklearn
import sys
import os
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score, f1_score

# Asegurarse de que las rutas de los módulos sean correctas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from diabetes_mlops.config import Config
from diabetes_mlops.dataset import load_data, preprocess_data
from diabetes_mlops.features import create_pipeline

def train_model():
    try:
        # Cargar y preprocesar los datos
        print("Cargando y preprocesando los datos...")
        data = load_data()
        data = preprocess_data(data)

        print(f"Dimensiones del dataset después del preprocesamiento: {data.shape}")
    except Exception as e:
        print(f"Error al cargar o preprocesar los datos: {e}")
        return

    try:
        # Separar características y etiquetas
        print("Separando características y etiquetas...")
        X = data.drop('class', axis=1)
        y = data['class']

        # Dividir los datos en conjuntos de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=Config.TEST_SIZE, random_state=Config.RANDOM_STATE)
        print(f"Datos de entrenamiento X_train: {X_train.shape}, y_train: {y_train.shape}")
        print(f"Datos de prueba X_test: {X_test.shape}, y_test: {y_test.shape}")
    except Exception as e:
        print(f"Error en la separación de características y etiquetas: {e}")
        return

    try:
        # Crear pipeline de preprocesamiento
        print("Creando el pipeline de preprocesamiento...")
        preprocessor = create_pipeline()
    except Exception as e:
        print(f"Error al crear el pipeline de preprocesamiento: {e}")
        return

    # Modelos a evaluar
    models = {
        'LogisticRegression': LogisticRegression(class_weight='balanced'),
        'RandomForest': RandomForestClassifier(class_weight='balanced', random_state=Config.RANDOM_STATE),
        'XGBClassifier': XGBClassifier(scale_pos_weight=1, eval_metric='logloss')
    }

    # Hiperparámetros a evaluar para cada modelo
    param_grids = {
        'LogisticRegression': {
            'classifier__C': [0.1, 1, 10, 100],
            'classifier__solver': ['liblinear', 'lbfgs'],
            'classifier__max_iter': [100, 200]
        },
        'RandomForest': {
            'classifier__n_estimators': [50, 100, 200],
            'classifier__max_depth': [10, 20, None],
            'classifier__min_samples_split': [2, 5, 10]
        },
        'XGBClassifier': {
            'classifier__n_estimators': [50, 100, 200],
            'classifier__max_depth': [3, 6, 10],
            'classifier__learning_rate': [0.01, 0.1, 0.2]
        }
    }

    # Iniciar MLflow para el tracking de experimentos
    mlflow.set_tracking_uri(Config.MLFLOW_URI)
    mlflow.set_experiment("Diabetes Prediction")

    best_model = None
    best_score = 0
    best_params = None

    # Entrenar y evaluar cada modelo
    for model_name, model in models.items():
        try:
            print(f"Entrenando el modelo {model_name}...")
            model_pipeline = Pipeline([
                ('preprocessor', preprocessor),
                ('classifier', model)
            ])

            # Búsqueda de hiperparámetros con GridSearch
            grid_search = GridSearchCV(model_pipeline, param_grids[model_name], cv=Config.CV_FOLDS, n_jobs=-1)

            with mlflow.start_run(run_name=model_name):
                # Entrenar el modelo
                grid_search.fit(X_train, y_train)

                # Evaluar el modelo en el conjunto de prueba
                y_pred = grid_search.best_estimator_.predict(X_test)
                score = f1_score(y_test, y_pred)

                # Loggear resultados y el modelo en MLflow
                mlflow.log_params(grid_search.best_params_)
                mlflow.log_metric("accuracy", accuracy_score(y_test, y_pred))
                mlflow.log_metric("f1_score", score)
                mlflow.sklearn.log_model(grid_search.best_estimator_, "model")

                print(f"Modelo {model_name} entrenado con f1_score: {score}")

                # Guardar el mejor modelo si tiene mejor rendimiento
                if score > best_score:
                    best_model = grid_search.best_estimator_
                    best_score = score
                    best_params = grid_search.best_params_
        except Exception as e:
            print(f"Error en el modelo {model_name}: {e}")
            continue

    # Guardar el mejor modelo entrenado con DVC
    if best_model:
        try:
            # Cambiar la ruta para guardar el modelo en la carpeta 'models' en la raíz del proyecto
            model_path = os.path.join("models", Config.MODEL_PATH)
            joblib.dump(best_model, model_path)
            print(f"Mejor modelo guardado en {model_path} con f1_score: {best_score}")
            print(f"Mejores parámetros: {best_params}")
        except Exception as e:
            print(f"Error al guardar el mejor modelo: {e}")
    else:
        print("No se encontró un modelo con mejor rendimiento.")

if __name__ == '__main__':
    train_model()
