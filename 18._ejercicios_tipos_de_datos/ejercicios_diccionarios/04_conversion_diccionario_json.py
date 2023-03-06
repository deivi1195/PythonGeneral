# Convertir un diccionario en su representacion en el formato JSON

import json

productos = {'Mouse': 29.9, 'Teclado': 119.9, 'Audifonos': 35.9, 'Monitor': 299}

print(productos)
print(type(productos).__name__)

producto_json = json.dumps(productos)

print(producto_json)
print(type(producto_json).__name__)

