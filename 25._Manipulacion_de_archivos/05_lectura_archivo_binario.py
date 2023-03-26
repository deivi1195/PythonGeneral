def main():
    # Lectura del contenido de un archivo binario.
    
    nombre_archivo = '25._Manipulacion_de_archivos/numeros.bin'
    
    archivo = open(nombre_archivo, 'rb')
    
    numeros = list(archivo.read())
    
    archivo.close()
    
    print()
    
    print(numeros)
    
    print('El programa ha terminado')

if __name__ == '__main__':
    main()