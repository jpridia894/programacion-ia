# Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar, multiplicar, dividir y terminar. 
# Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error.
# El menú se volverá a mostrar, a menos que no se de a la opción terminar.
a, b = 0, 0
def pedir_numeros():
    a, b = 0,0
    a = int(input("Introduce un número: "))
    b = int(input("Introduce otro número: "))
    return a, b
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

def menu():
    print("--- MENU CALCULADORA ---")
    print("0.- Salir")
    print("1.- Pedir números")
    print("2.- Sumar")
    print("3.- Restar")
    print("4.- Multiplicar")
    print("5.- Dividir")
    opcion = int(input("Introduce una opción: "))
    return opcion

def comprobarNumeros(a, b):
    if (a == None or b == None) or (a == 0 and b == 0):
        return False
    else:
        return True
    
while True:
    opcion = menu()
    match opcion:
        case 0:
            break
        case 1: 
            a, b = pedir_numeros()
        case 2: 
            if comprobarNumeros(a, b):
                sumar(a,b)
            else:
                print("Error. Debes inicializar los números primero\n\n")
        case 3:
            if comprobarNumeros(a, b):
                restar(a,b)
            else:
                print("Error. Debes inicializar los números primero\n\n")
        case 4:
            if comprobarNumeros(a, b):
                multiplicar(a,b)
            else:
                print("Error. Debes inicializar los números primero\n\n")
        case 5:
            try:
                if comprobarNumeros(a, b):
                    dividir(a,b)
                else:
                    print("Error. Debes inicializar los números primero\n\n")
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        case _:
            print("El número introducido no es válido\n\n")