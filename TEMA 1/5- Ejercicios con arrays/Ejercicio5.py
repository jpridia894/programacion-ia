# 5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista de 4 filas por 5 columnas. 
# El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. La suma total debe aparecer 
# en la esquina inferior derecha.

import random

def generarMatriz():
    matriz = []
    for i in range(4): 
        lista = random.sample(range(100, 1000), 5)
        matriz.append(lista)
    return matriz


matriz = generarMatriz()
print(matriz)
contador_columna = 0
columnas = [0, 0, 0, 0, 0]
        
for fila in matriz:
    contador_fila = 0
    for numero in fila:
        contador_fila += numero
    fila.append(contador_fila)
    
for iColumna in range(5):
    contador_columna = 0
    for iFila in range(4):
        contador_columna += matriz[iFila][iColumna]
    columnas[iColumna] = contador_columna
    
suma_total = [0]
for valor in columnas:
    suma_total[0] += valor

matriz.append(columnas + suma_total)
print(matriz)
        