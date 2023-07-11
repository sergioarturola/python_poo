class Asterisco:

    def imprimir(self):
        lineas = int(input("Digita el numero de lineas a imprimir: "))
        for i in range(1,lineas+1):
            for j in range(i):
              print( "*", end="") 
            
            print("")


asterisco = Asterisco()
asterisco.imprimir()