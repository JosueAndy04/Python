# Conocer el indice de un caracter
# Conocer que caracter hay en un indice
mi_texto = 'Esta es una prueba'
resultado = mi_texto[-4]
print(resultado)

# Index
mi_texto = 'Esta es una prueba'
resultado = mi_texto.index('a', 5, 11)
print(resultado)

# Rindex
mi_texto = 'Esta es una prueba'
resultado = mi_texto.rindex('a', 5, 11)
print(resultado)