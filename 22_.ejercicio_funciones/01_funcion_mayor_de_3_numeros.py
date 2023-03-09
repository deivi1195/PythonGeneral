# Funcion para obtener el mayor de 3 numeros


numeros = [13, 54, 23, 16]

def numero_mayor():
    mayor = numeros[0]
    
    for n in range(1, len(numeros)):
        if numeros[n] > mayor:
            mayor = numeros[n]

    
    if mayor == numeros[0] and mayor == numeros[-1]:
        return 'No hay nuemro mayor, todos los numeros son iguales.'
    else:
        return f'El numero mayor es: {mayor}'


resultado = numero_mayor()
print(resultado)
        
# otra forma de resolver dado variable con valores especificos(sin lista)

# a, b, c

def numero_mayor(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return None
    
x = 3
y = 3
z = 5

resultado = numero_mayor(x, y, z)
#print(f'El numero mayor entre {x} {y} {z} es: {resultado}')
if resultado:
    print(f'El numero mayor es: {resultado}')
else:
    print('No hay nuemro mayor, todos los numeros son iguales.')








