class Date:
    def __init__(self, dia, mes, anyo):
        # Validar año, mes y día
        if not (1 <= mes <= 12):
            raise ValueError("El mes debe estar entre 1 y 12")
        if anyo < 1:
            raise ValueError("El año debe ser positivo")

        dias_mes = [31, 29 if self.es_bisiesto(anyo) else 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]

        if not (1 <= dia <= dias_mes[mes - 1]):
            raise ValueError(f"El mes {mes} tiene entre 1 y {dias_mes[mes - 1]} días")

        self.dia = dia
        self.mes = mes
        self.anyo = anyo

    def __str__(self):
        # con :02d aparece "08" en vez de "8" por ejemplo
        return f"{self.dia:02d}/{self.mes:02d}/{self.anyo}"

    def es_bisiesto(self, anyo):
        return anyo % 4 == 0 and (anyo % 100 != 0 or anyo % 400 == 0)
    
    # Sumar días
    def sumar_dias(self, n):
        dias_mes = [31, 29 if self.es_bisiesto(self.anyo) else 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]
        dia = self.dia
        mes = self.mes
        anyo = self.anyo

        for _ in range(n):
            dia += 1
            # si supera el limite es el dia 1 del mes siguiente
            if dia > dias_mes[mes - 1]:
                dia = 1
                mes += 1
                # si supera los 12 meses es el mes 1 del año siguiente
                if mes > 12:
                    mes = 1
                    anyo += 1
                    dias_mes[1] = 29 if self.es_bisiesto(anyo) else 28

        return Date(dia, mes, anyo)

    # Restar días
    def restar_dias(self, n):
        dias_mes = [31, 29 if self.es_bisiesto(self.anyo) else 28, 31, 30, 31, 30,
                    31, 31, 30, 31, 30, 31]
        dia = self.dia
        mes = self.mes
        anyo = self.anyo

        for _ in range(n):
            dia -= 1
            # si retrocede al mes 0, se vuelve a diciembre del año anterior
            if dia < 1:
                mes -= 1
                # si el mes es 0 o menos, volvemos al mes anterior
                if mes < 1:
                    mes = 12
                    anyo -= 1
                    dias_mes[1] = 29 if self.es_bisiesto(anyo) else 28
                dia = dias_mes[mes - 1]

        return Date(dia, mes, anyo)
    
    # Comparar fechas 
    def __lt__(self, otra):
        return (self.anyo, self.mes, self.dia) < (otra.anyo, otra.mes, otra.dia)

    def __eq__(self, otra):
        return (self.anyo, self.mes, self.dia) == (otra.anyo, otra.mes, otra.dia)

    # Dia de la semana - Congruencia de Zeller
    def dia_semana(self):
        dia = self.dia
        mes = self.mes
        anyo = self.anyo

        # Si el mes es enero o febrero, se cuentan como mes 13 y 14 del año anterior
        if mes < 3:
            mes += 12
            anyo -= 1

        # Partimos el año
        primeros_dos = anyo // 100  # primeros dos dígitos, 2025 → 20
        ultimos_dos = anyo % 100    # ultimos dos dígitos, 2025 → 25

        # Formula de Zeller: https://parzibyte.me/blog/posts/congruencia-zeller-python/
        indice_dia = (dia + (13 * (mes + 1)) // 5 + ultimos_dos + (ultimos_dos // 4) + (primeros_dos // 4) + 5 * primeros_dos) % 7

        # Traducción del número a nombre de día
        dias = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        return dias[indice_dia]

# Main
f1 = Date(28, 2, 2025)
print("Fecha 1:", f1)
print("Día de la semana:", f1.dia_semana())

f2 = f1.sumar_dias(3)
print("Sumamos 3 dias:", f2)

f3 = f2.restar_dias(5)
print("Restamos 5 dias:", f3)

print(f"¿{f3} < {f1}?", f3 < f1)
print(f"¿{f3} == {f1}?", f3 == f1)