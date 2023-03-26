import re

text = "remplazando todas las vocales por asteriscos"

#buscamos todas las vocales [aeiou] puenden ser separadas o juntas
#si buscamos sin corchetes [] si tiene que encontrar aeiou juntas
new_text = re.sub("[aeiou]", "*", text)

print(new_text)