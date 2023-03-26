import json

def main():
    # Creacion de un archivo binario
    
    nombre_archivo = '25._Manipulacion_de_archivos/numeros.bin'
    
    # cuando se coloca wb significa que reescribes las cosas en binario
    archivo = open(nombre_archivo, 'wb')
    
    numeros = [2, 3, 5, 7, 11]
    
    archivo.write(bytearray(numeros))
    
    archivo.close()
    
    print('El programa ha temrinado.')

if __name__ == '__main__':
    main()
    