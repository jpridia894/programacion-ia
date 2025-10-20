while True:
  numero1 = input("Introduce un número: ")
  numero2 = input("Introduce otro número: ")
  if numero1.isdigit() and numero2.isdigit():
    numero1 = int(numero1)
    numero2 = int(numero2)
    break
  elif not numero1.isdigit():
    print("Comprueba el primer número")
  elif not numero2.isdigit():
    print("Comprueba el segundo número")
  else:
    print("Comprueba ambos números")
numero = str(numero1)+str(numero2)
numeroInvertido = str(numero)[::-1]
print(f"El número invertido es {str(numeroInvertido)}")