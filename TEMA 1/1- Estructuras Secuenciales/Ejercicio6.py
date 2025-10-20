preguntas = int(input("Introduce el número de preguntas que tuvo el examen: "))
correctas = int(input("Introduce el número de preguntas acertadas: "))
blanco = int(input("Introduce el número de preguntas en blanco: "))
falladas = int(input("Introduce el número de preguntas falladas: "))
if preguntas != (correctas + blanco + falladas):
  print("El número de respuestas no coincide con el número de preguntas")
else:
  puntuacion = (correctas * 5) - (falladas * 1)

puntuacionTotal = preguntas * 5
print(f"La puntuación final es de: {puntuacion}/{preguntas*5} puntos")
nota =  nota = (puntuacion / puntuacionTotal) * 10
print(f"La nota normalizada es de: {nota}")

# Para facilitar el sistema de puntuaje haría variables con la puntuación o incluso métodos por el cual se le pase por parametro dicha puntuación
