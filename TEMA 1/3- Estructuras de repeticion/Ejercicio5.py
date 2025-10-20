# Crea un programa que pida un número por teclado al usuario y diga si es primo. En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.
while True:
    num = input("Introduce un número: ")
    if not num.isdigit():
        print("Error, introduce un número válido")
    elif int(num) < 2:
        print("Error, introduce un número mayor que 2")
    else:
        num = int(num)
        if num % 2 == 0:
            print("Es primo")
        else: 
            print("No es primo")
        break