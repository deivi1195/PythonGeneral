diccionario = {
    'nombre' : "Deivi",
    'apellido' : "Gonzalez",
    'edad' : "27"
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get() (si el programa no enecuentra nada el programa continua)
valor_de_edad = diccionario.get("edad")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre","edad")

#obteniendo un elemento dict_item iterable
diccionario_iterable = diccionario.items()
















