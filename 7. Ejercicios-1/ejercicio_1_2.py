#Le pedimos al usuario que nos diga una frase (o varias)
frase = input("Escribe una frase y te calculo cuanto tardarias si tuvieras que decirlo: ")

#Creamos una lista con todas las palabras de la frase(se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split(" ")

#Usamos len() para ver la cantidad de elementos que hay en la lista
cantidad_de_palabras = len(palabras_separadas)

#En caso de que tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("No te pedi un testamento")

#Calculamos cuanto tardaria en decir las palabras y se lo decimos    
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo.")
print(f"Dalto lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos")    


print(palabras_separadas)

















