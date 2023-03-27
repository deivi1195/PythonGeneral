from modelos.rectangulo import Rectangulo
from modelos.triangulo import Triangulo
from modelos.circulo import Circulo

def main():
    # Prueba de ejecucion sobre la jerarquia de herencia de figuras - Polimorfismo
    print('Prueba de ejecucion sobre la jerarquia de herencia de figuras - Polimorfismo')

    figuras = []
    
    #todos estos objetos son de tipo figura
    rectangulo_rojo = Rectangulo('Rojo', 'Negro', 10, 5)
    
    circulo_verde = Circulo('Verde', 'Negro', 5)
    
    triangulo_negro = Triangulo('Negro', 'Gris', 7, 10)
    
    figuras.append(rectangulo_rojo)
    figuras.append(circulo_verde)
    figuras.append(triangulo_negro)
    
    print()
    
    print('El area de todas las figuras')
    
    for f in figuras:
        f.dibujar()
        
        area = f.area()
        print(f'El area es igual a {area} u^2')
        
        print()

    print()
    
    # Demostracion de sobreescritura de metodos
    print('Demostracion de sobreescritura de metodos')

    print(rectangulo_rojo)

    print()
    
    print(circulo_verde)
    
    print()
    
    print(triangulo_negro)



if __name__ == '__main__':
    main()









