# Crea una biblioteca de funciones numéricas que contenga las siguientes funciones Recuerda que puedes usar unas dentro de otras si es necesario
# Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo Por ejemplo, la función 
# is_palindromic() resulta trivial teniendo reverse() y la función next_prime() también es muy fácil de implementar teniendo is_prime()

def is_prime(a: int):
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False
    
    # comprobamos divisores impares desde 3 hasta la raiz cuadrada del numero
    # solo necesitamos llegar hasta la raiz, ya que si hay un divisor mayor, ya habriamos encontrado un divisor mas pequeño
    # usamos int(a**0.5) para obtener la raiz cuadrada sin usar math
    limite = int(a**0.5)
    
    for i in range(3, limite + 1, 2): # incrementamos de 2 en 2 (solo impares)
        if a % i == 0:
            return False # encontramos un divisor 
            
    return True # si el bucle termina, el numero es primo
        
print(f"El resultado de comprobar si 4 es primo es {is_prime(4)} y si 5 es primo es {is_prime(5)} (NOTA: esta funcion esta mal implementada)")

def next_prime(a: int):
    a +=1 
    while True:
        if is_prime(a):
            break
        else:
            a += 1
    return a

print(f"El siguiente numero primo despues de 7 es {next_prime(7)}")

def digits(num: int):
    num = abs(num)
    # caso de número 0
    if num == 0:
        return 1
        
    digitos = 0
    while num > 0:
        # a cada digito eliminado se suma al marcador
        num //= 10
        digitos += 1
        
    return digitos

print(f"El numero de digitos de 12345 es {digits(12345)} y de 0 es {digits(0)}")

def reverse(num: int):
    numero = 0
    while num != 0:
        numero = 10*numero+num % 10
        num //= 10 # divide y redondea hacia abajo
    return numero

print(f"El inverso de 12345 es {reverse(12345)}")

def is_palindromic(num):
    return num == reverse(num)

print(f"El numero 121 es palindromico: {is_palindromic(121)}")


def digit_position(numero: int, digito_buscado: int) -> int:
    # comprueba que el digito esté entre 0 y 9
    if not (0 <= digito_buscado <= 9):
        return -1

    # se convierte a un valor absoluto por si el número es negativo
    numero = abs(numero)

    # por si el número es 0, para que entre en el bucle
    if numero == 0:
        return 0 if digito_buscado == 0 else -1

    posicion = 0 
    # recorremos dígito a dígito, de derecha a izquierda
    while numero > 0:
        ultimo_digito = numero % 10  # Extrae el dígito más a la derecha
        if ultimo_digito == digito_buscado:
            return posicion  # si coincide, lo devolvemos
        # si no, eliminamos el num que acabamos de comparar y pasamos a la siguiente posicion
        numero //= 10  
        posicion += 1  
        
    # devolvemos -1 si no encontramos numero
    return -1

print(f"La posicion del digito 9 en 12948 es {digit_position(12948, 9)} (contando desde la derecha)")

def digit_n(numero: int, posicion: int):

    # valor absoluto por si el num es negativo
    numero = abs(numero)

    # contamos el numero de digitos
    digitos = 0
    num_temporal = numero
    if num_temporal == 0:
        digitos = 1
    else:
        digitos = digits(num_temporal)

    # si la posicion no existe devolvemos -1
    if posicion < 0 or posicion >= digitos:
        return -1

    # extraer el dígito de izquierda a derecha
    # si el numero = 75342 y posición = 2 (3), debemos eliminar los (total_digitos - posicion - 1) digitos de la derecha
    for _ in range(digitos - posicion - 1):
        numero //= 10

    # el ultimo digito es el que queremos
    return numero % 10

print(f"El digito en la posicion 2 de 12948 es {digit_n(12948, 2)}")

def remove_behind(numero: int, digitos: int):
    # eliminar numeros de la derecha (12345, 2) -> (123)
    contador = 0
    if digits(numero) > digitos:    
        while contador != digitos:
            numero //= 10
            contador += 1
    else: 
        numero = -1
    return numero

print(f"Al eliminar 3 digitos por detras de 12948, el resultado es {remove_behind(12948, 3)}")

def remove_ahead(numero: int, digitos: int):
    # eliminar numeros por delante, le damos la vuelta al numero y los borramos, lo volteamos de nuevo para devolverlo
    return reverse(remove_behind(reverse(numero), digitos))

print(f"Al eliminar 2 digitos por delante de 12948, el resultado es {remove_ahead(12948, 2)}")

def paste_behind(numero: int, digito: int):
    #debe ser un digito valido
    if 0 > numero < 9:
        print("Solo puede anadir un digito") 
        return -1
    # modulo de 10, sumado al numero * 10 
    digito = abs(digito) % 10
    nuevo = (numero * 10) + digito
    return nuevo

print(f"Al pegar el digito 4 por detras de 123, el resultado es {paste_behind(123, 4)}")

def paste_ahead(numero: int, digito: int):
    # mismo procedimiento que el remove, le damos la vuelta, reutilizamos la funcion y retornamos el reverse
    return reverse(paste_behind(reverse(numero),digito))

print(f"Al pegar el digito 9 por delante de 123, el resultado es {paste_ahead(123, 9)}")

def piece_of_number(numero: int, inicio: int, fin: int):
    # controlamos que no se salga de rango
    num_digitos = digits(numero)
    if inicio > (num_digitos-1) or inicio < 0:
        print("Posicion inicial fuera de rango")
        return -1
    if fin > (num_digitos-1) or fin < 0:
        print("Posicion final fuera de rango")
        return -1
    if inicio >= fin:
        print("El inicio debe ser menor que el final")
        return -1 
    modificado = 0
    for i in range(num_digitos):
        if inicio <= i <= fin:
            # si el indice esta dentro del rango (mayor que la inicial y menor que la final) 
            digito_actual = digit_n(numero, i) 
            modificado = paste_behind(modificado, digito_actual) 
            print(f"Posicion: {i} Anadido: {digito_actual} Numero: {modificado}")
            
    return modificado

print(f"El trozo del numero 12948 de la posicion 1 a 3 es {piece_of_number(12948, 1, 3)}")

def concatenate(numero_uno: int, numero_dos: int):
    temporal = numero_uno
    for i in range(digits(numero_dos)):
        temporal = paste_behind(temporal, digit_n(numero_dos, i))
    return temporal

print(f"Al concatenar 123 y 456, el resultado es {concatenate(123, 456)}")