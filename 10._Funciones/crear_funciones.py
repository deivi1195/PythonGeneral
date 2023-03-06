
'''#creando una funcion simple
def saludar():
    print("Hola lucas, como andas?")

#ejecutando la funcion simple
saludar()'''

#crear una funcion que tenga parametros
def saludar(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = "reina"
    elif (sexo == 'hombre'):
        adjetivo = 'titan'
    else:
        adjetivo = 'amor'
        
    print(f'Hola {nombre}, mi {adjetivo} como andas?')
    
saludar("camila","Mujer")
saludar("Dalto","Hombre")
saludar("Fran","no binario")

'''
#crear una funcion que nos retorne multiples valores
def crear_contrasena_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena

password = crear_contrasena_random(90)
frase = f'Tu contrasena nueva es: {password}'
print(frase)'''

#crear una funcion que nos retorne multiples valores
def crear_contrasena_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasena,num #retorna un tupla

#desempaquetando la funcion
password,primer_numero = crear_contrasena_random(90)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlos
print(f'Tu contrasena nueva es: {password}')
print(f'El numero utilizado para crearla fue: {primer_numero}')




























