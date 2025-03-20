from random import randint
# Adivina el numero
# Preguntar por nombre
# preguntar por numero entre 1-100
# 1 > n > 100 no permitido
# n < nprogram menor
# n > nprogram mayor
# n == nprogram ganaste y numero de intentos
# Si no hasta que se acaben los intentos


print("Hola este programa es un mini juego de numeros")
print("Adivinaras un numero entre el 1 - 100")
print("Tienes 5 intentos")

# Input nombre y numero
nombre = input("Porfavor dime tu nombre: ")

# Proceso
nprog = randint(1, 100)
intentos = 10

# Main
while intentos != 0:
    n = int(input('Dame un numero entre el 1 - 100: '))

    if n > 0 and 0 < 101:
        if (n < nprog):
            intentos -= 1
            print('El numero es menor')
        elif (n > nprog):
            intentos -= 1
            print('El numero es mayor')
        elif (n == nprog):
            intentos -= 1
            print(f'Ganaste {nombre}, con {(intentos - 10) * -1} intentos')
            break
    else:
        intentos -= 1
        print('Numero no permitido')
else:
    print(f'Perdiste {nombre}, el numero es {nprog}')
