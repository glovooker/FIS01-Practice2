def calcular_tiempo_impulso(distancia_en_metros, velocidad_impulso=100):
    """
    Calcula el tiempo que tarda un impulso nervioso en recorrer
    la distancia especificada, dado que la velocidad del impulso 
    nervioso es aproximadamente 100 m/s.

    Parámetros:
    distancia_en_metros (float): Distancia a recorrer en metros.
    velocidad_impulso (float): Velocidad del impulso (m/s). Por defecto: 100.

    Retorna:
    float: Tiempo en segundos que tarda el impulso en recorrer la distancia.
    """
    tiempo = distancia_en_metros / velocidad_impulso
    return tiempo

def main():
    print("Cálculo del tiempo de viaje de un impulso nervioso")
    distancia = float(input("Ingrese la distancia desde el punto de estímulo (en metros): "))
    tiempo_resultante = calcular_tiempo_impulso(distancia)
    print(f"El impulso nervioso tarda aproximadamente {tiempo_resultante:.4f} segundos en llegar al cerebro.")

if __name__ == "__main__":
    main()
