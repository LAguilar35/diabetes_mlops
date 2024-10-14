import matplotlib.pyplot as plt
import seaborn as sns

def plot_histograms(data):
    """Genera histogramas del dataset."""
    data.hist(bins=15, figsize=(15, 10))
    plt.show()

def plot_correlation_matrix(data):
    """Genera la matriz de correlación."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(data.corr(numeric_only=True), annot=True, fmt='.2f', cmap='coolwarm')
    plt.show()

def plot_boxplots(data):
    """Genera boxplots para cada feature en función de la clase."""
    for column in data.columns[:-1]:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x='class', y=column, data=data)
        plt.title(f'Relationship between diabetes result and {column}')
        plt.show()
