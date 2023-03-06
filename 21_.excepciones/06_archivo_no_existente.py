# Error al intentar acceder un archivo del sistema de almacenamiento:
print('Error al intentar acceder un archivo del sistema de almacenamiento')

nombre_archivo = 'python.txt'

try:
    with open(nombre_archivo, 'r') as f:
        #iterar por cada una de las lineas que tiene ese archivo
        for l in f.readlines():
            print(l)
except FileNotFoundError as e:
    print(f'ERROR: ', {e})
    








