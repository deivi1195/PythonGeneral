#importando modulo_saludar sin la funcion y llamando al modulo como m_saludar
import modulo_saludar as m_saludar

saludo =  m_saludar.saludar("Lucas")
print(saludo) 

#importando el modulo con la funcion saludar
from modulo_saludar import saludar

saludo = saludar("Lucas")
print(saludo)


#importando todas las funciones del modulo
#pero es una mala practica
from modulo_saludar import *

saludo = saludar("Lucas")
print(saludo)

#para ver las propiedades y metedos de el namespace
#print(dir(m_saludar))

#accdemos al nombre de este modulo
#print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)


