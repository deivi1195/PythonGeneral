# a traves de una funcion validar si un numero se halla en un rango.

def valor_en_rango(valor, rango):
    """
    Comprueba si un valor dado se halla enn un rango especifico.
    
    Parameters:
    valor: valor a verificar
    rango: Rango de valores
    
    Returns:
    True: si el valor se halla en el rango
    False: en caso contrario
    """
    if isinstance(valor, (int,float)):
        if isinstance(rango, (list, tuple)):
            if len(rango) == 2:
                inicio = rango[0]
                fin = rango[1]
                
                if inicio < fin:
                    return valor in range(inicio, fin + 1)
                    # tambien se puede hacer de esta forma por que el * abarca todos los valores que se encuentre en el rango
                    #return valor in range(*rango)
                
                raise ValueError("El rango debe estar compuesto por dos numeros, el primero debe ser menos al segundo.")
            
            raise Exception('El rango debe tener exactamente dos elementos.')
        
        raise TypeError('Ha especificado un tipo de valor invalido para el argumento `rango`. Debe se una lista o tupla.')
    else:
        raise TypeError('Ha especificado un tipo de valor invalido para el argumento `valor`. Debe ser un entero o real.')
        

numero = 5
rango = [0, 10]

try:
    resultado = valor_en_rango(numero, rango)
    print(f'El valor {numero} se halla en el rango {rango}? {resultado}')
except Exception as e:
    print("ERROR:", e)

numero = 5
rango = [10, 0]

try:
    resultado = valor_en_rango(numero, rango)
    print(f'El valor {numero} se halla en el rango {rango}? {resultado}')
except Exception as e:
    print("\nERROR:", e)















