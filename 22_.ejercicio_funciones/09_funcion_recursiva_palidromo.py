# crear una funcion recursiva para comporbar si una cadena es palindromo

# oso => oso
# ana => ana
# lateleletal => lateleletal
# correa => aerroc (no es palindromo)

def es_palindromo(palabra):
    """
    Determinar si una palabra es palindromo
    
    Parameters:
    Palabra: palabra sobre la que se realiza la comprobacion.
    
    Returns:
    True si la palabra es palindromo, False en caso contrario.
    """
    if len(palabra) < 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        False

print(f'oso es palindromo?: {es_palindromo("oso")}')
print(f'oso es palindromo?: {es_palindromo("lateleletal")}')
print(f'oso es palindromo?: {es_palindromo("perro")}')








