#Creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}
print(conjunto2)


#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto (3:22:55)
#para verificar si NO ES un subconjunto es >=
#para verificar si ES un subconjunto es <=
resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 > conjunto1

#verificar si hay algun numero elemento en comun
#si hay uno o mas elementos iguales entre los conjuntos lanza False
#si ningun elemento entre los conjuntos son iguales lanza True
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)










