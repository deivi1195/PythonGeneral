# creacion de objetos (instanciacion):
from modelos.carro import Carro
from modelos.camion import Camion
from modelos.deportivo import Deportivo
from modelos.volqueta import Volqueta
from modelos.formula1 import Formula1


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
    
    # Creacion/instanciacion de un objeto Camion:
    print('Creacion/instanciacion de un objeto Camion:')
    
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
    
    print()
    
    # Creacion/instanciacion de un objeto Deportivo:
    print('Creacion/instanciacion de un objeto Deportivo:')
    
    deportivo_lujo = Deportivo('DEF-789', 'Audi', '2013', 'Alemania', 'Marca rines', 'Deportivo')
    
    print(f'El tipo de dato de la variable `deportivo_lujo` es: {type(deportivo_lujo)}')
    
    print(f'Placa: {deportivo_lujo.placa}')
    print(f'Marca: {deportivo_lujo.marca}')
    print(f'Modelo: {deportivo_lujo.modelo}')
    print(f'Pais Procedencia: {deportivo_lujo.pais_procedencia}')
    print('Encendido?: ', 'Si' if deportivo_lujo.estado else 'No')
    print(f'Marca de rines: {deportivo_lujo.marca_rines}')
    print(f'Tipo de carro: {deportivo_lujo.tipo}')
    
    print()
    
    deportivo_lujo.encender()
    
    print('Encendido?: ', 'Si' if camion_carga.estado else 'No')
    
    deportivo_lujo.abrir_puertas()
    deportivo_lujo.cerrar_puertas()
    
    print()
    
    deportivo_lujo.acelerar()
    deportivo_lujo.acelerar()
    
    deportivo_lujo.frenar()
    
    print()
    
    # Creacion/instanciacion de un objeto Volqueta:
    print('Creacion/instanciacion de un objeto Volqueta:')
    
    volqueta_carga = Volqueta('FGH-951', 'Dawewoo', 2014, 'Taiwan', 4000, 2000000)
    
    print(f'El tipo de dato de la variable `volqueta_carga` es: {type(volqueta_carga)}')
    
    print(f'Placa: {volqueta_carga.placa}')
    print(f'Marca: {volqueta_carga.marca}')
    print(f'Modelo: {volqueta_carga.modelo}')
    print(f'Pais Procedencia: {volqueta_carga.pais_procedencia}')
    print('Encendido?: ', 'Si' if volqueta_carga.estado else 'No')
    print(f'Capacidad de carga: {volqueta_carga.capacidad_carga}')
    print(f'Costo de servicio: {volqueta_carga.costo_servicio}')
    
    print()
    
    volqueta_carga.encender()
    
    print('Encendido?: ', 'Si' if volqueta_carga.estado else 'No')
    
    volqueta_carga.cargar_material()
    volqueta_carga.descargar_material()
    
    print()
    
    volqueta_carga.acelerar()
    volqueta_carga.frenar()
    
    volqueta_carga.apagar()
    
    print('Encendido?: ', 'Si' if volqueta_carga.estado else 'No')
    
    # Creacion/instanciacion de un objeto Formula1:
    print('Creacion/instanciacion de un objeto Formula1:')
    
    auto_formula1 = Formula1('F11-458', 'BMW', 2019, 'Alemania', 120)
    
    print(f'El tipo de dato de la variable `volqueta_carga` es: {type(auto_formula1)}')
    
    print(f'Placa: {auto_formula1.placa}')
    print(f'Marca: {auto_formula1.marca}')
    print(f'Modelo: {auto_formula1.modelo}')
    print(f'Pais Procedencia: {auto_formula1.pais_procedencia}')
    print('Encendido?: ', 'Si' if auto_formula1.estado else 'No')
    print(f'Peso del auto (kg): {auto_formula1.peso}')
    
    print()
    
    auto_formula1.encender()
    
    print('Encendido?: ', 'Si' if auto_formula1.estado else 'No')
    
    auto_formula1.competir()
    
    print()
    
    auto_formula1.acelerar()
    auto_formula1.frenar()
    
    print()
    
    auto_formula1.apagar()
    
    print('Encendido?: ', 'Si' if auto_formula1.estado else 'No')
    
    
    print()
    
    #iterar por cada uno de los objetos carro que se crearon:
    print('iterar por cada uno de los objetos carro que se crearon:')
    
    carros = [camion_carga, deportivo_lujo, volqueta_carga, auto_formula1]
    
    for c in carros:
        print(f'Placa: {c.placa}')
        print(f'Marca: {c.marca}')
        print(f'Modelo: {c.modelo}')
        print(f'Pais Procedencia: {c.pais_procedencia}')
        print('Encendido?: ', 'Si' if c.estado else 'No')
    
        c. encender()
        print('Encendido?: ', 'Si' if c.estado else 'No')
        
        c.acelerar()
        c.frenar()
        c.apagar()
    
    
    

if __name__ == '__main__':
    main()



