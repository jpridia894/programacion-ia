# 1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga las lista number con valores aleatorios entre 0 y 100. 
# En la lista square se deben almacenar los cuadrados de los valores que hay en number. En la lista cube se deben almacenar los cubos de los valores que hay en number. 
# A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

import random 

number = random.sample(range(0, 101), 20)
square = []
cube = []
# almacenamos el valor del numero con su correspondiente potencia
for numero in number:
    square.append(numero**2)
    cube.append(numero**3)

print("Método Tradicional:")
print("NUMERO \t CUADRADO \t CUBO")
print("-" * 30)

# con zip() iteramos sobre las tres listas a la vez
# usamos formato f-string (f"{variable:<X}") para alinear el texto a la izquierda
for numero, cuadrado, cubo in zip(number, square, cube):
    print(f"{numero:<6} \t {cuadrado:<8} \t {cubo:<10}")
