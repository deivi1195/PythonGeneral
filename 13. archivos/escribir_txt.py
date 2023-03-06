'''con el permiso de 'w' si no encuentra el archivo, lo crea'''

with open("archivos\\texto_de_dalto.txt",'w',encoding="UTF-8") as archivo:
    
    #sobreescribiendo el archivo sin guarda nada de lo que tenia
    #archivo.write("jajajaj hola")
    
    #el parametro es el proceso inverso a readlines()
    #al parametro hay que pasarle una lista
    archivo.writelines(["Hola maestro como andas\n", "misericordia\n"])
    
    #agregando otras 2 lineas
    archivo.writelines(["Muy bien master\n","y tu?"])