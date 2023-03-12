def dividir(dividendo, divisor):
    """
    Calcula la division de dos numeros
    
    Parameters:
    dividendo: Dividendo de la division.
    divisor: Divisor de la division.
    
    Returns:
    Division entre dividendo y divisor.
    """
    if divisor == 0:
        raise ZeroDivisionError('El divisor no puede ser cero.')
    elif dividendo == divisor:
        return 1
    #cuando la division es entera y no real.
    elif dividendo < divisor:
        return 0
    else:
        return 1 + dividir(dividendo - divisor, divisor)
        
print(f'{5}/{2} = {dividir(5, 2)}')
print(f'{1}/{2} = {dividir(1, 2)}')

try:
    print(f'{5}/{0} = {dividir(5, 0)}')
except ZeroDivisionError as e:
    print('ERROR:', e)














