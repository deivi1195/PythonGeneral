# creacion de objetos (instanciacion):
from modelos.carro import Carro


def main():
    carro_chevrolet = Carro('ABC-123', 'Chevrolet', 2010, 'Estados unidos')
    
    print(f'El tipo de dato de la variable carro es: {type(carro_chevrolet).__name__}')
    
    print(f'Placa: {carro_chevrolet.placa}')
    print(f'Marca: {carro_chevrolet.marca}')
    print(f'Modelo: {carro_chevrolet.modelo}')
    print(f'Pais Procedencia: {carro_chevrolet.pais_procedencia}')
    print('Encendido?: ', 'Si' if carro_chevrolet.estado else 'No')
    
    print()
    
    print('Invocacion de metodos de la instancia de la clase Carro:')
    
    carro_chevrolet.encender()
    
    print('Esta encendido?:', 'Si' if carro_chevrolet.estado else 'No')
    
    carro_chevrolet.apagar()
    
    print('Esta encendido?:', 'Si' if carro_chevrolet.estado else 'No')
    
    print()
    
    carro_chevrolet.acelerar()
    carro_chevrolet.frenar()
    
    carro_chevrolet.encender()
    
    carro_chevrolet.acelerar()
    carro_chevrolet.frenar()
    

if __name__ == '__main__':
    main()



