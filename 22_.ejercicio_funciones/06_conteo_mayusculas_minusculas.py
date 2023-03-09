# usar una funcion para contar minusculas y mayusculas en una cadena

def contador_min_mayus(texto):
    """
    Cuenta la cantidad de mayusculas y minusculas que hay en el texto.
    
    Parameters:
    texto: Cadena de caracteres con el texto.
    
    Returns:
    Tupla con la cantidad de minusculas y mayusculas.
    """
    if isinstance(texto, str):
        minusculas = 0
        mayusculas = 0
        
        for c in texto:
            if c.isalpha():
                if c.islower():
                    minusculas += 1
                elif c.isupper():
                    mayusculas += 1
        
        return minusculas, mayusculas
    
    raise TypeError('El argumento debe ser una cadena de caracteres.')

frase = 'Python es TreMendo'

try:
    resultado = contador_min_mayus(frase)
    print(f'Cantidad minusculas: {resultado[0]}')
    print(f'Cantidad mayusculas: {resultado[1]}')
except TypeError as e:
    print("ERROR:", e)



















