# Programa Python con punto de entrada:

def saludar(mensaje):
    print(mensaje)
    
class Persona:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre

# aqui definiremos cualquier operacion de interes mayor
def main():
    edward = Persona(123456789, "Edward Ortiz")

    saludo = f'Hola, Mi nombre es {edward.nombre}.'

    saludar(saludo)

# Invocacion de esta funcion
if __name__ == '__main__':
    main()







