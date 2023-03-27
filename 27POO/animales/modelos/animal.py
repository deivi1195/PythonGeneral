from abc import ABC, abstractmethod

#esto nos quiere decir que la clase animal es abstracta (ABC), no podemos crear objetos de esa clase, unicamente nos sirve como referencia para la jerarquia de referencia que debemos especificar para las subclases.
class Animal(ABC):
    def __init__(self, nombre, edad, nombre_cientifico):
        self.nombre = nombre
        self.edad = edad
        self.nombre_cientifico = nombre_cientifico
        
    def comer(self):
        print('El animal esta comiendo...')
        
    def moverse(self):
        print('El animal se esta moviendo...')
        
    @abstractmethod
    def hablar(self):
        pass









