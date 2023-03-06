#Expresiones lambda - Funciones anonimas

def sumar(a, b):
    resultado = a + b
    return resultado

x = 2
y = 3

print(f'La suma de {x} + {y} es igual a {sumar(x, y)}')


#lambda [parametros]: [operacion con los parametros anteriores(return)]
#Solo se puede escribir una unica instruccion
sumar_lambda = lambda a, b: a + b
print(f'La suma de {x} + {y} es igual a {sumar_lambda(x, y)}\n')


def cuadrado(n):
    return n ** 2

cuadrado_lambda = lambda n: n ** 2 

numero = 10

print(f'El cuadrado de {numero} es igual a {cuadrado(numero)}')
print(f'El cuadrado de {numero} es igual a {cuadrado_lambda(numero)}\n')



# Filtrar el contenido de una lista

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'Contenido de la variable numeros: {numeros}')
print(f'Cantidad de la variable numeros: {len(numeros)}\n')

def extraer_impares(lista):
    impares = []
    
    for i in lista:
        if i % 2 != 0:
            impares.append(i)
        
    return impares

resultado = extraer_impares(numeros)       

print(f'Contenido de la lista resultado(impares): {resultado}')
print(f'Cantidad de la lista resultado(impares): {len(resultado)}\n')

#Lista de comprension
resultado = [n for n in numeros if n % 2 != 0]
print(f'Contenido de la lista resultado(impares): {resultado}')
print(f'Cantidad de la lista resultado(impares): {len(resultado)}\n')


#No se puede usar len() en filter() 
#asi que le pasamos filter como lista list(filter())
resultado = list(filter(lambda n: n % 2 != 0, numeros))
print(f'Contenido de la lista resultado(impares): {resultado}')
print(f'Cantidad de la lista resultado(impares): {len(resultado)}\n')


# para la funcion filter tambien podemos especificar una funcion nombrada

def filtro(n):
    return n % 2 != 0


#lambda significa funcion anonima
#aqui abajo en el primer parametro de filter() le pasamos una funcion con nombre filtro
# la funcion filtro tiene su propia expresion
resultado = list(filter(filtro, numeros))
print(f'Contenido de la lista resultado(impares): {resultado}')
print(f'Cantidad de la lista resultado(impares): {len(resultado)}\n')


#Obtener el cuadrado de cada numero de la lista numeros
# Utilizar la funcion map() para crear un mapeo (mapping) del contenido de una lista (iterable)

def elevar_cuadrado(lista):
    cuadrados = []
    
    for n in lista:
        cuadrados.append(n ** 2)

    return cuadrados

resultado = elevar_cuadrado(numeros)
print(f'Contenido de la variable numeros: {numeros}')
print(f'Todos los numeros de la lista al cuadrado: {resultado}\n')

#lista de comprension

resultado = [n**2 for n in numeros]
print(f'Todos los numeros de la lista al cuadrado: {resultado}\n')

#Funcion map()

resultado = list(map(lambda n: n ** 2, numeros))
print(f'Todos los numeros de la lista al cuadrado: {resultado}\n')





