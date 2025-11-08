# 6. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

import numpy as np
# Matriz de 4x5  
matriz = np.random.randint(100, 1000, size=(4, 5))

# Calculamos la suma de cada fila y la añadimos como nueva columna
suma_filas = matriz.sum(axis=1) # suma horizontal (por filas)
matriz_con_filas = np.column_stack((matriz, suma_filas))

# Calculamos la suma de cada columna y la añadimos como nueva fila
suma_columnas = matriz_con_filas.sum(axis=0)  # suma vertical (por columnas)
matriz_nueva = np.vstack((matriz_con_filas, suma_columnas))
print(matriz_nueva)