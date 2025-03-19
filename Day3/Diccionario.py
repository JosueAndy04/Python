diccionario = {"c1": "valor1", "c2": "valor2"}
print(diccionario)

# Consultar
resultado = diccionario["c1"]
print(resultado)

# Ejemplo
cliente = {"nombre": "Anderson", "apellido": "Josue", "peso": 88, "talla": "M"}
consulta = cliente["talla"]
print(consulta)

# Diccionario dentro de diccionario
dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dic["c3"]["s2"])
print(dic["c2"][1])

# Practica
dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic["c2"][1].upper())

# Agregar
dic = {1: "a", 2: "b"}
print(dic)
dic[3] = 'c'
print(dic)

# Cambiar
dic = {1: "a", 2: "b"}
print(dic)
dic[2] = 'B'
print(dic)

# Imprimir todas la claves
print(dic.keys())
print(dic.values())
print(dic.items())
