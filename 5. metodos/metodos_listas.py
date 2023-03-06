#creando una lista con list()
lista = list(["Hola","Deivi",34,56,23,True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
agregando_con_append = lista.append("JAJAJA")

#agregando un elemento a la lista con un indice especifico
#el primer parametro es el indice en el que quieras insertar un elemento
#el segundo parametro es el elemento que quieres que se agregue
lista.insert(2,"TOMA")

#agregando varios elementos a la lista
#agrega los elementos al final de la lista
#agrega multiples elementos al mismo tiempo, al contrario de append() que solo se le puede agregar un solo elemento
lista.extend(False, 2030)

#eliminando un elemento de la lista (por su indice)
lista.pop(-1) #-1 para eliminar el ultimo elemento de la lista

#removiendo un elemento de la lista por su valor
lista.remove("TOMA")

#eliminando todos los elemtnos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usamos el parametro de reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(56)

