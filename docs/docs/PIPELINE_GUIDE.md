# Guía del Pipeline DVC para el Proyecto Diabetes MLOps

Este proyecto utiliza DVC para gestionar y versionar el flujo de trabajo completo, asegurando que cada etapa sea reproducible y esté alineada con los objetivos de gobernanza y calidad.

## Etapas del Pipeline

## Configuración de DVC
DVC se utiliza para gestionar y versionar datos y modelos.

### Instrucciones Básicas de DVC
1. Inicializar DVC: `dvc init`
2. Añadir datos: `dvc add <ruta_datos>`
3. Guardar estado: `dvc commit`


### 1. Preprocesamiento de Datos (`preprocess`)
- **Descripción**: Esta etapa prepara los datos de entrada para el entrenamiento del modelo. Incluye limpieza, selección de características y cualquier transformación de datos necesaria.
- **Ejecución**: `dvc repro preprocess`
- **Salida Esperada**: `data/processed/diabetes_data_upload.csv`

### 2. Entrenamiento del Modelo (`train`)
- **Descripción**: Entrena el modelo utilizando los datos procesados en la etapa anterior.
- **Ejecución**: `dvc repro train`
- **Salida Esperada**: `models/trained_model.pkl`

### 3. Generación de Predicciones (`predict`)
- **Descripción**: Usa el modelo entrenado para realizar predicciones.
- **Ejecución**: `dvc repro predict`
- **Salida Esperada**: `data/predictions/predictions.csv`

## Instrucciones de Ejecución Completa
Para ejecutar todo el pipeline desde el inicio:
```bash
dvc repro
