import pandas as pd

#usando la funcion read_csv para leer el archivo csv
#df = data frames.. filas||columnas
#df = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")

#ordenandolo de forma descendente
df_ordenandolo_descendente = df.sort_values("edad",ascending=False)

#concatenando los dos data frame
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras 3 filas con head()
#te muestra tantas filas como le indiques de arriba hacia abajo
primera_fila = df.head(3)

#accediendo a las ultimas 3 filas con tail()
#te muestra tantas filas como le indiques de abajo hacia arriba
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
#shape es una propiedad
#filas_y_columnas_totales = df.shape
#(6,3)
#filas_totales = filas_y_columnas_totales[0]
#6
#columnas_totales = filas_y_columnas_totales[1]
#3

#desempaquetando
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2, columna 2
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas las filas de una columna
#con slicing el primer parametro como no tiene nada significa que son todos
#el segundo parametro es 1 solo elemento especifico que tu quieras
'''.iloc[FILAS,COLUMNAS]'''
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
#accedo a la 2da fila y a todas las columnas
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila3 = df.iloc[2,:]

#accediendo a las filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]


print(mayor_que_30)

















