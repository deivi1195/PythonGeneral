def main():
    # introduccion a la manipulacion de archivos de texto
    print('introduccion a la manipulacion de archivos de texto')

    print()

    #Apertura de un archivo de texto:
    print('apertura de un archivo de texto')

    nombre_archivo = '25._Manipulacion_de_archivos/lenguajes.txt'

    # 1. Apertura de archivo
    archivo = open(nombre_archivo, 'r')

    # 2. conjunto de tareas a realizar
    for l in archivo.readlines():
        print(l, end='')
        
    # 3. nos asegura que el arcchivo se cierre de forma apropiada
    archivo.close()  
    
    print()
    
    # Apertura de un archivo con un manejador de contexto  
    print('Apertura de un archivo con un manejador de contexto ') 
    nombre_archivo = '25._Manipulacion_de_archivos/lenguajes.txt'
    
    # manejador de contexto 'with' automatiza ciertas acciones como la de close
    with open(nombre_archivo, 'r') as f:
        for l in f.readlines():
            print(l, end='')
    
    
    

if __name__ == "__main__":
    main()











