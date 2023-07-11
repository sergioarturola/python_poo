"""
Crea una clase base llamada estudiante con los atributos nombre, apellido y cedula, despues una clase derivada llamada
calificacion que pida 4 notas entre 0 y 100 ademas validar que solo ingresen numeros enteros, mostrar datos mediante una funcion
"""

#clase base
class Estudiante:

    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido



#clase derivada
class Calificacion(Estudiante):
      
    def __init__(self, cedula, nombre, apellido):
        Estudiante.__init__(self, cedula, nombre, apellido)
        self.calificaciones = []
        self.numero = 0
        self.contador = 0

        while self.contador < 4:
            print(f" Estudiante: {self.nombre} | Ingresa calificacion [{self.contador}]: ")
            try:
                self.numero = int(input())
            except ValueError:
                print("Ingresa solo numeros")

            if(self.numero >= 0 and self.numero <= 100):
                self.calificaciones.append(self.numero)
                self.contador += 1
            else:
                print("Calificacion no valida")


    def mostrarNotas(self):
        print("+------------------+")
        print(f"ESTUDIANTE {self.nombre} {self.apellido}")
        print(f"CEDULA: {self.cedula}")
        print("- Notas del semestre -")
        print(self.calificaciones)


#Creacion de objetos
estudianteUno = Calificacion(1234, "Juan", "Lopez")
estudianteDos = Calificacion(456, "Maria", "Gomez")
estudianteUno.mostrarNotas()
estudianteDos.mostrarNotas()