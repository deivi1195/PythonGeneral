# Lista de variable de argumentos de una funcion
print('Lista de variable de argumentos de una funcion')

# def sumar(a, b):
#     return a + b

# def sumar(a, b, c):
#     return a + b + c

# def sumar(a, b, c, d):
#     return a + b + c + d

# def sumar(a, b, c, d, e):
#     return a + b + c + d + e

#Todas estas funciones se pueden hacer en una sola

# *valores = pueden ser 0 o mas argumentos (n cantidad de argumentos)
# se pueden iterar
def sumar(*valores):
    suma = 0
    
    for v in valores:
        suma += v
        
    return suma

resultado = sumar(1) #cantidad de argumentos que se especifico con *valores
print(f'El resultado de la suma es igual: {resultado}')

resultado = sumar(1, 2) #cantidad de argumentos que se especifico con *valores
print(f'El resultado de la suma es igual: {resultado}')

resultado = sumar(1, 2, 3) #cantidad de argumentos que se especifico con *valores
print(f'El resultado de la suma es igual: {resultado}')

