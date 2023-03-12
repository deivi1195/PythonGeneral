# Programa Python:

def saludar(mensaje):
    print(mensaje)
    
class Persona:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        
edward = Persona(123456789, "Edward Ortiz")

saludo = f'Hola, Mi nombre es {edward.nombre}.'

saludar(saludo)


# AQUI LO QUE SE QUIERE DAR A ENTENDER ES QUE ESTE SCRIPT NO TIENE PUNTO DE ENTRADA ESPECIFICO POR PARTE DEL DESARROLLADOR POR LO CUAL EL PROGRAMA POR DEFECTO EMPIEZA DESDE LA LINEA 1











