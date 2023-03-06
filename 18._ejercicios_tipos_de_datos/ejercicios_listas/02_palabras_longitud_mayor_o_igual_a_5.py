# Encontras las palabras de una lista que tienen al menos 5 caracteres de longitud

paises = ["España", "Fran", "Ita", "Ale", "Reino", "Estados", "Canadá", "México"]

print(f'Contenido actual de la lista paises:\n{paises}')


#Solucion 1

paises_5_caracteres = []

for i in paises:
    if len(i) >= 5:
        paises_5_caracteres.append(i)
        
print(f"Cantidad de la variable paises actual: {paises_5_caracteres}")


#solucion 2

paises_5_caracteres = [i for i in paises if len(i) >= 5]

print(f"Cantidad de la variable paises actual: {paises_5_caracteres}")