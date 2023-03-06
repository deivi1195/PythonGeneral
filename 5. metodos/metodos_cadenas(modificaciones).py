cadena1 = "Hola soy Deivi"
cadena2 = "Bienvenido maquina"

#EL METODO ES DATO.METODO(parametros)

#Convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayusculas
primer_letra_mayusc = cadena1.capitalize()

#buscando una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hay conicidencias lanza una excepcion
busqueda_index = cadena1.index("la soy")

#si es numerico, devolvemos True, si no devolvemos False
es_numerico = cadena1.isnumeric()

#si es alfanumero, devolvemos True, si no devolvemos False
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias\
contar_concidencias = cadena1.count("Hola")

#contamos cuantos caracteres tiene una cadena
#len() no es un metodo, es una funcion
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("vi")

#reemplaza un pedazo de una cadena dada por otra dada
#necesita dos parametros, el primer parametro pide lo que quieres reemplazar exactamente
#el segundo parametro pide con lo que quieras que sea reemplazado el primer parametro
cadena_nueva = cadena1.replace("Hola", "Bye")

#separar cadenas con la cadena que le pasemos
#nos devuelve una lista, con los elementos separados por el parametro asigando
cadena_separada = cadena1.split(" ") #en este ejemplo crea una lista con los elementos separados por espacios


print(cadena_separada)

