def main():
    #creacion de un archivo de texto plano
    nombre_archivo = '25._Manipulacion_de_archivos/paises.txt'

    #utf-8 sirve para poder escribir con tildes y otros caracteres
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write('Colombia')
        f.write('\n')
        f.write('Ecuador')
        f.write('\n')
        f.write('Argentina')
        f.write('\n')
        f.write('Alemania')
        f.write('\n')
        f.write('Perú')
        f.write('\n')
        f.write('Italia')
        f.write('\n')
        f.write('Rusia')


if __name__ == '__main__':
    main()


