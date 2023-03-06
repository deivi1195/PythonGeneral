#1 alumno es profesor - 1 Alumno es asistente
# A) Pedir la edad de los compa;eros que vinieron hoy a clase y ordenar los datos
# de menor a mayor
# B) El mayor es el profesor y el menor es el asistente: Quien es quien?

#funcion para obtener al sistente y al profesor segun la edad
def obtener_companeros(cantidad_de_companeros):
    
    #creando la lista con los companeros
    companeros = []
    
    #ejecutando un for para pedir informacion de cada compa;ero
    for i in range(cantidad_de_companeros):
        nombre = input("ingrese el nombre del compa;ero: ")
        edad = int(input("ingrese la edad del compa;ero: "))
        companero = (nombre,edad)
        
        #agregando la informacion a la lista
        companeros.append(companero)
        
    #ordenandolos de menor a mayor segun su edad
    companeros.sort(key=lambda x:x[1])
    
    #compa;ero[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = companeros[0][0]
    profesor = companeros[-1][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_companeros(5)

#mostrando el resultado
print(f'El profesor es: {profesor} y su asistente es: {asistente}')

























