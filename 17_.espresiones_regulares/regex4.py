import re

#validando correos electronicos
email = "deivigonzaleznuevogmail@gmail.com"

#[a-zA-Z0-9._%+-] pueden ser validos de la a-z (a-z) de la A-Z (A-Z) del 0-9 (0-9) 
# todo los que no sea un espacio en linea (.) 
# los guiones bajos tambien estan permitidos (_) 
# todo lo que encuentre ante y despues de lo valida (%(comodin)) 
# buscar 1 o mas coincidencias (+) 
# los guionas tambien estan permitidos (-) 
#[a-zA-Z0-9._%+-]+ encuentra al menos alguna vez alguno de los caracteres que aparecen detras del + (+)
# los arrobas estan permitidos (@)
# [a-zA-Z0-9.-]+ lo mismo de arriba solamente que saco el porcentaje %
# buscando un punto (\.)
# buscando valores de la a-zA-Z (mayus y minus) al menos dos veces {2,} {dos letras, ilimitadas letras}
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#re.match(encontrar el patron, en la variable "email")
result = re.match(pattern, email)

#validar el resultado
if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")