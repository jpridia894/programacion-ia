# Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. 
# Si introducimos otro número nos da un error.
dia = int(input("Introduce el dia de la semana: "))
match dia:
    case 1:
        print(f"{dia}.- Lunes")
    case 2:
        print(f"{dia}.- Martes")
    case 3:
        print(f"{dia}.- Miércoles")
    case 4:
        print(f"{dia}.- Jueves")
    case 5:
        print(f"{dia}.- Viernes")
    case 6:
        print(f"{dia}.- Sábado")
    case 7:
        print(f"{dia}.- Domingo")
    case _:
        print("Día no válido")
3