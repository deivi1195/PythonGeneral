
#Creando una funcion de 3 parametros
def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido}, eres un {adjetivo}'

#utilizando keyword arguments
#frase_resultante = frase("Lucas", "Dalto", "Capo")
frase_resultante = frase(adjetivo = "Capo", apellido = "Dalto", nombre =  "Lucas")

print(frase_resultante)

#Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo = "Tonto"):
    return f'Hola {nombre} {apellido}, eres un {adjetivo}'

frase_resultante2 = frase("Lucas", "Dalto", "Inteligente")

print(frase_resultante2)
















