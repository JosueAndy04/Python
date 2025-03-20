monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo mas dinero")

# Ejemplo
respuesta = "s"

while respuesta == "s":
    respuesta = input("Quires seguir?: ")
else:
    print("Gracias")

# Ejemplo Pass ticket
# respuesta = 's'

# while respuesta == 's':
#     pass
# print('Pass')

# Ejemplo Interrumpir
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        break
    print(letra)

# Ejemplo continue
nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == "r":
        continue
    print(letra)
