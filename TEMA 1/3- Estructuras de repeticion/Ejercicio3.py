# Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. 
# A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, 
# además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número 
# (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.
import random
num_intentos = 10
num_aleatorio = random.randint(1,100)
intento = 0
ganado = False
print("Programa para adivinar el número aleatorio ", num_aleatorio)
while intento < num_intentos and not ganado:
    numero = int(input("Introduce un número: "))
    if numero == num_aleatorio:
        print(f"Has acertado! Y lo has hecho en {intento} intentos")
        ganado = True
    elif numero < num_aleatorio:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")

    print(f"Te quedan {num_intentos - intento} intentos")


if not ganado:
    print(f"Se acabaron los intentos. El número era {num_aleatorio}")

