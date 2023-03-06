# Creacion de una clase personalizada

class ValorMinimoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return f'ValorMinimoError: {self.message}' 
        else:
            return 'Se ha generado el error ValorMinimoError'   

class ValorMaximoError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self):
        if self.message:
            return f'ValorMaximoError: {self.message}' 
        else:
            return 'Se ha generado el error ValorMaximoError'


minimo = 10
maximo = 20

while True:
    try:
        numero = int(input(f'Escriba un numero entre {minimo} y {maximo}: '))
        
        if numero < minimo:
            raise ValorMinimoError(f'Ha escrito un valor menor a {minimo}.')
        elif numero > maximo:
            raise ValorMaximoError(f'Ha escrito un valor mayor a {maximo}')
        
        print(f'Ha escrito un valor entero valido.\n')
        
        break
    except ValueError:
        print('Debe escribir un valor entero valido.\n')
    except ValorMinimoError as e:
        print('ERROR:\n', e)
    except ValorMaximoError as e:
        print('ERROR:\n', e)







