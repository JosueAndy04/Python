mi_set = set([1, 2, 3, 4, 5])
otro_set = {1, 2, 3, 4, 5}
print(type(mi_set))
print(mi_set)
print(type(otro_set))
print(otro_set)

# Admite tuple u objetos inmmutables
mi_set1 = set([1, 2, 3, (1, 2, 3), 4, 5])
print(mi_set1)

# Len
mi_set1 = set([1, 2, 3, (1, 2, 3), 4, 5])
print(len(mi_set1))

# Consulta
mi_set1 = set([1, 2, 3, (1, 2, 3), 4, 5])
print(2 in mi_set1)

# Union
otro_set1 = mi_set.union(mi_set1)
print(mi_set1)

# Add
otro_set1.add(100)
print(otro_set1)

# Eliminar
otro_set1.remove(100)
print(otro_set1)

# Descarta, no devuelve erro
otro_set1.discard(200)
print(otro_set1)

# Pop
otro_set1.pop()
print(otro_set1)

# Clear
otro_set1.clear()
print(otro_set1)