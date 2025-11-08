from typeguard import typechecked

@typechecked
class Duration:
    def __init__(self, horas: int = 0, min: int = 0, seg: int = 0):
        self.__horas = horas
        self.__min = min
        self.__seg = seg
        self.__formatear()
    
    def __str__(self):
        return f"{self.__horas}h {self.__min}m {self.__seg}s"
    
    def __getHoras(self):
        return self.__horas
    def __getMinutos(self):
        return self.__min
    def __getSegundos(self):
        return self.__seg
    
    def __setHoras(self, horas):
        self.__horas = horas
    def __setMinutos(self, min):
        self.__min = min
    def __setSegundos(self, seg):
        self.__seg = seg
        
    def __total_segundos(self):
        return self.__horas * 3600 + self.__min * 60 + self.__seg
    
    def __formatear(self):
        segundos = self.__total_segundos()
        self.__horas = segundos // 3600
        self.__min = segundos % 3600 // 60
        self.__seg = segundos % 3600 % 60
    
    def agregar_segundo(self):
        self.__seg += 1
        self.__formatear()
        
    # Sobrecargando operadores
    def __add__(self, obj: Duration | int):
        if isinstance(obj, Duration):
            return Duration(self.__horas + obj.__horas, 
                            self.__min + obj.__min, 
                            self.__seg + obj.__seg)
        else:
            return Duration(self.__horas, self.__min, self.__seg - obj)       
    def __sub__(self, obj: Duration):
        if isinstance(obj, Duration):
            return Duration(self.__horas - obj.__horas, 
                            self.__min - obj.__min, 
                            self.__seg - obj.__seg)
        else:
            return Duration(self.__horas, self.__min, self.__seg - obj)        

    def __eq__(self, obj: Duration):
        return (self.__horas, self.__min, self.__seg) == (obj.__horas, obj.__min, obj.__seg) 
    
    def __ne__(self, obj):
        return not self == obj
    
    def __gt__(self, obj: Duration):
        return (self.__horas, self.__min, self.__seg) > (obj.__horas, obj.__min, obj.__seg)
    def __lt__(self, obj: Duration):
        return not self.__gt__(obj) and self.__ne__(obj)
    
from time import sleep

t = Duration()

"""
while True:
    print(t)
    t.agregar_segundo()
    sleep(1)
"""
t1 = Duration(1,20,0)
t2 = Duration(min=40)
t3 = t1 + t2 
print(t3)
t3 = t3 - t2
print(t3)