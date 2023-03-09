# Crear una funcion para multiplicar todos los numeros en una lista o tupla

def multiplicar(valores):
    """
    multiplica el conjunto o grupo de valores de una lista o tupla
    
    Parameters:
    valores: Lista o tupla con los valores a suamr
    
    Returns:
    multiplica de los valores en la lista o tupla.
    """
    if isinstance(valores, (list, tuple)):
        if len(valores):
            #empezamos por 1 ya que cualquier numero multiplicado por 0 dara 0
            acumulador = 1
            
            for v in valores:
                acumulador *= v
                
            return acumulador
        else:
            return None
    else:
        raise ValueError('Ha pasado con que no es lista ni tupla.')
    
edades = [19, 29, 31, 21]
try:
    resultado = multiplicar(edades)
    print(f'El resultado de la multiplicacion es: {resultado}')
except ValueError as e:
    print("ERROR:", e)


precios = (999.9, 59.9, 27.5)
try:
    resultado = multiplicar(precios)
    print(f'El resultado de la multiplicacion es: {resultado}')
except ValueError as e:
    print("ERROR:", e)


numeros = 1000
try:
    resultado = multiplicar(numeros)
    print(f'El resultado de la multiplicacion es: {resultado}')
except ValueError as e:
    print("ERROR:", e)
    

numero = []
try:
    resultado = multiplicar(numero)
    if resultado:
        print(f'El resultado de la multiplicacion es: {resultado}')
    else:
        print("No ha proveido datos par ala lista o tupla. Esta vacia.")
except ValueError as e:
    print("ERROR:", e)























