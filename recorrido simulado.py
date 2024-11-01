import numpy as np
import random
import math

# Parámetros
num_ciudades = 15
temperatura_inicial = 1000
temperatura_final = 1
tasa_enfriamiento = 0.99
iteraciones_por_temp = 100

# Generar una matriz de distancias aleatorias entre ciudades
np.random.seed(0)
distancias = np.random.rand(num_ciudades, num_ciudades) * 100
np.fill_diagonal(distancias, 0)  # La distancia de una ciudad a sí misma es 0

# Función para calcular la longitud total de una ruta
def calcular_longitud(ruta, distancias):
    return sum(distancias[ruta[i - 1]][ruta[i]] for i in range(len(ruta)))

# Función para generar una vecina de la ruta actual
def generar_vecina(ruta):
    vecina = ruta.copy()
    i, j = random.sample(range(len(ruta)), 2)
    vecina[i], vecina[j] = vecina[j], vecina[i]  # Intercambia dos ciudades
    return vecina

# Algoritmo de recocido simulado
def recocido_simulado(distancias, temperatura_inicial, temperatura_final, tasa_enfriamiento, iteraciones_por_temp):
    # Generar una ruta inicial aleatoria
    ruta_actual = list(range(len(distancias)))
    random.shuffle(ruta_actual)
    mejor_ruta = ruta_actual
    mejor_longitud = calcular_longitud(ruta_actual, distancias)
    temperatura = temperatura_inicial

    while temperatura > temperatura_final:
        for _ in range(iteraciones_por_temp):
            # Generar una vecina de la ruta actual
            nueva_ruta = generar_vecina(ruta_actual)
            longitud_actual = calcular_longitud(ruta_actual, distancias)
            nueva_longitud = calcular_longitud(nueva_ruta, distancias)

            # Aceptación de la nueva solución
            if nueva_longitud < longitud_actual:
                ruta_actual = nueva_ruta
            else:
                probabilidad = math.exp((longitud_actual - nueva_longitud) / temperatura)
                if random.random() < probabilidad:
                    ruta_actual = nueva_ruta

            # Actualizar la mejor solución
            if nueva_longitud < mejor_longitud:
                mejor_ruta = nueva_ruta
                mejor_longitud = nueva_longitud

        # Enfriamiento
        temperatura *= tasa_enfriamiento

    return mejor_ruta, mejor_longitud

# Ejecución del algoritmo
mejor_ruta, mejor_longitud = recocido_simulado(
    distancias, 
    temperatura_inicial, 
    temperatura_final, 
    tasa_enfriamiento, 
    iteraciones_por_temp
)

print("Mejor ruta:", mejor_ruta)
print("Longitud de la mejor ruta:", mejor_longitud)
