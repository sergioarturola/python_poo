"""
Crear una clase llamada circulo que calcule el area y perimetro de un
circulo, crear un objeto y mostrar los datos por pantalla
"""

#Clase circulo
class Circulo:
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):

        print( 3.1416*(self.radio * self.radio) )
    
    def perimetro(self):
        print(2*3.1416*self.radio)

#objeto
circulo1 = Circulo(5)
circulo1.perimetro()
circulo1.area()