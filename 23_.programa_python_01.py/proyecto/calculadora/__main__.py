from .funciones_aritmeticas import sumar, restar, multiplicar, dividir
#para compilarlo desde la consola se una el punto delante del modulo (dunciones aritemticas en este caso)
#se accede al directorio donde se encuentra el programa
# y se escribe "python -m 'nombre del programa'"

def menu():
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('0. Salir')

def main():
    while True:
        while True:
            menu()
            try:
                opcion = int(input('Escriba la opcion a ejecutar: '))
                break
            except ValueError as e:
                print("ERROR: Ha digitado un valor invalido")
        #salto de linea
        print()
        
        if opcion == 0:
            break
        
        if 1 <= opcion <= 4:
            while True:
                try:
                    numero_1 = int(input('Escriba el numero 1: '))
                    break
                except ValueError as e:
                    print("ERROR: Ha digitado un valor invalido")   
            while True:
                try:
                    numero_2 = int(input('Escriba el numero 2: '))
                    break
                except ValueError as e:
                    print("ERROR: Ha digitado un valor invalido") 
        print()
        
        if opcion == 1:
            resultado = sumar(numero_1, numero_2)
        elif opcion == 2:
            resultado = restar(numero_1, numero_2)
        elif opcion == 3:
            resultado = multiplicar(numero_1, numero_2)
        elif opcion == 4:
            try:
                resultado = dividir(numero_1, numero_2)
            except ZeroDivisionError as e:
                print('ERROR:', e)
                
        print(f"el resultado de la operacion es: {resultado}\n")

    print()

    print("El programa ha terminado.")

if __name__ == '__main__':
    main()

#


