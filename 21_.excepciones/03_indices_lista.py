# Gestion de excepciones para acceso a elementos de una lista:

lenguajes = ['Python', 'JavaScript', 'PHP', 'C#', 'C++', 'Java']

print(f'Cantidad de elementos de la lista `lenguajes`: {len(lenguajes)}')
print(f'Primer elemento de la lista `lenguajes`: {lenguajes[0]}\n')

indice = 6

try:
    print(f'Primer elemento de la lista `lenguajes`: {lenguajes[indice]}')
except IndexError:
    print(f'El indice {indice} no existe en la lista `lenguajes`')
    
print('El programa ha finalizado.')














