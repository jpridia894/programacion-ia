# Escribir un programa que lea un año indicar si es bisiesto 
# (un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).
anyo = int(input("Introduce un año: "))
if (anyo % 4 == 0) and (anyo % 100 != 0) and (anyo % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")
    