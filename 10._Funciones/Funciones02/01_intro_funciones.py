# introduccion a las funciones - unidades de reutilizacion y encapsulacion de informacion

# 1. Creacion de una funcion:
print('1. Creacion de una funcion')

def sumar(numero_1, numero_2):
    """
    Suma dos numeros (sean enteros o punto flotante).
    
    Parameters:
    numero_1: primer valor a sumar.
    numero_2: segundo valor a sumar.
    
    Returns:
    Suma de dos numeros (enteros o reales).
    """
    suma = numero_1 + numero_2
    
    return suma

x = 2
y = 3

resultado = sumar(x, y)

print(f'La suma de {x} y {y} es igual a: {resultado}')

# 2. Invocacion de una funcion

resultado = sumar(2, 3)
print(f'La suma de {x} y {y} es igual a: {resultado}')

# 3. Obtener documentacion/ayuda de una funcion:
print('\nObtener documentacion/ayuda de una funcion:')

help(sumar)




