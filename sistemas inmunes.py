import numpy as np
from scipy.spatial.distance import mahalanobis
import matplotlib.pyplot as plt

# Generación de datos de muestra (normal)
def generar_datos_normal(n):
    return np.random.normal(50, 10, n)

# Generación de datos anómalos
def generar_datos_anomalos(n):
    return np.random.uniform(80, 120, n)

# Inicialización de anticuerpos aleatorios en el rango esperado (normal)
def inicializar_anticuerpos(num_anticuerpos, datos_normales):
    media = np.mean(datos_normales)
    desviacion = np.std(datos_normales)
    return np.random.normal(media, desviacion, num_anticuerpos)

# Función de detección de anomalías usando la distancia de Mahalanobis
def detectar_anomalias(datos, anticuerpos, datos_normales):
    anomalías = []

    # Calcular la matriz de covarianza
    covarianza = np.cov(datos_normales, rowvar=False)

    # Verificar si la matriz de covarianza es invertible
    try:
        inversa_cov = np.linalg.inv(covarianza)
    except np.linalg.LinAlgError:
        print("La matriz de covarianza es singular. Usando la distancia Euclidiana.")
        inversa_cov = None  # Establecer a None para usar otro método

    for dato in datos:
        es_anormal = True
        for anticuerpo in anticuerpos:
            if inversa_cov is not None:
                # Calcular la distancia de Mahalanobis si la matriz es invertible
                distancia = mahalanobis([dato], [anticuerpo], inversa_cov)
            else:
                # Usar distancia Euclidiana como alternativa
                distancia = np.linalg.norm(dato - anticuerpo)
                
            if distancia < 3:  # Umbral ajustable
                es_anormal = False
                break
        if es_anormal:
            anomalías.append(dato)
    return anomalías

# Parámetros
num_datos_normales = 100
num_datos_anomalos = 10
num_anticuerpos = 20

# Generación de datos
datos_normales = generar_datos_normal(num_datos_normales)
datos_anomalos = generar_datos_anomalos(num_datos_anomalos)
datos = np.concatenate((datos_normales, datos_anomalos))

# Inicialización de anticuerpos mejorada
anticuerpos = inicializar_anticuerpos(num_anticuerpos, datos_normales)

# Detección de anomalías mejorada
anomalias_detectadas = detectar_anomalias(datos, anticuerpos, datos_normales)

# Resultados
print("Anticuerpos generados:", anticuerpos)
print("Datos anómalos detectados:", anomalias_detectadas)

# Visualización de resultados
plt.figure(figsize=(10, 6))
plt.hist(datos_normales, bins=30, alpha=0.5, label='Datos Normales', color='blue')
plt.hist(datos_anomalos, bins=30, alpha=0.5, label='Datos Anómalos', color='red')
plt.axvline(x=3, color='green', linestyle='--', label='Umbral de Anomalía')
plt.axvline(x=-3, color='green', linestyle='--')
plt.title('Distribución de Datos Normales y Anómalos')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.legend()
plt.show()

