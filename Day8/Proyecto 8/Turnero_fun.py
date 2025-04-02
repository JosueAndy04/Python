from Turnero_gen_dec import ticket_perfumeria
from Turnero_gen_dec import ticket_farmacia
from Turnero_gen_dec import ticket_cosmetica
from Turnero_gen_dec import decorador_ticket

"""
Turnero
"""


def bienvenida():
    print("-" * 60 + "----------")
    print("-" * 30 + "Bienvenido" + "-" * 30)
    print("-" * 60 + "----------")
    print("Areas")
    print("[F] Farmacia")
    print("[C] Cosmeticos")
    print("[P] Perfumeria")


def elegir_area():
    while True:
        try:
            bienvenida()
            sector = input("En que area necesita realizar sus tramites: ")
            ['P','F','C'].index(sector)
        except ValueError:
            print("Opcion no valida")
        match sector:
            case "F":
                decorador = decorador_ticket(ticket_farmacia)
                decorador()
                print('Otro Turno')
            case "C":
                decorador = decorador_ticket(ticket_cosmetica)
                decorador()
                print('Otro Turno')
            case "P":
                decorador = decorador_ticket(ticket_perfumeria)
                decorador()
                print('Otro Turno')

elegir_area()
