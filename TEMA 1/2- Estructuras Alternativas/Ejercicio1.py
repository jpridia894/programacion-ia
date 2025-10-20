# 1. Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda.
# Ten en cuenta que ambas pueden tener la misma edad. 
# En tal caso, hazlo saber con un mensaje adecuado.
print("Programa para identificar que persona es mayor")
while True: 
    edad1 = input("Introduce la edad de Jorge: ")
    edad2 = input("Introduce la edad de Pepe: ")
    if edad1.isdigit() and edad2.isdigit():
        edad1 = int(edad1)
        edad2 = int(edad2)
        break
    
    elif not edad1.isdigit():
        print("El primer número no es válido")
    elif not edad2.isdigit():
        print("El segundo número no es válido")
    else: 
        print("Ninguno de los números es válido")
    
if edad1 > edad2:
    print(f"Jorge ({edad1}) es mas grande que Pepe ({edad2})")
elif edad1 < edad2:
    print(f"Pepe ({edad2}) es mas grande que Jorge ({edad1})")
else: 
    print(f"Ambos tienen la misma edad ({edad1}) ")