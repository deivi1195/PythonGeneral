# Error al intentar acceder a un atributo inexsistente en una clase

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

computador = Producto(1001, 'Computador', 799)

print('Codigo:', computador.codigo)
print('nombre:', computador.nombre)
print('precio:', computador.precio)

try:
    print('Cantidad', computador.cantidad)
except AttributeError as e:
    print('Se esta tratando de acceder a una propiedad/atributo inexistente')
    print("ERROR", e)









