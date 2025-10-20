# Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.
inicio = int(input("Introduce el primer número: "))
fin = int(input("Introduce el segundo número: "))

if inicio < fin:
    for i in range(fin):
        if inicio % 2 == 0:
            print(inicio)
        inicio+=1
else:
    print("El número de inicio debe ser menor que el de fin")