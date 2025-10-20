
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
num5 = int(input("Introduce el quinto número: "))
numeros = [num1, num2, num3, num4, num5]
contador = 0
num_mayor = num1
for num in numeros:
    if num > num_mayor:
        num_mayor = num
        
print(f"El número mayor es: {num_mayor}")
