# Loop For
lista = ["a", "b", "c"]

for letra in lista:
    print("Letra: " + letra)

# Loop for index
lista = ["a", "b", "c", "d"]

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra}: {letra}")

# Loop For ejemplo
lista = ["pablo", "laura", "fede", "julia"]

for nombre in lista:
    if nombre.startswith("l"):
        print(nombre)
    else:
        print("Nombre que no comienza con L")

# Ejemplo
numeros = [1, 2, 3, 4, 5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)
print(mi_valor)

# Ejemplo
palabra = "python"

for letra in palabra:
    print(letra)

# Ejemplo
for objeto in [[1, 2], [3, 4], [5, 6]]:
    print(objeto)

# Ejemplo
for a, b in [[1, 2], [3, 4], [5, 6]]:
    print(a)
    print(b)

# Ejemplo dic
dic= {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item in dic.values():
    print(item)

dic= {'clave1':'a', 'clave2':'b', 'clave3':'c'}
for a, b in dic.items():
    print(a, b)