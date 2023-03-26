import re

# La cadena en la que se buscarán los patrones
text = "La fecha es 23/06/2021 y el teléfono es +1-555-555-5555"

# El patrón a buscar
#2 veces un numero (\d{2}) - una barra / (/) - 2 veces un numero (\d{2}) - una barra - 4 veces un numero (\d{2})
pattern = r"\d{2}/\d{2}/\d{4}"

# El texto con el que se reemplazará el patrón
replacement = "Fecha oculta"

# Reemplazar todas las apariciones del patrón en la cadena de texto
#sub lo que haces es encuentra una cadena y hace un reemplazo
#(pattern, replacement, text) -> (encontramos un patron, 
# reemplazamos el patron por lo que este en la variable "replacement", 
# todo eso sucede en el "Texto")
new_text = re.sub(pattern, replacement, text)

# Imprimir el resultado
print("Texto modificado:", new_text)