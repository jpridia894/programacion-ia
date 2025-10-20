# Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))

if num1 >= num2 and num1 >= num3:
    num_mayor = num1
elif num2 >= num1 and num2 >= num3:
    num_mayor = num2
else: 
    num_mayor = num3

print(f"El mayor es {num_mayor}")
