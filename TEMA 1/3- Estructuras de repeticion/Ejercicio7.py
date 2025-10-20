# Programa sencillo para calcular la cuota mensual de una hipoteca

importe = float(input("Importe del prestamo €: "))
interes_anual = float(input("Tasa de interes anual %: "))
plazo_anios = int(input("Plazo del prestamo en años: "))

# Convertimos a meses los datos
interes_mensual = interes_anual / 100 / 12
num_cuotas = plazo_anios * 12

# Fórmula para calcular la cuota mensual
cuota = importe * (interes_mensual * (1 + interes_mensual)**num_cuotas) / ((1 + interes_mensual)**num_cuotas - 1)
print("\n")
print(f"Importe del préstamo: {importe} €")
print(f"Tasa de interés anual: {interes_anual} %")
print(f"Plazo total: {plazo_anios} años ({num_cuotas} meses)")
print(f"Cuota mensual aproximada: {cuota:.2f} €")