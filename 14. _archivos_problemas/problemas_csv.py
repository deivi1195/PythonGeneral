#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("14._archivos_problemas\\datos.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df['edad'][0]))

#reemplazando los datos "dalto" por "maestro"
df['apellido'].replace("dalto","maestro",inplace=True)

#mostrando la columna apellido
#print(df['apellido'])

#eliminando filas con datos faltantes
df = df.dropna()

#eliminando columnas con datos faltantes
#el parametro de axis=0 son las columnas y axis=1 son las filas
df = df.dropna(axis=1)

#eliminando las filas repeditas
df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("14._archivos_problemas\\datos_limpios.csv")







