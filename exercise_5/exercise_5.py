import time

def simulate_train():
    # Parámetros físicos
    v_crucero = 20.0        # m/s (72 km/h)
    a_frenado = -1.0        # m/s^2
    a_aceleracion = 0.5     # m/s^2
    t_parada_real = 120.0   # 2 minutos = 120 s

    # Parámetros de la simulación (ajustables)
    time_step = 0.5   # paso de tiempo de la simulación (en s)
    scale_dist = 10   # 1 carácter en pantalla = 10 metros
    time_scale = 0.2  # factor para "acelerar" la espera (parada)

    # Variables de estado
    t_sim = 0.0       # tiempo simulado transcurrido
    x = 0.0           # posición del tren (m)
    v = v_crucero     # velocidad inicial (m/s)
    fase = "frenado"  # fases: frenado -> parada -> aceleracion -> fin

    # Calcular la distancia donde se alcanza la estación (v=0)
    # (No es imprescindible, pero lo usamos para marcar la "S" en pantalla)
    # Distancia de frenado: v^2 / (2*|a|)
    d_frenado = (v_crucero**2) / (2.0 * abs(a_frenado))

    # Distancia para la fase de aceleración, desde 0 hasta v_crucero
    # v^2 / (2*a)
    d_acel = (v_crucero**2) / (2.0 * a_aceleracion)

    # Distancia total (frenado + aceleración)
    d_total = d_frenado + d_acel

    # Para la representación en ASCII, definimos un largo de vía
    # un poco mayor que d_total, para que se aprecie bien.
    track_length = int(d_total + 50)  # 50 m extra

    # Tiempo que dura el frenado teórico (20 s)
    # Tiempo que dura la aceleración teórica (40 s)

    t_espera = 0.0  # tiempo acumulado en la parada (simulado)
    parada_completada = False

    while True:
        # Imprimimos un "fotograma"
        # 1) Limpiamos pantalla de la consola o bajamos líneas
        print("\n" * 50)

        # 2) Construimos la representación en caracteres
        #    - Estación = en la posición donde tren se detiene (al final del frenado)
        #    - Tren     = posición x
        #    - '.'      = el resto de la vía

        # Índice del tren (en caracteres)
        train_index = int(x / scale_dist)

        # Índice de la estación (allí donde v=0 => x = d_frenado)
        station_index = int(d_frenado / scale_dist)

        # Nos aseguramos que los índices no se vayan más allá de la vía
        if train_index > track_length // scale_dist:
            train_index = track_length // scale_dist

        # Creamos un array de puntos
        track_array = ["." for _ in range(track_length // scale_dist + 1)]

        # Marcamos la estación con 'S'
        if station_index < len(track_array):
            track_array[station_index] = "S"

        # Marcamos la posición del tren con 'T'
        if train_index < len(track_array):
            track_array[train_index] = "T"
        else:
            track_array[-1] = "T"

        # Unimos todo en un string
        track_str = "".join(track_array)

        # Desplegamos información
        print(f"Tiempo simulado: {t_sim:.1f} s  |  Fase: {fase}")
        print(track_str)
        print(f"Posición: {x:.1f} m | Velocidad: {v:.1f} m/s")

        # Verificamos transiciones de fase
        if fase == "frenado":
            # Actualizamos velocidad y posición con aceleración negativa
            if v > 0:
                # Movimiento con MRUA (a_frenado)
                v_new = v + a_frenado * time_step
                if v_new < 0:
                    v_new = 0  # no bajar de 0
                # Desplazamiento (aprox v_prom * dt)
                x_new = x + 0.5*(v + v_new)*time_step
                v = v_new
                x = x_new
            else:
                # Ya frenó (v=0)
                fase = "parada"

        elif fase == "parada":
            # El tren está quieto
            v = 0
            # Acumulamos tiempo en la parada
            t_espera += time_step

            # Para no esperar 120 s reales, "aceleramos" ese lapso
            if t_espera >= t_parada_real * time_scale:
                fase = "aceleracion"

        elif fase == "aceleracion":
            # Acelera hasta llegar a 20 m/s
            if v < v_crucero:
                v_new = v + a_aceleracion * time_step
                if v_new > v_crucero:
                    v_new = v_crucero
                x_new = x + 0.5*(v + v_new)*time_step
                v = v_new
                x = x_new
            else:
                fase = "fin"

        elif fase == "fin":
            # Llegó a la velocidad de crucero otra vez.
            # Terminamos la simulación.
            print("\nSimulación finalizada: el tren volvió a 20 m/s.")
            break

        # Avanzamos el tiempo simulado
        t_sim += time_step
        # Hacemos una pequeña pausa para ver el "movimiento" en la consola
        time.sleep(0.05)


if __name__ == "__main__":
    simulate_train()
