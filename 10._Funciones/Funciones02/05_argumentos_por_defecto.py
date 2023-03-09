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

print(f'\nResultado {resultado}')

resultado = saludar('Daniela',)

print(f'\nResultado {resultado}')


resultado = saludar('Oliva', pais='Espa;a', saludo='Buenas noches')

print(f'\nResultado {resultado}')

print(f'\nCalculando la exponente de un numero:')
def exponenciacion(base, exponente=2):
    """
    Calcula la exponenciacion de un numero base con respecto a un exponente
    
    Parameters:
    base: Base de la exponenciacion.
    exponente: Potencia de la exponenciacion (valor por defecto 2).
    
    Returns:
    Exponenciacion de una base y un exponente
    """
    resultado = base ** exponente
    
    return resultado

potencia = exponenciacion(5)
print(f'El resultado de la exponenciacion es: {potencia}')

potencia = exponenciacion(10, 3)
print(f'El resultado de la exponenciacion es: {potencia}')










