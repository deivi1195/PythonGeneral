# Crear una funcion para sumar todos los numeros en una lista o tupla

def sumar(valores):
    """
    Suma el conjunto o grupo de valores de una lista o tupla
    
    Parameters:
    valores: Lista o tupla con los valores a suamr
    
    Returns:
    suma de los valores en la lista o tupla.
    """
    if isinstance(valores, (list, tuple)):
        
        acumulador = 0
        
        for v in valores:
            acumulador += v
            
        return acumulador
    else:
        raise ValueError('Ha pasado con que no es lista ni tupla.')
    
edades = [19, 29, 31, 21]
try:
    resultado = sumar(edades)
    print(f'El resultado de la suma es: {resultado}')
except ValueError as e:
    print("ERROR:", e)


precios = (999.9, 59.9, 27.5)
try:
    resultado = sumar(precios)
    print(f'El resultado de la suma es: {resultado}')
except ValueError as e:
    print("ERROR:", e)


numeros = 1000
try:
    resultado = sumar(numeros)
    print(f'El resultado de la suma es: {resultado}')
except ValueError as e:
    print("ERROR:", e)


