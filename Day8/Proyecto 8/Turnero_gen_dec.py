"""
Turnero generador y decorador
"""


def decorador_ticket(funcion):
    def wrapper():
        print("Este es su ticket:")
        print(next(funcion))
        print("Gracias, espere porfavor")

    return wrapper


def generador_farmacia():
    count = 0
    while True:
        count += 1
        serie = "F-" + str(count)
        yield serie


def generador_permuferia():
    count = 0
    while True:
        count += 1
        serie = "P-" + str(count)
        yield serie


def generador_cosmetica():
    count = 0
    while True:
        count += 1
        serie = "C-" + str(count)
        yield serie


ticket_farmacia = generador_farmacia()
ticket_perfumeria = generador_permuferia()
ticket_cosmetica = generador_cosmetica()