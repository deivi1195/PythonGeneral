# Tomar una lista de numeros e identificar los numeros unicos.

#se puede hacer de esta forma corta pasando la lista o tupla a set() y se eliminan los valores duplicados
# def numeros_unicos(numeros):
#     if isinstance(numeros, (tuple, list)):
#         numeros = set(numeros)
#         numeros_unicos = numeros
        
#         return list(numeros_unicos)
    
#     raise TypeError('El argumento `numeros` debe ser una lista o una tupla.')

def numeros_unicos(numeros):
    
    if isinstance(numeros, (tuple, list)):
        """
        Obtiene los numeros unicos en una tupla o lista
        
        Parameters:
        numeros: lista o tupla con numeros.
        
        Returns:
        Lista con los valores unicos.
        """
        unicos = []
        
        for n in numeros:
            if n not in unicos:
                unicos.append(n)
                
        return unicos
    
    raise TypeError('El argumento `numeros` debe ser una lista o una tupla.')


valores = [2, 5, 2, 2, 2, 3, 7, 5 ,7, 11, 13]
print(f'El contenido de la lista `valores` es: {valores}')
print(f'Cantidad de elementos de la lista `valores` es: {len(valores)}')

try:
    resultado = numeros_unicos(valores)
    print(f'\nEl contenido de la lista `resultado` es: {resultado}')
    print(f'Cantidad de elementos de la lista `resultado` es: {len(resultado)}')
except TypeError as e:
    print('\nERROR:', e)    


#salta error por que valores tiene un texto
valores = '[2, 5, 2, 2, 2, 3, 7, 5 ,7, 11, 13]'
print(f'El contenido de la lista `valores` es: {valores}')
print(f'Cantidad de elementos de la lista `valores` es: {len(valores)}')

try:
    resultado = numeros_unicos(valores)
    print(f'\nEl contenido de la lista `resultado` es: {resultado}')
    print(f'Cantidad de elementos de la lista `resultado` es: {len(resultado)}')
except TypeError as e:
    print('\nERROR:', e)












