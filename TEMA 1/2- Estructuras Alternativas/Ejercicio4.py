# Escribir un programa que que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. 
# Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.
cantidad_usuario = int(input("Introduce la cantidad exacta en euros: "))
valores = [500, 200, 100, 50, 20, 10, 5, 2, 1]
print(f"Cantidad minima para {cantidad_usuario}")

for (valor) in valores:
    if cantidad_usuario >= valor:
        numero = cantidad_usuario // valor
        cantidad_usuario = cantidad_usuario % valor
        if valor >= 5:
            print(f"{numero} billetes de {valor}€")
        else:
            print(f"{numero} monedas de {valor}€")