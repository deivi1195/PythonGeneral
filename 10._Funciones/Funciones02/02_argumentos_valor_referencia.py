# Pasar argumentos por valor y por referencia
print('Pasar argumentos por valor y por referencia')

# 1. Pasar argumentos por valor
print('\nPasar argumentos por valor')

def duplicar(numero):
    numero *= 2 #numero = numero * 2
    print(f'El numero duplicado es igual a: {numero}')

x = 2
print(f'El valor de la variable `x` antes de su duplicacion: {x}')

duplicar(x)

print(f'El valor de la variable `x` despues de su duplicacion: {x}')


# 2. Pasar argumentos por referencia:
print('\nPasar argumentos por referencia')

def agregar_elemento(lista):
    lista.append(2)
    
numeros = [1]
print(f'Contenido de la variable numeros antes de invocar agregar_elemento: {numeros}')

agregar_elemento(numeros)

print(f'Contenido de la variable numeros despues de invocar agregar_elemento: {numeros}')









