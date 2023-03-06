#Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,error):
        print(f"Impresionante, cometiste un error: {error}")

#lanzando mi propia excepcion  
#raise MiExcepcion("Cometiste un error master")

#manejandola
try:
    raise MiExcepcion("Cometiste un error master")
except:
    print("Como vas a cometer ese error?")












      