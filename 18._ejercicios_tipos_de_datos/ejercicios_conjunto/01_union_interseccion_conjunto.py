# Realizar operaciones de union e interseccion de conjuntos

numeros = set(list(range(1, 11)))
primos = set([2, 3, 5, 7, 11, 13, 17, 19])

print(numeros)
print(primos)

union = numeros.union(primos)

print(union)

interseccion = primos.intersection(numeros)

print(interseccion)