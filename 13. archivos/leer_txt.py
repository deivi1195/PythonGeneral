#usando open para abrir un archivo con una codificacion universal (UTF-8)
archivo = open("archivos\\texto_de_dalto.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo.read()

'''cuando un archivo se abre y se lee, no se puede volver a arbir 
hay que cerrarlo y volverlo a abrir'''

#leer linea por linea
#lineas = archivo.readlines()

#leer una sola linea
#el parametro de readline hace que lea tantos caracteres 
#como el numero que pongas en el parametro
linea = archivo.readline()

#cerrar el archivo
archivo.close()


print(archivo)


















