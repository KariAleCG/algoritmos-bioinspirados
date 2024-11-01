import numpy as np
import random

# Parámetros
num_hormigas = 10
num_ciudades = 5
alpha = 1.0   # Importancia de la feromona
beta = 2.0    # Importancia de la distancia
evaporacion = 0.5
intensidad = 1.0
iteraciones = 100

# Generar una matriz de distancias aleatorias entre ciudades
np.random.seed(0)
distancias = np.random.rand(num_ciudades, num_ciudades) * 100
np.fill_diagonal(distancias, 0)  # La distancia de una ciudad a sí misma es 0

# Inicialización de la matriz de feromonas
feromonas = np.ones((num_ciudades, num_ciudades))

def probabilidad(ciudad_actual, no_visitadas, feromonas, distancias, alpha, beta):
    """Calcula las probabilidades de moverse a la siguiente ciudad."""
    numerador = [
        (feromonas[ciudad_actual][i] ** alpha) * ((1.0 / distancias[ciudad_actual][i]) ** beta)
        for i in no_visitadas
    ]
    denominador = sum(numerador)
    return [n / denominador for n in numerador]

def construir_solucion(num_ciudades, feromonas, distancias, alpha, beta):
    """Construye una solución individual para una hormiga."""
    solucion = [random.randint(0, num_ciudades - 1)]
    for _ in range(num_ciudades - 1):
        ciudad_actual = solucion[-1]
        no_visitadas = list(set(range(num_ciudades)) - set(solucion))
        probs = probabilidad(ciudad_actual, no_visitadas, feromonas, distancias, alpha, beta)
        siguiente_ciudad = random.choices(no_visitadas, weights=probs, k=1)[0]
        solucion.append(siguiente_ciudad)
    return solucion

def calcular_longitud(solucion, distancias):
    """Calcula la longitud total de la ruta de una hormiga."""
    return sum(distancias[solucion[i - 1]][solucion[i]] for i in range(len(solucion)))

def actualizar_feromonas(feromonas, hormigas, evaporacion, intensidad):
    """Actualiza la matriz de feromonas."""
    feromonas *= (1 - evaporacion)  # Evaporación
    for solucion, longitud in hormigas:
        for i in range(len(solucion) - 1):
            feromonas[solucion[i]][solucion[i + 1]] += intensidad / longitud

# Algoritmo principal
mejor_solucion = None
mejor_longitud = float("inf")

for _ in range(iteraciones):
    hormigas = []
    for _ in range(num_hormigas):
        solucion = construir_solucion(num_ciudades, feromonas, distancias, alpha, beta)
        longitud = calcular_longitud(solucion, distancias)
        hormigas.append((solucion, longitud))
        if longitud < mejor_longitud:
            mejor_solucion = solucion
            mejor_longitud = longitud
    actualizar_feromonas(feromonas, hormigas, evaporacion, intensidad)

print("Mejor solución:", mejor_solucion)
print("Mejor longitud:", mejor_longitud)
