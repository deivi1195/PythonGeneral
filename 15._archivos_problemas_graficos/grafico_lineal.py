import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("15._archivos_problemas_graficos\\pedos.csv")

#creando el grafico de lineas
sns.lineplot(x="fecha",y="pedos",data=df)

#creando un punto en el momento de mas pedos
plt.plot("01-09",17,"+")

#mostrando el grafico
plt.show()




