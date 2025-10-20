# Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

a = float(input("Introduce las medidas de A: "))
b = float(input("Introduce las medidas de B: "))
c = float(input("Introduce las medidas de C: "))

if (a**2 + b**2 == c**2) or (c**2 + b**2 == a**2) or (a**2 + c**2 == b**2): 
    print("Es un triángulo rectángulo")
elif (a == b and a == c and c != b) or (a == b and a != c and c == b) or (a != b and a == c and c == b):
    print("Es un triángulo isósceles")
elif a == b == c:
    print("Es equilátero")
else: 
    print("Es escaleno")