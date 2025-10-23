a = int(input("Introduce un número: "))
b = int(input("Introduce otro número: "))
def sumar(a,b):
    suma = a+b
    print(f"El resultado de la suma es: {suma}\n\n") 

def restar(a,b):
    resta = a-b
    print(f"El resultado de la resta es: {resta}\n\n") 

def multiplicar(a,b):
    multiplicacion = a*b
    print(f"El resultado de la multiplicación es: {multiplicacion}\n\n")

def dividir(a,b):
    division = a / b
    print(f"El resultado de la división es: {division}\n\n") 

while True:
    print("--- MENU CALCULADORA ---")
    print("0.- Salir")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    opcion = int(input("Introduce una opción: "))
    match opcion:
        case 0:
            break
        case 1: 
            sumar(a,b)
        case 2:
            restar(a,b)
        case 3:
            multiplicar(a,b)
        case 4:
            try:
                dividir(a,b)
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        case _:
            print("El número introducido no es válido\n\n")