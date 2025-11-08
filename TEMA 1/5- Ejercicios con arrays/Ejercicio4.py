# 4. Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista
# es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc.
# El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.

def pedirNumeros():
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el primer número: "))
    num3 = int(input("Introduce el primer número: "))
    num4 = int(input("Introduce el primer número: "))
    num5 = int(input("Introduce el primer número: "))
    lista = [num1, num2, num3, num4, num5]
    return lista

lista = pedirNumeros()
lista_aux = lista.copy()
print("Lista: ",lista)
contador = 0
for num in lista:
    if (contador) == len(lista) - 1:
        lista_aux[0] = lista[contador]
    else:
        lista_aux[contador + 1] = lista[contador]
    contador+=1
print("Lista modificada: ",lista_aux)