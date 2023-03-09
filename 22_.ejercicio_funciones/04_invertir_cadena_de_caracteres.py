# Crear una funcion para invertir el contenido de una cadena de caracteres.

#Python => nohtyP


def invertir_cadena(texto):
    cadena_invertida = texto[::-1]
    return cadena_invertida
    
cadena = "Python"
resultado = invertir_cadena(cadena)
print(f"Esta es la cadena de caracteres invertida: {resultado}")
    
#otra solucion
def invertir_cadena(texto):
    """
    Inviierte una cadena de caracteres
    
    Parameters:
    texto: cadena de caracteres a invertir
    
    Returns:
    cadena de caracteres invertida
    """
        
    if isinstance(texto, str):
        resultado = ''
        
        for i in range(len(texto) - 1, -1, -1):
            resultado += texto[i]
        
        return resultado
    else:
        raise TypeError('No se ha especificado una cadena de caracteres.')
    
frase = 'Python es tremendo!'
try:
    resultado = invertir_cadena(frase)
    print(f'Texto original: {frase}')
    print(f'Texto invertido: {resultado}')
except TypeError as e:
    print('ERROR:', e)

frase1 = 1000
try:
    resultado = invertir_cadena(frase1)
    print(f'\nTexto original: {frase1}')
    print(f'Texto invertido: {resultado}')
except TypeError as e:
    print('\nERROR:', e)

frase2 = ['P','y','t','h','o','n']
try:
    resultado = invertir_cadena(frase2)
    print(f'\nTexto original: {frase2}')
    print(f'Texto invertido: {resultado}')
except TypeError as e:
    print('\nERROR:', e)














