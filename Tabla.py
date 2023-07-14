"""
Crear una clase llamanda tabla que mediante su constructor pida un numero e imprima
la tabla de dicho numero del 1 al 10, crear un objeto para ver resultados
"""

class Tabla:
    def __init__(self):

        self.numero = int(input("Digita un numero: "))
    

    def imprimir(self):

        for i in range(11):
            print(self.numero," * ",i," =", i*self.numero)


cinco = Tabla()
cinco.imprimir()