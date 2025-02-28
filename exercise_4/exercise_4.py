import math

def calcular_separacion_tras_3s(d, aA, aB):
    """
    Calcula la separación entre los dos carritos luego de 3 segundos.
    
    Parámetros:
    d (float): Separación inicial entre los pilotos (m).
    aA (float): Aceleración del piloto A (m/s^2).
    aB (float): Aceleración del piloto B (m/s^2).
    
    Retorna:
    float: Separación en metros tras 3 segundos.
    """
    t = 3.0
    # xA(t) = 0.5 * aA * t^2
    xA = 0.5 * aA * (t**2)
    # xB(t) = d - 0.5 * aB * t^2
    xB = d - 0.5 * aB * (t**2)
    return abs(xB - xA)

def calcular_tiempo_encuentro(d, aA, aB):
    """
    Calcula el tiempo que tardan en encontrarse (toparse) los dos pilotos.
    Asume que A inicia en x=0 y B en x=d, con aceleraciones en sentido opuesto.
    
    Parámetros:
    d (float): Separación inicial entre los pilotos (m).
    aA (float): Aceleración del piloto A (m/s^2).
    aB (float): Aceleración del piloto B (m/s^2).

    Retorna:
    float: Tiempo en segundos hasta que se encuentran.
    """
    # Resolviendo 0.5*aA*t^2 = d - 0.5*aB*t^2
    # => 0.5(aA + aB)*t^2 = d
    # => t^2 = 2d / (aA + aB)
    # => t = sqrt(2d / (aA + aB))
    if (aA + aB) == 0:
        return None  # Evita división por cero en caso de datos incorrectos
    t_encuentro = math.sqrt((2.0 * d) / (aA + aB))
    return t_encuentro

def main():
    print("Cálculos de separación y tiempo de encuentro de dos pilotos en carritos.")
    
    # Solicitar datos de entrada al usuario
    d = float(input("Ingrese la separación inicial (m): "))
    aA = float(input("Ingrese la aceleración del piloto A (m/s^2): "))
    aB = float(input("Ingrese la aceleración del piloto B (m/s^2): "))
    
    # (a) Separación después de 3 segundos
    separacion_3s = calcular_separacion_tras_3s(d, aA, aB)
    print(f"La separación después de 3.0 s es: {separacion_3s:.2f} m")
    
    # (b) Tiempo de encuentro
    tiempo_encuentro = calcular_tiempo_encuentro(d, aA, aB)
    if tiempo_encuentro is not None:
        print(f"El tiempo hasta que se topen es aproximadamente: {tiempo_encuentro:.2f} s")
    else:
        print("No es posible calcular el encuentro con los datos proporcionados (aA + aB = 0).")

if __name__ == "__main__":
    main()
