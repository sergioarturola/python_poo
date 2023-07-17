"""
Realizar una clase en la cual se pase un numero mediante el constructor y por
medio de una funcion se haga la sumatoria desde 0 hasta el numero dado
"""

class Numero:
    
    def __init__(self, entero):
        self.entero = entero
    
    def sumatoria(self):
        suma = 0
        for i in range(self.entero+1):
            suma += i


        print("La suma es: ", suma) 


num = Numero(3)
num.sumatoria()