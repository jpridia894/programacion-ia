while True:
    minutos = input("Introduce la cantidad en minutos: ")
    if minutos.isdigit():   # isdigit() comprueba que sea un número positivo
        minutos = int(minutos)
        break
horas = minutos // 60 # división entera
minutosRestantes = minutos % 60 # módulo para los minutos
print(f"{minutos} minuto/s equivale a {horas} hora/s y {minutosRestantes} minuto/s")