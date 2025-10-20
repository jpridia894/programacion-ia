while True:
  horas = input("Hora de salida: ")
  minutos = input("Minutos de salida: ")
  segundos = input("Segundos de salida: ")
  duracionViaje = input("Duración del viaje (en segundos): ")
  if not horas.isdigit():
    print("Las horas deben ser un número válido")
  elif not minutos.isdigit():
    print("Los minutos deben ser un número válido")
  elif not segundos.isdigit():
    print("Los segundos deben ser un número válido")
  elif not duracionViaje.isdigit():
    print("La duracion del viaje debe ser un número válido")
  else:
    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)
    duracionViaje = int(duracionViaje)
    break
# Lo convertimos todo a segundos y calculamos la hora de llegada
totalSalida = horas * 3600 + minutos * 60 + segundos
totalLlegada = totalSalida + duracionViaje

horasLlegada = (totalLlegada // 3600) % 24
minutosLlegada = (totalLlegada % 3600) // 60
segundosLlegada = totalLlegada % 60

print(f"El ciclista llegará a las {horasLlegada}:{minutosLlegada}:{segundosLlegada}")

