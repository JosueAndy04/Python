# if
if 10 > 9:
    print("Es correcto")

# else
if 10 < 9:
    print("Es correcto")
else:
    print('No es correcto')

# Ejemplo
mascota = 'perro'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
elif mascota == 'pez':
    print('Tienes un pez')
else:
    print('No se que animal es')

# Ejemplo 2 
edad = 16 
calificacion = 9

if edad < 18:
    print('Eres menor de edad')
    if calificacion >=7:
        print('Aprovado')
    else:
        print('No aprovado')
else:
    print('Eres adulto')