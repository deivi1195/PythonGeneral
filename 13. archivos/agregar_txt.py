'''con el permiso 'a' se pueden agregar los archivos'''

with open("archivos\\texto_de_dalto.txt",'a',encoding="UTF-8") as archivo:
    
    #agregando el archivo
    #archivo.write("jajajaj hola")
    
    #agregando un espacio en blanco
    archivo.write("\n")
    #agregando parablas con un bucle
    for i in range(5):
        archivo.write(f"Linea {i+1} agregada\n")
    