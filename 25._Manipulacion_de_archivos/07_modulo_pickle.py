import pickle

def main():
    # uso del modulo pickle para serializar y des serealizar objetos python
    print('uso del modulo pickle para serializar y des serealizar objetos python')

    paises_capitales = {'Colombia': 'Bogota', 'Ecuador': 'Quito', 'Argentina': 'Buenos aires'}
    
    nombre_archivo = '25._Manipulacion_de_archivos/paises_capitales.pickle'
    
    with open(nombre_archivo, 'wb') as f:
        
        pickle.dump(paises_capitales, f)
        
    print()
    
    print('lectura del contenido de un archivo pickle:')
    
    with open(nombre_archivo, 'rb') as f:
        
        paises_capitales_recuperados = pickle.load(f)
        
        print('Tipo de dato de la variable `paises_capitales_recuperados`:', type(paises_capitales_recuperados))
        print('El contenido de la variable `paises_capitales_recuperados`:')
        print(paises_capitales_recuperados)
    
    print('El programa ha terminado.')






if __name__ == '__main__':
    main()
    