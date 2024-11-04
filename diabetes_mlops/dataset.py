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

def test_data_types(data):
    """Verifica los tipos de datos del dataset seleccionado"""
    dtypes = data.dtypes
    columns = data.columns
    errors = 0
    try:
        for column in columns:
            if column in Config.SCHEMA:
                assert dtypes[column] == Config.SCHEMA[column]['dtype'],\
                    "El tipo de dato de la columna {} no es de tipo {}".format(column, dtypes[column])
    except AssertionError as ae:
        print('ERROR EN PRUEBA DE TIPO DE DATOS:', ae)
        errors += 1
    else:
        print('Pruebas de tipo de dato CORRECTAS')
    
    return errors

def test_data_content(data):
    """Verifica los valores de los datos dentro del dataset"""
    columns = data.columns
    errors = 0
    try:
        for column in columns:
            if column in Config.SCHEMA:
                test_data_column(Config.SCHEMA[column], column, data)
    except AssertionError as ae:
        errors += 1
        print('ERROR EN PRUEBA DE VALORES DE DATOS:', ae)
    else:
        print('Pruebas de valores de datos CORRECTAS')
    return errors

def test_data_column(schema_node, column, data):
    """Verifica el dato que existe dentro de una columna en específico"""
    try:
        if column in Config.NUMERIC_FEATURES:
            assert data[column].min() >= schema_node[Config.RANGE][Config.MIN],\
            "Los valores de la columna {} no deben ser menores a {}".format(column, schema_node[Config.RANGE][Config.MIN])
            assert data[column].max() <= schema_node[Config.RANGE][Config.MAX],\
            "Los valores de la columna {} no deben ser mayores a {}".format(column, schema_node[Config.RANGE][Config.MAX])
        elif column in Config.CATEGORICAL_FEATURES:
            assert data[column].isin(schema_node[Config.OPTIONS]).all(),\
            "Los valores de la columna {} solo pueden estar dentro del siguiente conjunto {}".format(column, schema_node[Config.OPTIONS])
        elif column in Config.RESULT_FEATURE:
            assert data[column].isin(schema_node[Config.OPTIONS]).all(),\
            "Los valores de la columna {} solo pueden estar dentro del siguiente conjunto {}".format(column, schema_node[Config.OPTIONS])
    except AssertionError as ae:
        raise(ae)

if __name__ == '__main__':
    # Cargar los datos
    raw_data = load_data()
    print("Datos crudos cargados correctamente")
    # Pruebas de tipos de dato
    data_type_errors = test_data_types(raw_data)
    # Pruebas de valores
    data_content_errors = test_data_content(raw_data)
    if data_type_errors + data_content_errors > 0:
        sys.exit()
    
    # Preprocesar los datos
    # processed_data = preprocess_data(raw_data)
    print("Datos preprocesados correctamente")
    
    # Guardar los datos preprocesados
    save_processed_data(raw_data)

