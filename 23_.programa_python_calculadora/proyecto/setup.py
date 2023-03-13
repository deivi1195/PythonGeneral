from setuptools import setup

setup(name='calculadora', version='1.0.0', packages=['calculadora'], 
entry_points= {
    #si tuvieramos una aplicacion con interfaz grafica
    #se puede escribir 'gui_scripts
    #['nombre de proyecto = donde esta alojado el proyecto.__main__:metodo del modulo(def main())]
    'console_scripts': ['calculadora = calculadora.__main__:main']
})














