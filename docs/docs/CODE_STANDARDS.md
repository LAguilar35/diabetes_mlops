# Estándares de Código para el Proyecto Diabetes MLOps

## Convenciones de Nomenclatura
- **Funciones y Variables**: Usar `snake_case` (ej., `load_data`, `process_features`).
- **Clases**: Utilizar `CamelCase` para nombres de clases (ej., `DataProcessor`, `ModelTrainer`).
- **Constantes**: Definir constantes en mayúsculas separadas por guiones bajos (ej., `DATA_PATH`, `MODEL_PATH`).
  
## Documentación
- **Docstrings**: Usar el formato Google o NumPy para todos los docstrings. Incluye:
    - **Descripción breve** del propósito de la función.
    - **Parámetros** con tipo y descripción.
    - **Retorno** y tipo de los valores devueltos.
    - **Excepciones** que pueden ser levantadas.
- **Comentarios**: Añadir comentarios claros para secciones complejas de código o bloques lógicos importantes. Mantener comentarios actualizados para reflejar cambios.

## Estilo de Código
- **Longitud de Línea**: Limitar las líneas a 79 caracteres.
- **Indentación**: Usar 4 espacios para la indentación, sin tabulaciones.
- **Importaciones**:
  - Agrupar importaciones en tres bloques (bibliotecas estándar, bibliotecas de terceros y módulos locales).
  - Ordenar alfabéticamente cada grupo de importaciones.
- **Comprobación de Calidad del Código**: Usar herramientas de linters como `flake8` y `pylint` para validar el estilo de código. 
  - Ejecutar el comando `flake8` o `pylint` antes de realizar cada commit.

## Prácticas de Seguridad en el Código
- **Validación de Entradas**: Implementar validación de entradas en todas las funciones críticas. Utilizar `assert` para verificar supuestos clave y reducir errores.
- **Manejo de Excepciones**:
  - Usar bloques `try-except` para manejar errores en funciones de acceso a archivos o procesos externos.
  - Especificar excepciones, evitando `except Exception` genérico.
  - **Ejemplo de Manejo de Excepciones**:
    ```python
    def load_data(filepath):
        """Carga los datos desde un archivo CSV.
        
        Args:
            filepath (str): Ruta al archivo CSV.
        
        Returns:
            pd.DataFrame: DataFrame con los datos cargados.
        
        Raises:
            FileNotFoundError: Si el archivo no existe.
            pd.errors.EmptyDataError: Si el archivo está vacío.
        """
        try:
            data = pd.read_csv(filepath)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return None
        except pd.errors.EmptyDataError as e:
            print(f"Error: {e}")
            return None
        return data
    ```
