mi_tuple = (1, 2, (10, 20), 3, 4)
print(type(mi_tuple))

# Consultar
print(mi_tuple[-2])

# Agregar
mi_tuple = list(mi_tuple)
print(mi_tuple[2][0])

# Lista
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))

# Asignar a diferentes listas
t = (1, 2, 3)
x, y, z = t
print(x, y, z)

#Propiedades
# Contar
t = (1, 2, 3, 4, 1)
print(t.count(1))
#Index
t = (1, 2, 3, 4, 1)
print(t.index(2))