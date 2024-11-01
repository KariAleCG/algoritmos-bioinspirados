import time

# Ordenamiento por inserción
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Mueve los elementos del arreglo que son mayores que la clave a una posición adelante
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Medición de tiempo para diferentes tamaños de entrada
def medir_tiempo(n):
    arr = list(range(n, 0, -1))  # Arreglo en orden inverso para peor caso
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    return end_time - start_time

# Prueba de tiempo para tamaños de entrada crecientes
for tamaño in [100, 200, 500, 1000, 2000]:
    tiempo = medir_tiempo(tamaño)
    print(f"Tamaño de entrada: {tamaño} - Tiempo de ejecución: {tiempo:.5f} segundos")
