#2 listas, una con nombres otra con apellidos
nombres = ["Lucas", "Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robetix","Tarado"]

#registrar esta informacion en un TXT de forma optima
#IMPORTANTE A LA HORA DE HACER EL BUCLE(FOR) ENCERRAR LA SENTENCIA EN UNA LISTA []
#pasandole la ruta, crea voy el archivo en esa ruta si no crea el archivo fuera de todo
with open("14._archivos_problemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los Datos son:\n\n")
    [arch.writelines(f"nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]

#es lo mismo que arriba pero en dos lineas
'''
for n,a in zip(nombres,apellidos):
    arch.writelines(f"nombre: {n}\nApellido: {a}\n-----------\n")
'''











