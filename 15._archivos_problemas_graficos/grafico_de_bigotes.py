import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("15._archivos_problemas_graficos\\bigotes.csv")

#creando el grafico de barras
sns.boxplot(x="categoria",y="valor",data=df)

#mostrando el grafico
plt.show()