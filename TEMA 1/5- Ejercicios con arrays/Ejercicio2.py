# 2. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

import numpy as np

# con np.random.randint(min, max_excluido, size) generamos un array de 20 numeros aleatorios
number = np.random.randint(0, 101, 20)

# se aplican los calculos de forma directa a todo el array
square = number ** 2
cube = number ** 3

# np.column_stack apila los arrays horizontalmente, creando una matriz de 3 columnas
resultado_columnas = np.column_stack((number, square, cube))
print("Método Numpy:")
print("NUMERO \t CUADRADO \t CUBO")
print(resultado_columnas)
