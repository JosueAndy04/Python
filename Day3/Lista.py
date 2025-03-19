# Lista
mi_lista = ['a', 'b', 'c']
print(type(mi_lista))

# Largo
mi_lista = ['a', 'b', 'c']
print(len(mi_lista))
print(type(mi_lista))

# Indice 
mi_lista = ['a', 'b', 'c']
resultado = mi_lista[0]
print(resultado)

# Concatenar
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
resultado = mi_lista[0]
print(resultado)
print(mi_lista3)

# Cambiar
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3[0] = 'alfa'
print(mi_lista3)

# Agregar append
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.append('g')
print(mi_lista3)

# Eliminar
mi_lista = ['a', 'b', 'c']
mi_lista2 = ['d', 'e', 'f']
mi_lista3 = mi_lista + mi_lista2
mi_lista3.pop()
mi_lista3.pop(0)
eliminado = mi_lista3.pop()
print(mi_lista3)
print(eliminado)

# Ordenar
lista = ['g', 'o', 'b', 'm', 'ca']
lista.sort()
print(lista)

# Ordenar al inverso
lista = ['g', 'o', 'b', 'm', 'ca']
lista.reverse()
print(lista)
