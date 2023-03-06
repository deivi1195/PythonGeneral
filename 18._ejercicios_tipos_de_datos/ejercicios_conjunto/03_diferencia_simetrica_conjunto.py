# Calcular diferencia simetrica entre dos conjuntos

escritorio = {'Notepad++', 'Atom', 'Eclipse', 'Netbeans', 'PyCharm'}
portatil = {'Notepad++', 'PyCharm', 'VSC', 'IDEA'}

#serian los programas que no estan instalados en cualquiera de los dos conjuntos


resultado = escritorio.symmetric_difference(portatil)

print(resultado)


