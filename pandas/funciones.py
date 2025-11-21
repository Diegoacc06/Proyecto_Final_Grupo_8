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