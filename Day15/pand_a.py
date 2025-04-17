import pandas as pd

# from google import drive
import matplotlib.pyplot as plt


numeros = pd.Series([1, 2, 3, 4, 5])
numeros.mean()

numeros.sum()

colores = pd.Series(["rojo", "amarillo", "verde"])
# print(colores)

autos = pd.Series(["audi", "bmw", "ferrari"])
# print(autos)

tabla = pd.DataFrame({"Tipo de Auto": autos, "Color": colores})
# print(tabla)

# drive.mount('/content/drive')

venta_autos = pd.read_csv("Day15/ventas-autos.csv")

# print(venta_autos)

venta_autos.to_csv('Day15/ventas-autos1.csv')

# print(venta_autos.dtypes)

# print(venta_autos.describe())

# print(venta_autos.info())

# print(venta_autos.columns)

# print(venta_autos.head())

# print(venta_autos.head(7))

# print(venta_autos.tail(5))

# print(venta_autos.loc[3])

# print(venta_autos.iloc[[3, 7, 9]])

# print(venta_autos["Kilometraje"])

# print(venta_autos["Kilometraje"].mean())

# print(venta_autos["Kilometraje"] > 10000)

# print(pd.crosstab(venta_autos["Fabricante"], venta_autos["Puertas"]))

# print(venta_autos.groupby("Fabricante")['Kilometraje'].mean())

venta_autos["Kilometraje"].plot()
plt.show()

venta_autos["Kilometraje"].hist()
plt.show()
venta_autos["Precio (USD)"].hist()
plt.show()
venta_autos["Precio (USD)"] = venta_autos["Precio (USD)"].astype(str)
venta_autos["Precio (USD)"] = venta_autos["Precio (USD)"].str.replace('$', '')
venta_autos["Precio (USD)"] = venta_autos["Precio (USD)"].str.replace(',', '')
venta_autos["Precio (USD)"] = venta_autos["Precio (USD)"].str.replace('.', '')
venta_autos["Precio (USD)"] = venta_autos["Precio (USD)"].astype(int)/100
venta_autos["Precio (USD)"].plot()
plt.show()
