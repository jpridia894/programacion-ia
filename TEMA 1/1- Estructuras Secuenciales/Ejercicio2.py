#2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
import math
cateto1 = 5
cateto2 = 4
hipotenusa = math.sqrt((cateto1**2)+(cateto2**2))
# O podemos usar otro método de la librería math
# hipotenusa = math.hypot(cateto1, cateto2)
print("La hipotenusa es:", hipotenusa)