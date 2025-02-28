def calcular_tiempo_crecimiento(longitud_inicial, longitud_final, tasa_crecimiento=2.0):
    """
    Calcula el tiempo necesario para que el cabello crezca
    desde 'longitud_inicial' hasta 'longitud_final', 
    dada una tasa de crecimiento (cm/mes).

    Parámetros:
    longitud_inicial (float): Longitud inicial del cabello (cm)
    longitud_final (float): Longitud final deseada (cm)
    tasa_crecimiento (float): Tasa de crecimiento del cabello en cm/mes.

    Retorna:
    float: Tiempo en meses que tarda el cabello en pasar de la longitud
           inicial a la longitud final.
    """
    if longitud_final <= longitud_inicial:
        # Si la longitud final es menor o igual a la inicial, no se requiere crecimiento
        return 0.0

    crecimiento_necesario = longitud_final - longitud_inicial
    tiempo_en_meses = crecimiento_necesario / tasa_crecimiento
    return tiempo_en_meses

def convertir_tiempo(tiempo_en_meses, unidad):
    """
    Convierte el tiempo en meses a la unidad solicitada.
    Unidades soportadas: 'meses', 'semanas', 'dias'.
    
    Parámetros:
    tiempo_en_meses (float): Tiempo en meses
    unidad (str): Unidad deseada para la conversión

    Retorna:
    float: Tiempo convertido en la unidad solicitada
    """
    unidad = unidad.lower()

    if unidad == "meses":
        return tiempo_en_meses
    elif unidad == "semanas":
        # Aproximación de 1 mes = 4.345 semanas
        return tiempo_en_meses * 4.345
    elif unidad == "dias":
        # Aproximación de 1 mes = 30 días
        return tiempo_en_meses * 30
    else:
        raise ValueError("Unidad de tiempo no reconocida. Use 'meses', 'semanas' o 'dias'.")

def main():
    print("Cálculo del tiempo de crecimiento de cabello")

    # Solicitar datos al usuario
    longitud_inicial = float(input("Ingrese la longitud inicial del cabello (en cm): "))
    longitud_final = float(input("Ingrese la longitud final deseada (en cm): "))
    tasa_crecimiento = float(input("Ingrese la tasa de crecimiento (cm/mes). Use 2 si no está seguro: "))

    # Calcular el tiempo en meses
    tiempo_meses = calcular_tiempo_crecimiento(longitud_inicial, longitud_final, tasa_crecimiento)

    # Solicitar unidad de tiempo de salida
    unidad = input("¿En qué unidad de tiempo desea el resultado? (meses, semanas, dias): ")
    try:
        tiempo_convertido = convertir_tiempo(tiempo_meses, unidad)
        print(f"El cabello tardará aproximadamente {tiempo_convertido:.2f} {unidad} en llegar de {longitud_inicial} cm a {longitud_final} cm.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
