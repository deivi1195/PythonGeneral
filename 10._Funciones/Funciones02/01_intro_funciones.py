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

# 4. Creacion de una funcion para alternar los valores de dos variables
print('\nCreacion de una funcion para alternar los valores de dos variables')

# a = 2, b = 3
# a = 3, b = 2

# auxiliar = 2
# a = 3
# b = 2

def intercambiar_valores(a, b):
    """
    Intercambia los valores de dos variables.
    
    Parameters:
    a: primer valor.
    b: segundo valor.
    
    Returns:
    Los valores de a y b intercambiados.
    """
    auxiliar = a
    a = b
    b = auxiliar
    
    return a, b

x = 2
b = 4

print('Valores de las variables `x` e `y` antes del intercambio:')
print(f'x = {x} - y = {b}')

resultado = intercambiar_valores(x, b)

x = resultado[0]
b = resultado[1]

print('Valores de las variables `x` e `y` despues del intercambio:')
print(f'x = {x} - y = {b}')




