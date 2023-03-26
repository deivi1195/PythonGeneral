import os

def main():
    # Operaciones adicionales sobre archivos:
    
    print('Renombrar un archivo')
    
    nombre_archivo = '25._Manipulacion_de_archivos/archivo.txt'
    
    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.')
    else:
        print(f'El archivo {nombre_archivo} no esxiste en disco.')

    print()
    
    print('Cambiar el nombre de un archivo')
    
    os.rename(nombre_archivo, '25._Manipulacion_de_archivos/archivo2.txt')

    if os.path.isfile(nombre_archivo):
        print(f'El archivo {nombre_archivo} existe en disco.')
    else:
        print(f'El archivo {nombre_archivo} no esxiste en disco.')



if __name__ == '__main__':
    main()
    
    print('Fin del programa.')
    
    
    