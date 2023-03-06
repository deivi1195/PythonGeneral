# Excepciones en flujo de ejecucion de un programa Python


try:
    numero = int(input('Escriba un numero entero: '))
    
    print(f'Contenido de la variable numero: {numero}')
    print(f'El tipo de dato de la variable numero es: {type(numero)}')

except ValueError as e:
    print(f'ERROR: {e}\n')


print('El programa ha terminado\n')

# Captura segura de un numero entero
print('Captura segura de un numero entero')

while True:
    try:
        edad = int(input('Escriba su edad: '))

        if edad > 0:
            if edad <= 70:
                break
            else:
                print('MENSAJE: La edad debe ser menor a 70 a;os')
        else:
            print('MENSAJE: Escriba un numero positivo')
    except:
        print('MENSAJE: No ha escrito un valor valido. Intente de nuevo.\n')
        
print(f'Su edad es: {edad} a;os.\nEl Programa ha terminado.')        







