# def suma():
#     n1 = int(input('numero 1: '))
#     n2 = int(input('numero 2: '))
#     print(n1 +n2)
#     print('Gracias por sumar' + n1)

# try:
#     suma()
#     # Codigo que queremos probar
# except TypeError:
#     # Codigo a ejecutar si hay error
#     print('Estas intentando concatenar tipos distintos')
# except ValueError:
#     print('Ese no es un numero')
# else:
#     # Codigo a ejecutar si no hay un error
#     print('Hiciste todo bien')
# finally:
#     # Codigo que se va a ejecutar de todos modos
#     print('eso fue todo')
def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except ValueError:
            print("Ese no es numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break
    print("Gracias")


pedir_numero()
