# remover todos los elementos duplicados de un diccionario

productos = {1001: 'Mouse', 1002: 'Teclado', 1003: 'Monitor', 1004: 'Mouse', 1005: 'Audifonos', 1006: 'Teclado'}

print(productos)
print(len(productos))


productos_unicos = {}

for k, v in productos.items():
    #.values() pregunta por los valores
    if v not in productos_unicos.values():
        productos_unicos[k] = v

print(productos_unicos)
print(len(productos_unicos))
