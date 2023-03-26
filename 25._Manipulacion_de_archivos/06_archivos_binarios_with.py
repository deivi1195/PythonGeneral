def main():
    # Creando un archivo binario y leyendo su estructura con with
    nombre_archivo = '25._Manipulacion_de_archivos/numeros.bin'
    
    # se crea el archivo binario
    print('Se esta creando un archivo binario...')
    with open(nombre_archivo, 'wb') as f:
    
        numeros = [2, 3, 5, 7, 11]        
        f.write(bytearray(numeros))
        
    print()
    
    print('este es el contenido del archivo binario `numeros.bin`')
    
    # se accede al contenido de ese archivo binario
    with open(nombre_archivo, 'rb') as f:
    
        numeros = list(f.read())
        
        print()
        
        print(numeros)
    
    print('El programa ha terminado.')

if __name__ == '__main__':
    main()
    