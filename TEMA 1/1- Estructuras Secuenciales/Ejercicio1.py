# 1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
nombre = ""
while nombre == "":
    # se lo pedimos mientras la cadena no esté vacía
    nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}")