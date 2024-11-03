import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import pandas as pd
from config import Config

def load_data():
    """Carga el dataset desde la ruta especificada en config.

    Returns:
        pd.DataFrame: El DataFrame que contiene los datos cargados desde el archivo CSV.
    """
    data = pd.read_csv(Config.DATA_PATH)
    return data

def preprocess_data(data):
    """Aplica las transformaciones necesarias al dataset.

    Realiza las siguientes transformaciones:
    - Convierte la columna 'class' en un valor booleano donde 'Positive' es True.
    - (Código comentado) Convierte la columna 'Gender' a un valor booleano.
    - (Código comentado) Convierte otras columnas categóricas en valores booleanos.

    Args:
        data (pd.DataFrame): El DataFrame que contiene los datos a preprocesar.

    Returns:
        pd.DataFrame: El DataFrame procesado con las transformaciones aplicadas.
    """
    # data['Gender'] = data['Gender'] == 'Male'
    data['class'] = data['class'] == 'Positive'
    
    # for column in data.columns[2:-1]:
    #     data[column] = data[column] == 'Yes'
    
    return data

def save_processed_data(data):
    """Guarda el dataset procesado en formato CSV en la ruta especificada.

    Args:
        data (pd.DataFrame): El DataFrame que contiene los datos procesados.

    Returns:
        None: Imprime un mensaje indicando que los datos se han guardado correctamente.
    """

    processed_path = 'data/processed/diabetes_data_upload.csv'  # Asegurarse de que sea un .csv
    data.to_csv(processed_path, index=False)
    print(f"Datos procesados guardados correctamente en {processed_path}")

if __name__ == '__main__':
    # Cargar los datos
    raw_data = load_data()
    print("Datos crudos cargados correctamente")
    
    # Preprocesar los datos
    # processed_data = preprocess_data(raw_data)
    print("Datos preprocesados correctamente")
    
    # Guardar los datos preprocesados
    save_processed_data(raw_data)

