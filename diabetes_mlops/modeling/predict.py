import sys
import os
import pandas as pd
import joblib

# Añadir el directorio raíz que contiene config.py al sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
config_path = os.path.join(root_dir, 'diabetes_mlops')  # Ajustar la ruta para encontrar config.py
sys.path.insert(0, config_path)

from config import Config  # Importar el archivo de configuración

# Definir la ruta del archivo de datos de entrada
input_data_path = os.path.join(root_dir, 'data', 'processed', 'diabetes_data_upload.csv')

# Definir la ruta de salida de las predicciones
output_dir = os.path.join(root_dir, 'data', 'predictions')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_path = os.path.join(output_dir, 'predictions.csv')

# Definir la función de predicción
def predict(new_data):
    """Realiza predicciones utilizando un modelo previamente entrenado.

    Esta función carga el modelo desde el archivo especificado en la configuración,
    verifica que las columnas de los datos de entrada coincidan con las esperadas y
    realiza predicciones sobre los nuevos datos.

    Args:
        new_data (pd.DataFrame): Un DataFrame que contiene los datos sobre los que se realizarán las predicciones.

    Raises:
        ValueError: Si faltan columnas en los datos de entrada que son necesarias para las predicciones.

    Returns:
        np.ndarray: Un array con las predicciones generadas por el modelo.
    """
    # Cargar el modelo entrenado desde el archivo almacenado
    model = joblib.load(Config.MODEL_PATH)

    # Verificar si las columnas de entrada coinciden con las esperadas (nueva forma)
    try:
        expected_cols = model.feature_names_in_
    except AttributeError:
        # En caso de que feature_names_in_ no exista, continuar sin verificación
        expected_cols = new_data.columns  # Suponer que las columnas son correctas

    missing_cols = set(expected_cols) - set(new_data.columns)
    if missing_cols:
        raise ValueError(f"Las siguientes columnas faltan en new_data: {missing_cols}")

    # Realizar predicciones
    predictions = model.predict(new_data)

    # Convertir predicciones a un DataFrame para guardarlo como CSV
    df_predictions = pd.DataFrame(predictions, columns=['Prediction'])
    df_predictions.to_csv(output_path, index=False)

    return predictions

# Cargar los datos de entrada y realizar la predicción
if __name__ == "__main__":
    try:
        new_data = pd.read_csv(input_data_path)
        predict(new_data)
        print(f"Predicciones guardadas en {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error en las columnas de datos: {e}")
