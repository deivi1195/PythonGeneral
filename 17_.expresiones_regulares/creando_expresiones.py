import re

#detectando un numero CABA y ocultandolo

texto = "hola Pedro, mi numero es: +54 11 4321-4321"

#el guion - no lo toma como caracter espacial por lo tanto puede buscarse sin la barra invertida (\-)
#si el guion estuviera entre corchetes si habria que validarlo
pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

reemplazo = re.sub(pattern,"(Numero Oculto)", texto)

print(reemplazo)















