# Argumentos/parametros nombrados variables - keywords:
print('Argumentos/parametros nombrados variables - keywords:')

'''
**keywords = iteractuan como un diccionario con llave y valor ('key': value)
def mostrar_identidad(**identificacion):
    print(type(identificacion))
    print(identificacion)
    
mostrar_identidad()

#<class 'dict'>
#{}
'''
def mostrar_identidad(**identificacion):
    resultado = ''
    
    if identificacion.get('documento'):
        resultado += 'Documento: ' + identificacion.get('documento') + '\n'
    if identificacion.get('nombre'):
        resultado += 'Nombre: ' + identificacion.get('nombre') + '\n'
    if identificacion.get('apellido'):
        resultado += 'Apellido: ' + identificacion.get('apellido') + '\n'

    return resultado

persona = mostrar_identidad(nombre= 'Jhon', apellido= 'Ortiz', documento='V11.232.567')
print(f'Identificacion:\n{persona}')









