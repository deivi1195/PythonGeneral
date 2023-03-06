#ver la ruta del paquete con la propiedad __path__ 
#(tiene que haber un archivo __init__.py en la carpeta)
import paquete

print(paquete.__path__)

#utilizar la funcion del paquete
import paquete.saludar

print(paquete.saludar.saludar("dalto"))








