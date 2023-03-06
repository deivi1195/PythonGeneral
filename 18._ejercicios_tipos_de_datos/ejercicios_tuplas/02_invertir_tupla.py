# Invertir el contenido de una tupla

numeros = (1,2,3,4,5,6,7,8,9,10)

#solucion 1
print("Solucion 1: ")
print(numeros[::-1])

#solucion 2
print("Solucion 2: ")
numeros_invertidos = []

for i in range(len(numeros) - 1, -1, -1):
    numeros_invertidos.append(numeros[i])

numeros_invertidos = tuple(numeros_invertidos)
print(numeros_invertidos)

#solucion 3
print("Solucion 3: ")
numeros_invertidos_2 = tuple(reversed(numeros))

print(numeros_invertidos_2)



