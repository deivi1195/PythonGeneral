# Remover un elemento (valor) de una tupla

lenguajes = ("Python", "Java", "JavaScript", "C++", "Ruby")

'''
print(f"~Contenido actual de la tupla `lenguajes`:\n---{lenguajes}")
print(f"~Cantidad de elementos de la tupla `lenguajes`:\n--------- {len(lenguajes)} ---------")

lenguaje = "Java"

if lenguaje in lenguajes:
    lenguajes = lenguajes[:1] + lenguajes[2:]
    
    
    print(f"~Contenido actual de la tupla `lenguajes` despues de remover 'Java':\n---{lenguajes}")
    print(f"~Cantidad de elementos de la tupla `lenguajes`:\n--------- {len(lenguajes)} ---------")

else:
    print(f'No existe un nombre de lenguaje con: {lenguaje}')'''

#Tambien se puede eliminar un elemento de una tupla convirtiendola a lista

if len(lenguajes) > 0:
    print(f"Lenguajes de la tupla actual:\n{lenguajes}")
    lenguajes_lista = list(lenguajes)
    '''for i in range(len(lenguajes_lista)):
       lenguajes_lista[i] = lenguajes_lista[i].lower()
    print(lenguajes_lista)'''
    lenguajes_lista = [i.lower() for i in lenguajes_lista] #lista de comprension
    while True:
        elemento_remover = input(f'Escribe el lenguaje que deseas eliminar de la tupla: ')
        elemento_remover = elemento_remover.lower()
        if elemento_remover in lenguajes_lista:
            lenguajes_lista.remove(elemento_remover)
            lenguajes = tuple(lenguajes_lista)
            print(f'Ahora tu nueva tupla es:\n{lenguajes}') 
        #elif elemento_remover not in lenguajes_lista:
        else:
            print('El lenguaje que escribiste no se encuentra en la tupla.')
            
else: 
    print("No hay lenguajes que remover.")
    
       


    
    


    
