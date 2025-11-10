from math import gcd  # maximo comun divisor

class Fraction:
    def __init__(self, numero: int, denominador: int):
        if denominador == 0:
            raise ValueError("El denominador no puede ser 0")
        self.numero = numero
        self.denominador = denominador
        self.__simplificar()
    
    def __str__(self):
        return f"{self.numero}/{self.denominador}"
    
    def __simplificar(self):
        mcdivisor = gcd(self.numero, self.denominador)
        self.numero //= mcdivisor
        self.denominador //= mcdivisor
        # si el denominador es negativo, se le pasa el signo al numerador 
        # y el denominador pasa a positivo
        if self.denominador < 0:
            self.numero *= -1
            self.denominador *= -1

    # Convertir a numero decimal
    def parse_float(self):
        return self.numero / self.denominador
    
    # Sobrecarga de operadores
    def __add__(self, other):
        if isinstance(other, Fraction):
            num = self.numero * other.denominador + other.numero * self.denominador
            den = self.denominador * other.denominador
        elif isinstance(other, (int, float)):
            num = self.numero + other * self.denominador
            den = self.denominador
            
        return Fraction(int(num), int(den))
    
    def __sub__(self, other):
        if isinstance(other, Fraction):
            num = self.numero * other.denominador - other.numero * self.denominador
            den = self.denominador * other.denominador
        elif isinstance(other, (int, float)):
            num = self.numero - other * self.denominador
            den = self.denominador
            
        return Fraction(int(num), int(den))
    
    def __mul__(self, other):
        if isinstance(other, Fraction):
            num = self.numero * other.numero
            den = self.denominador * other.denominador
        elif isinstance(other, (int, float)):
            num = self.numero * other
            den = self.denominador

        return Fraction(int(num), int(den))
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            num = self.numero * other.denominador
            den = self.denominador * other.numero
        elif isinstance(other, (int, float)):
            num = self.numero
            den = self.denominador * other
            
        return Fraction(int(num), int(den))

    # Comparadores
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numero * other.denominador == other.numero * self.denominador
        elif isinstance(other, (int, float)):
            return self.parse_float() == other


    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numero * other.denominador < other.numero * self.denominador
        elif isinstance(other, (int, float)):
            return self.parse_float() < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    def __ne__(self, other):
        return not self == other
      
# Main
f1 = Fraction(1, 2)
f2 = Fraction(2, 4)
f3 = Fraction(3, 5)

print("Fraccion 1:", f1)
print("Fraccion 2:", f2)
print("Son iguales:", f1 == f2)      # Si, 1/2 = 2/4
print("Suma:", f1 + f3)              # 11/10
print("Resta:", f1 - f3)             # -1/10
print("Multiplicacion:", f1 * f3)    # 3/10
print("Division:", f1 / f3)          # 5/6
