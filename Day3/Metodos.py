# Upper
texto = 'Este es el texto de Anderson'
resultado = texto.upper()
print(resultado)

# Unica letra
texto = 'Este es el texto de Anderson'
resultado = texto[2].upper()
print(resultado)

# Lower
texto = 'Este es el texto de Anderson'
resultado = texto.lower()
print(resultado)

# Split
texto = 'Este es el texto de Anderson'
resultado = texto.split()
print(resultado)

# Split con separador
texto = 'Este es el texto de Anderson'
resultado = texto.split('t')
print(resultado)

# Join
a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a,b,c,d])
print(e)

# Find
# Devuelve -1 si no se encuentra
texto = 'Este es el texto de Anderson'
resultado = texto.find('g')
print(resultado)

# Replace
texto = 'Este es el texto de Anderson'
resultado = texto.replace('Anderson', 'Josue')
print(resultado)
