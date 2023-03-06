# Encontrar los tres valores mayores en un diccionario

from heapq import nlargest

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audifonos': 35.9, 'Monitor': 299}

#key=productos.get = queremos obtener los valores de cada una de las llaves
productos_mas_caros_3 = nlargest(3, productos, key=productos.get)

print(productos_mas_caros_3)

