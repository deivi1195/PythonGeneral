#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros    
        a = input("numero 1: ")
        b = input("numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("no escribiste un numero, vuelve a intentar escribir un numero")
            #aqui mostramos exactamente el nombre del error
            print(f'ERROR: {e}')        
        #si todo salio bien terminamos el bucle
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")
            
    #mostrando el resultado        
    return resultado

print(sumar_dos())






















