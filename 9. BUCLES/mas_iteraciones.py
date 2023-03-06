
#creando las listas

frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Deivi"
numeros = [2,5,8,10]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue #--------> lo que hace es que se salta la accion dada
    print(f'me voy a comer una {fruta}')
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta con un break)
for fruta in frutas:
    if fruta == 'pera':
        break #------------> lo que hace es que se detenga en bucle y deje de iterar
    print(f'me voy a comer una {fruta}')

print("Bucle terminado")      
        
        
#recorrer una cadena de texto
for letra in cadena:
    print(letra)
       
#for en una sola linea de codigo
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero * 2)
print(numeros_duplicados)       
        
#for en una sola linea de codigo simplificado
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)    



