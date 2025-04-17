import matplotlib.pyplot as plt
import numpy as np

a = [1, 5, 3, 8, 7, 15]
plt.plot(a)
# plt.show()

x = list(range(101))

y = []
for numero in x:
    y.append(numero**2)

plt.plot(x, y)
# plt.show()

fig, ax = plt.subplots()

ax.plot(x, y)
# plt.show()

x = list(range(101))
y = []
for numero in x:
    y.append(numero**2)

fig, ax = plt.subplots()

ax.plot(x, y)

ax.set(
    title="Grafico de casos de COVID-19 en Latam",
    xlabel="dias",
    ylabel="casos confirmados",
)

fig.savefig("ejemplo-grafico-covid.png")

x_1 = np.linspace(0, 100, 20)
y_1 = x_1**2

fig, ax = plt.subplots()
ax.scatter(x_1, y_1)
# plt.show()

fig, ax = plt.subplots()

x_2 = np.linspace(-10, 10, 100)
y_2 = np.sin(x_2)

ax.scatter(x_2, y_2)
# plt.show()

comidas = {"lasagna": 350, "sopa": 150, "roast_beef": 650}

fig, ax = plt.subplots()
ax.bar(comidas.keys(), comidas.values())

ax.set(title="Precios de comidas", xlabel="Comidas", ylabel="Precios")
# plt.show()

fig, ax = plt.subplots()
ax.barh(list(comidas.keys()), list(comidas.values()))

ax.set(title="Precios de comidas", ylabel="Comidas", xlabel="Precios")
# plt.show()

x = np.random.randn(1000)

fig, ax = plt.subplots()
ax.hist(x)
# plt.show()
# print(plt.style.available)
plt.style.use('seaborn-v0_8-whitegrid')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 5))

ax1.plot(x_1, y_1, color='#fcba03')
ax2.scatter(x_2, y_2, color='#fcba03')
ax3.bar(comidas.keys(), comidas.values(), color='#fcba03')
ax4.hist(np.random.randn(1000), color='#fcba03')
plt.show()

