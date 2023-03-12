def sumar(a, b):
    """
    Suma dos numeros
    
    Parameters:
    a: Primer numero a sumar
    b: segundo numero a sumar
    
    Returns:
    Suma de los dos numeros
    """
    return a + b

def restar(a, b):
    """
    Resta dos numeros
    
    Parameters:
    a: Primer numero a restar
    b: segundo numero a restar
    
    Returns:
    Resta de los dos numeros
    """
    return a - b

def multiplicar(a, b):
    """
    multiplica dos numeros
    
    Parameters:
    a: Primer numero a multiplicar
    b: segundo numero a multiplicar
    
    Returns:
    multiplica de los dos numeros
    """
    return a * b

def dividir(a, b):
    """
    divide dos numeros
    
    Parameters:
    a: Primer numero a dividir (dividendo)
    b: segundo numero a dividir (divisor)
    
    Returns:
    divide de los dos numeros
    """
    if b != 0:
        return a / b
    
    raise ZeroDivisionError('Esta intendtando dividir entre cero.')











