#creando diccionarios con dict()
#para crear un diccionario vacio se utiliza la funcion en este caso dict()
diccionario = dict(nombre="lucas",apellidos="dalto")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["dalto","pablo"]):"jajaja"}

#creando diccionarios con fromkeys()
#itera el primer elemento osea lo que coloques en la parte de la key
diccionario = dict.fromkeys(["nombre","apellido"])

#creando un diccionario iterando las keys con una cadena e texto
#dict.fromkeys(DATO_ITERABLE(KEY),LO_QUE_VAMOS_A_IGUALAR(VALOR)(POR DEFECTO ES NONE))
diccionario = dict.fromkeys("ADCBE")



print(diccionario)
























