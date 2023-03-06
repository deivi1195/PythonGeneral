import re

text = "Este es un ejemplo de una página web: https://proyectodalto.com y también podemos visitar http://example.org"

#https? signo de pregunta = si encuentras https muestralo si no, igual muestralo, es decir puede ser https o http
#? = encontrar 0 o 1 conicidencias, pero no mas de 1
# tiene que haber ://
# [a-zA-Z0-9.-]+ tiene que haber una vez o mas todo loq eu esta entre corchetes
# tiene que haber un "." (\.)
# buscando valores de la a-zA-Z (mayus y minus) al menos dos veces {2,} {dos letras, ilimitadas letras}
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)


