# Remover valores duplicados

numeros = [1, 2, 3, 1, 1, 1, 1, 4, 5, 6, 3, 3, 2, 5]

print(f'Contenido actual de la lista `numeros`: {numeros}')
print(f'Cantidad actual de la lista `numeros`: {len(numeros)}\n')


#solucion 1

numeros_sin_repetir = []

for n in numeros:
    if n not in numeros_sin_repetir:
        numeros_sin_repetir.append(n)
        
print(f'Contenido actual de la lista `numeros_sin_repetir`: {numeros_sin_repetir}')
print(f'Cantidad actual de la lista `numeros_sin_repetir`: {len(numeros_sin_repetir)}\n')
        
#solucion 2:
#convirtiendo la lista a conjunto , ya que en un conjunto no se pueden repetir valores

numeros_conjunto = list(set(numeros))


print(numeros_conjunto)
 





