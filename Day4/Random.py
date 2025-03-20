from random import randint
from random import uniform
from random import random
from random import choice
from random import shuffle

aleatorio = randint(1, 50)
print(aleatorio)

aleatorio = uniform(1, 50)
print(aleatorio)

aleatorio = random()
print(aleatorio)

colores = ["azul", "rojo", "verde", "amarillo"]
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)