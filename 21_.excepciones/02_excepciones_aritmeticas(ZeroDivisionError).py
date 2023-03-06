# Gestion de excepciones en operaciones artimeticas - division:
print('Gestion de excepciones en operaciones artimeticas - division:')

# Captura del primer numero - dividendo

while True:
    try:
        dividendo = float(input('Escriba el dividendo: '))
        
        break
    except:
        print("MENSAJE: debe escribir un valor valido. Intente nuevamente.\n")

while True:
    try:
        divisor = float(input('Escriba el divisor: '))
        
        break
    except:
        print("MENSAJE: debe escribir un valor valido. Intente nuevamente.\n")    

try:
    division = dividendo / divisor

    print(f'El resultado de la division es: {division}')
except ZeroDivisionError as e:
    print(f'ERROR: {e}')
    print('MENSAJE: Intento de division entre cero.')













