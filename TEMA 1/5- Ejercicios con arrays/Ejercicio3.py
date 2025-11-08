# 3. Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. 
# El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) 
# y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.

import numpy as np
#                     (min   max excluido, cantidad)
numeros = np.random.randint(0, 101, 20)
son_pares = (numeros % 2 == 0) # devuelve True o False en la posicion del num dependiendo si es par / impar

# recogemos en dos listas las coincidencias del array anterior
pares = numeros[son_pares]
impares = numeros[~son_pares]

# concatenamos ambas listas
resultado = np.concatenate((pares, impares))

print(f"Listado: {resultado}")