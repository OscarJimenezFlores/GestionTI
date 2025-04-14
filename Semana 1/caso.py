"""
### Caso de Estudio. 
## Implementación de un Sistema de Gestión de Proyectos en una Empresa de Tecnología

#### Descripción del Proyecto

La empresa **TechSolutions S.A.** ha decidido implementar un sistema de gestión de proyectos para mejorar la planificación, ejecución y monitoreo de sus proyectos tecnológicos. Este sistema se diseñará para automatizar la asignación de tareas, la comunicación interna, el seguimiento del avance y la gestión de recursos.

El costo de implementación del sistema es de **$100,000** y se espera que genere ahorros en el tiempo de gestión, mejora en la asignación de recursos y una mayor eficiencia operativa, resultando en un incremento de ingresos proyectados de **$150,000** durante el primer año.

#### Objetivo del Caso de Estudio

1. **Calcular el ROI** de la implementación del sistema.
2. **Gestionar el proyecto** utilizando un sistema de tareas con tiempos estimados y recursos asignados.
3. **Visualizar los resultados** de la duración de cada fase del proyecto y la distribución de recursos.

#### Detalles del Proyecto

- **Costo de Implementación**: $100,000
- **Ingresos Proyectados (Ahorros y Mejora en Eficiencia)**: $150,000
- **Duración del Proyecto**: 6 meses
- **Tareas del Proyecto**: 5 tareas principales
  - Planificación (10 días)
  - Desarrollo (30 días)
  - Pruebas (15 días)
  - Implementación (5 días)
  - Monitoreo (20 días)

#### Datos del Proyecto

Para este caso de estudio, se utiliza el siguiente script python en google colab (https://colab.google):
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Función para calcular el ROI
def calcular_roi(inversion_inicial, ganancia_obtenida):
    beneficio_neto = ganancia_obtenida - inversion_inicial
    roi = (beneficio_neto / inversion_inicial) * 100
    return roi

# Datos del caso de estudio
inversion_inicial = 100000  # Costo de implementación del sistema
ganancia_obtenida = 150000  # Ahorros e ingresos generados por el sistema

# Calcular el ROI
roi = calcular_roi(inversion_inicial, ganancia_obtenida)

# Datos de las tareas del proyecto
data = {
    'Tarea': ['Planificación', 'Desarrollo', 'Pruebas', 'Implementación', 'Monitoreo'],
    'Duración (días)': [10, 30, 15, 5, 20],
    'Recursos Asignados (personas)': [2, 5, 3, 2, 4],
    'Estado': ['Completada', 'En progreso', 'Pendiente', 'Pendiente', 'Pendiente'],
    'Costo Estimado ($)': [5000, 30000, 15000, 5000, 10000]
}

# Crear un DataFrame con los datos del proyecto
df_proyecto = pd.DataFrame(data)

# Visualización de las tareas del proyecto
plt.figure(figsize=(10, 6))
plt.bar(df_proyecto['Tarea'], df_proyecto['Duración (días)'], color=['green', 'blue', 'orange', 'red', 'purple'])
plt.title('Duración de las Tareas del Proyecto de Gestión')
plt.xlabel('Tareas')
plt.ylabel('Duración (días)')
plt.show()

# Mostrar el ROI calculado
print(f"El ROI de la inversión en el sistema de gestión de proyectos es: {roi:.2f}%")

# Mostrar el DataFrame con detalles del proyecto
print("\nDetalles del Proyecto de Gestión:")
print(df_proyecto)

# Análisis adicional: Distribución del costo estimado por tarea
plt.figure(figsize=(10, 6))
plt.pie(df_proyecto['Costo Estimado ($)'], labels=df_proyecto['Tarea'], autopct='%1.1f%%', startangle=90)
plt.title('Distribución del Costo Estimado por Tarea')
plt.show()

# Análisis adicional: Recursos asignados por tarea
plt.figure(figsize=(10, 6))
plt.bar(df_proyecto['Tarea'], df_proyecto['Recursos Asignados (personas)'], color=['green', 'blue', 'orange', 'red', 'purple'])
plt.title('Recursos Asignados por Tarea del Proyecto')
plt.xlabel('Tareas')
plt.ylabel('Recursos Asignados (personas)')
plt.show()

