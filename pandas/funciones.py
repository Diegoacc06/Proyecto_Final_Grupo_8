def promedios(nombre_archivo,nombre_columna):
    try:
        if nombre_columna in nombre_archivo.columns:
            promedio= nombre_archivo[nombre_columna].mean()
            return  f"El promedio de la columna {nombre_columna}, es: {promedio}."
        else:
            return "Error al procesar la columna."
    except Exception:
        return "Error al procesar la columna."
    
def desviacion(nombre_archivo, nombre_columna):
    try:
        if nombre_columna in nombre_archivo.columns:
            desviacion_estandar= float(nombre_archivo[nombre_columna].std())
            return desviacion_estandar
        else:
            return "Error al procesar la columna."
    except Exception:
        return "Error al procesar la columna."
    
def percentiles(nombre_archivo, nombre_columna):
  import pandas as pd
  import numpy as np
  try:
        if nombre_columna not in nombre_archivo.columns:
            raise ValueError('Error al procesar la columna')
        
        
        percentil_25 = float(np.percentile(nombre_archivo[nombre_columna], 25))
        percentil_50 = float(np.percentile(nombre_archivo[nombre_columna], 50))
        percentil_75 = float(np.percentile(nombre_archivo[nombre_columna], 75))
        
        return percentil_25, percentil_50, percentil_75
    
  except Exception:
        return 'Error al procesar la columna'