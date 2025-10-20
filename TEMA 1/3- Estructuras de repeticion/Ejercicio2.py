# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
num_pedidos = int(input("Introduce la cantidad de numeros a ingresar: "))
mayores, menores, iguales = 0, 0, 0
for i in range(num_pedidos):
    numero = int(input("Introduce un número: "))
    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1
print(f"Hay {mayores} mayores que cero, {menores} menores que cero y {iguales} iguales a cero")
