# calcular la frecuencia (ocurrencias) de los elementos de una lista

from collections import Counter

numeros = [1, 2, 3, 1, 1, 1, 1, 4, 5, 6, 3, 3, 2, 5]
print(f'Contenido actual de la lista: {numeros}')


#solucion 1

frecuencia = {}

#recorremos cada elemento de numeros
for n in numeros:
    #si n esta en frecuencia entonces ese numero aumentara su valor en +1
    if n in frecuencia:
        frecuencia[n] += 1
    #si n no esta en frecuencia entonces ese numero se agrega a frecuencia
    else:
        frecuencia[n] = 1

print(frecuencia)

#solucion 2

contador = Counter(numeros)

print(contador)




