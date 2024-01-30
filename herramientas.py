import pandas as pd

def obtener_resumen_valores_unicos(df):
    # Obtener el número de valores únicos en cada columna
    valores_unicos = df.nunique()

    # Obtener el número total de valores en cada columna (no nulos)
    total_valores = df.count()

    # Obtener el número de valores nulos en cada columna
    valores_nulos = df.isnull().sum()

    # Obtener los tipos de datos de cada columna
    tipos_datos = df.dtypes

    # Calcular el porcentaje de valores nulos en cada columna
    porcentaje_nulos = (valores_nulos / df.shape[0]) * 100

    # Combinar los resultados en un nuevo DataFrame
    resumen_valores_unicos = pd.DataFrame({
        'Columna': valores_unicos.index,
        'Tipo de Dato': tipos_datos.values,
        'Valores Únicos': valores_unicos.values,
        'Total Valores': total_valores.values,
        'Valores Nulos': valores_nulos.values,
        'Porcentaje Nulos': porcentaje_nulos.values
    })
    
    return resumen_valores_unicos
def resaltar_filas(df, color='#D2F5A2', indices_a_resaltar=[0], axis=1):
    """
    Resalta filas específicas en un DataFrame con un color dado.

    Parameters:
    - df: DataFrame
    - color: str
      Color de resaltado, por ejemplo, 'yellow', 'lightblue', etc.
    - indices_a_resaltar: list of int
      Lista de índices de las filas que se deben resaltar.
    - axis: int, default: 1
      0 para resaltar filas, 1 para resaltar columnas.

    Returns:
    - Styler object
    """
    #if indices_a_resaltar is None:
    #    indices_a_resaltar = []

    def _resaltar_filas(s):
        return [f'background-color: {color}' if i in indices_a_resaltar else '' for i in range(len(s))]

    styled_df = df.style.apply(_resaltar_filas, axis=axis)
    return styled_df

import numpy as np

def resaltar_filas_columnas(df, color1='#D2F5A2', color2 = 'red', indices_a_resaltar=None, columnas_a_resaltar=None):
    """
    Resalta filas y columnas específicas en un DataFrame con un color dado.

    Parameters:
    - df: DataFrame
    - color: str
      Color de resaltado, por ejemplo, 'yellow', 'lightblue', etc.
    - indices_a_resaltar: list of int, default: None
      Lista de índices de las filas que se deben resaltar.
    - columnas_a_resaltar: list of str, default: None
      Lista de nombres de columnas que se deben resaltar.

    Returns:
    - Styler object
    """
    if indices_a_resaltar is None:
        indices_a_resaltar = []

    if columnas_a_resaltar is None:
        columnas_a_resaltar = []

    def _resaltar_filas_columnas(data):
        styles = np.full_like(data, '', dtype=object)

        for i in indices_a_resaltar:
            styles[i, :] = f'background-color: {color1}'

        for col in columnas_a_resaltar:
            if col in df.columns:
                styles[:, df.columns.get_loc(col)] = f'background-color: {color2}'

        return styles

    styled_df = df.style.apply(_resaltar_filas_columnas, axis=None)
    return styled_df