"""This script contains functions for visualizing data considering most of the variables are binary.
It includes:
1. Histogram generation for exploring data distribution.
2. Correlation matrix plotting for examining relationships between variables.
3. Boxplot generation for analyzing the distribution of each value.
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from dataset import load_data, preprocess_data

def plot_histograms(data):
    """Genera histogramas del dataset.

    Los histogramas permiten visualizar la distribución de cada variable en el conjunto de datos.

    Args:
        data (pd.DataFrame): El DataFrame que contiene los datos a visualizar.

    Returns:
        None: Muestra los histogramas generados.
    """
    data.hist(bins=15, figsize=(15, 10))
    plt.show()

def plot_correlation_matrix(data):
    """Genera la matriz de correlación.

    La matriz de correlación visualiza las relaciones entre las variables numéricas
    en el conjunto de datos, mostrando cómo se correlacionan entre sí.

    Args:
        data (pd.DataFrame): El DataFrame que contiene los datos a analizar.

    Returns:
        None: Muestra la matriz de correlación generada.
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
    plt.show()

def plot_boxplots(data):
    """Genera boxplots para cada característica en función de la clase.

    Los boxplots permiten visualizar la distribución de los valores de cada variable
    en función de la clase, ayudando a identificar la presencia de outliers y la
    variabilidad en los datos.

    Args:
        data (pd.DataFrame): El DataFrame que contiene los datos a visualizar.

    Returns:
        None: Muestra los boxplots generados.
    """
    for column in data.columns[:-1]:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x='class', y=column, data=data)
        plt.title(f'Relationship between diabetes result and {column}')
        plt.show()


# Cargar y preprocesar los datos
print("Cargando y preprocesando los datos...")
data = load_data()
data = preprocess_data(data)

plot_correlation_matrix(data)