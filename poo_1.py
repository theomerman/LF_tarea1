class Coche():
    def __init__(self):

        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos
        
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    
    def estado(self):
        print("El coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ",
            self.largoChasis)
        
        
miCoche = Coche()

print("El largo del coche es: ",Coche().largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
print(miCoche.arrancar(True))
miCoche.estado()

print("--------------------A continuación creamos el segundo objeto---------------------")

miCoche2 = Coche()

print("El largo del coche es: ",miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas, " ruedas")
print(miCoche2.arrancar(False))
miCoche2.estado()