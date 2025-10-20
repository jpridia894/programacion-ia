# Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir. 
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

inicio = int(input("Introduce el limite inferior: "))
fin = int(input("Introduce el limite superior: "))

while fin <= inicio:
    print("El numero de inicio debe ser menor que el de fin")
numeros = []
while True:    
    num = int(input("Introduce un número. Pulsa 0 para salir: "))
    if num == 0: break
    else: numeros.append(num)
suma = 0
numeros_fuera = 0
iguales_intervalo = []
for numero in numeros:
    if numero < fin and numero > inicio:
        suma += numero
    elif numero == inicio or numero == fin:
        iguales_intervalo.append(numero)
        suma += numero
    else:
        numeros_fuera += 1
print(f"La suma es: {suma}")
print(f"Hay {numeros_fuera} numeros que están fuera del intervalo")
print(f"Números iguales a los limites: {str(iguales_intervalo)}")
