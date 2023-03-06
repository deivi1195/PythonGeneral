# Argumentos por defecto en una funcion:

def saludar(nombre, saludo='Hola', pais='Colombia'):
    """
    Saluda utilizando un saludo, un nombre y un pais de procedencia.
    
    Paramaters:
    nombre: Nombre de la persona
    saludo: El tipo de saludo (e.g., Hola, Buenos dias, Buenas tardes, Buenas noches).
    pais: Nacionalidad de la persona
    
    Returns:
    Una frase con el saludo que incluye el nombre y la nacionalidad
    """
    frase = f'{saludo}, mi nombre es {nombre}, y soy de {pais}'
    
    return frase
    

resultado = saludar('Edward', saludo='Buenos dias')

print(f'Resultado {resultado}')

resultado = saludar('Daniela',)

print(f'Resultado {resultado}')






