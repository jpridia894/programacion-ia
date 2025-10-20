# Crea un programa que muestre en pantalla los N primeros número primos. El valor de N se pide por teclado al usuario/a.
max = int(input("Introduce la cantidad de numeros primos a mostrar: "))
n = 1
primos = []
while len(primos) != max:
    if n % 2 == 0:
        primos.append(n)
    n += 1
print(f"Los {max} primeros numeros son: {primos}")
