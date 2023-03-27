from modelos.animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, nombre_cientifico, raza):
        super().__init__(nombre, edad, nombre_cientifico)
        
        self.raza = raza
        
    def jugar(self):
        print('El perro esta jugando...')
        
    def hablar(self):
        print('Guau!')










