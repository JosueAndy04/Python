# Proyecto 3 Analisador de texto
# Pedir texto
# Pedir 3 letras
# Cuantas veces aparece cada letra
# Cuantas palabras hay en total
# Primera y ultima letra
# Invertir el orden
# Aparece python

# Main
print('Hola este es un analizador de texto, con este programa podras saber como esta compuesto tu texto')

# Input texto, letras
texto = input('Dime que texto quieres analizar: ')
print('Necesitamos 3 letras para analizar')
letra1 = input('La primera letra: ')
letra2 = input('La segunda letra: ')
letra3 = input('La tercera letra: ')

# Cuantas veces aparace cada letra
total_letra1 = texto.lower().count(letra1)
total_letra2 = texto.lower().count(letra2)
total_letra3 = texto.lower().count(letra3)
print(f'El total de letras {letra1} es: {total_letra1}')
print(f'El total de letras {letra2} es: {total_letra2}')
print(f'El total de letras {letra3} es: {total_letra3}')

# Cuantas palabras hay en total
total_palabras = len(texto.split())
print(f'El total de palabras con repeticion es: {total_palabras}')
total_palabras = len(set(texto.split()))
print(f'El total de palabras sin repeticion es: {total_palabras}')


# Primera y ultima palabra
list_palabras = list(texto)
primera_letra = list_palabras[0]
ultima_letra = list_palabras[-1]
print(f'La primera letra es: {primera_letra}')
print(f'La ultima letra es: {ultima_letra}')


#Invertir el orden de letras
print(f'Inverso de las letras: {texto[::-1]}')
list_texto = list(texto.split())
list_texto.reverse()
texto_inv = ' '.join(list_texto)
print(f'Inverso de palabras: {texto_inv}')

#Buscar palabra Python
buscar = set(texto.split())
print(f"Existe la palabra Python en el texto: {'Python' in buscar}")
