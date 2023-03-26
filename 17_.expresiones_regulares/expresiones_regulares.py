import re

texto = '''Hola master, esta es la cadena. 1. , como estas master"
Esta es la linea 224 de textobbbb.
y esta es la  finabbbl (linea 3) definitivabbbb.'''

resultado = re.search("Esta",texto)
#flags=re.IGNORECASE = devuelve todo sin importar las mayusculas y las minusculas
#haciendo una busqueda simple
resultado2 = re.findall("esta",texto)

#\D -> busca TODO MENOS digitos numericos
resultado3 = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado4 = re.findall(r"\w",texto)

#\W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado5 = re.findall(r"\W",texto)

#\s -> busca espacios en blanco -> espacios, tabulaciones, saltos de linea
resultado6 = re.findall(r"\s",texto)

#\S -> busca TODO MENOS espacios en blanco -> espacios, tabulaciones, saltos de linea
resultado7 = re.findall(r"\S",texto)

#. -> busca TODO MENOS saltos de linea
resultado8 = re.findall(r".",texto)

#. -> busca TODO MENOS saltos de linea
resultado8 = re.findall(r".",texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado9 = re.findall(r"\.",texto)

#armando una cadena que busque un numero seguido seguido de un punto y un espacio
resultado10 = re.findall(r'\d\.\s',texto)

#^ -> busca el comienzo de una linea
#se usa en conjunto Ej. ^Hola = Hola si esta al principio del texto
#^maestro = no esta al principio del texto, por lo tanto no te devuelve nada
#flags=re.M = hace que el texto se convierta en multileneas (cada linea tiene un principio)
#usandolo ^ y flags=re.M cada principio de linea cuenta 
resultado11 = re.findall(r'^Hola',texto)

#aqui funciona ^Esta como principio de linea usando flags=re.M
resultado12 = re.findall(r'^Esta',texto,flags=re.M)

#$ -> busca el final de una linea - se coloca $ al final de lo que se quiera buscar
resultado13 = re.findall(r'definitiva.$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
#Ej. busca 3 numeros juntos(\d{3}) y un espacio (\s)
resultado14 = re.findall(r'\d{3}\s',texto)

#{n,m} -> al menos n, como maximo m
resultado15 = re.findall(r'\d{1,4}',texto)

#{n,m} -> al menos n, como maximo m
#sin corchetes [] ab primero busca texto que tenga ab o abbb despende del {}
resultado16 = re.findall(r'ab{1,4}',texto)

#{n,m} -> al menos n, como maximo m
#con corchetes [ab] primero busca texto que nos devuelve cualquiera de los valores:
#"aa","ab","ba","bb"
resultado17 = re.findall(r'[ab]{2}',texto)

# | -> busca una cosa o la otra
resultado17 = re.findall(r'\d{2,4}|Hola',texto)


print(resultado17)




















