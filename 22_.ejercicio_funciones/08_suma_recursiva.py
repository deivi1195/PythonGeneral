# Crear una funcion recursiva para sumar los numeros de una lista.

# [1, 2, 3, 4, 5]

def sumar_lista(numeros):
    """
    Suma los elementos de una lista.
    
    Parameters:
    Lista de valores numericos.
    
    Returns:
    Suma de los valores de la lista.
    """
    if len(numeros) == 0:
        return 0
    else:
        return numeros[0] + sumar_lista(numeros[1:])
    
valores = [1, 2, 3, 4, 5]
resultado = sumar_lista(valores)

print(f'La suma es igual a: {resultado}')
























