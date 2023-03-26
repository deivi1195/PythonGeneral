# creacion de objetos (instanciacion):
from modelos.carro import Carro
from modelos.camion import Camion


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
    
    print()
    
    #Creacion/instanciacion de un objeto Camion:
    
    camion_carga = Camion('SBD-456', 'Scania', 2015, 'China', 2000)
    
    print(f'El tipo de dato de la variable `camion_carga` es: {type(camion_carga)}')
    
    print(f'Placa: {camion_carga.placa}')
    print(f'Marca: {camion_carga.marca}')
    print(f'Modelo: {camion_carga.modelo}')
    print(f'Pais Procedencia: {camion_carga.pais_procedencia}')
    print('Encendido?: ', 'Si' if camion_carga.estado else 'No')
    print(f'Capacidad de carga (kg): {camion_carga.capacidad_carga}')
    
    print()
    
    camion_carga.encender()
    
    print('Encendido?: ', 'Si' if camion_carga.estado else 'No')
    
    camion_carga.apagar()
    
    print('Encendido?: ', 'Si' if camion_carga.estado else 'No')
    
    camion_carga.cargarMercancia()
    camion_carga.descargarMercancia()
    
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    main()



