from os import system
# clase persona
# nombre y apellido
# cliente hereda de persona
# numero de cuenta y balance
# imprimir cliente todos los datos
# depositar y retirar
# codigo para depositar, retirar o salir
# crear cliente objeto


# The class `Persona` in Python defines a simple data structure for storing a person's first name and
# last name.
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Nombre: {self.nombre} \nApellido: {self.apellido}\n"


# This Python class represents a client with attributes such as name, account number, balance, and
# methods for depositing and withdrawing money.
class Cliente(Persona):
    def __init__(self, nombre, apellido, n_cuenta, balance):
        self.n_cuenta = n_cuenta
        self.balance = balance
        super().__init__(nombre, apellido)

    def depositar(self, deposito):
        self.balance = self.balance + deposito
        return self.balance

    def retirar(self, retiro):
        if retiro <= self.balance:
            self.balance = self.balance - retiro
        else:
            print("La cantidad de retiro es mayor al de tu cuenta")
            return self.balance

    def __str__(self):
        return (
            super().__str__()
            + f"Numero de cuenta {self.n_cuenta} y el balance es: {self.balance}"
        )


def crear_cliente(clientes):
    """
    The function "crear_cliente" creates a new client account with a unique account number and
    initializes the balance to zero.
    
    :param clientes: The `clientes` parameter in the `crear_cliente` function seems to be a list of
    existing clients. This list is being used to determine the account number for the new client being
    created. The new client's account number is set to be one more than the total number of clients in
    the list
    :return: The function `crear_cliente` is returning an instance of the `Cliente` class with the
    provided `nombre`, `apellido`, `n_cuenta`, and `balance` values.
    """
    nombre = input("Cual es tu nombre: ")
    apellido = input("Cual es tu apellido: ")
    n_cuenta = len(clientes) + 1
    balance = 0
    nombre_cuenta = apellido + str(n_cuenta)
    nombre_cuenta = Cliente(nombre, apellido, n_cuenta, balance)
    print("La cuenta ha sido creada con exito")
    return nombre_cuenta


def ver_cliente(n_cuenta, clientes):
    """
    The function `ver_cliente` takes a customer account number and a list of customers, and returns the
    customer object corresponding to the account number if it exists, otherwise returns False.
    
    :param n_cuenta: The `n_cuenta` parameter in the `ver_cliente` function seems to represent the
    account number of a client. The function is designed to search for a client in a list of clients
    based on their account number and return the client object if found
    :param clientes: The `ver_cliente` function takes two parameters:
    :return: The function `ver_cliente` is designed to return the client information associated with a
    given account number `n_cuenta` if it exists in the list of `clientes`. If the account number is
    found, the function will return the corresponding client object. If the account number is not found
    or is out of range, the function will return `False`.
    """
    if n_cuenta in range(1, len(clientes) + 1):
        for cliente in clientes:
            if n_cuenta == cliente.n_cuenta:
                return cliente
    else:
        return False


# pedir si ya tiene usuario
def inicio(clientes):
    """
    This Python function prompts the user to input their account number to verify their account, then
    allows them to deposit or withdraw funds from their account.
    
    :param clientes: The function `inicio` seems to be a part of a banking system where clients can
    deposit or withdraw money from their accounts. It takes a list of `clientes` as a parameter, which
    likely contains information about the clients and their accounts
    :return: The function `inicio` is returning either the updated `cliente` object after a deposit or
    withdrawal operation, or `False` if the user chooses to exit the system.
    """
    n_cuenta = input("Ingrese su numero de cuenta para verificar su cuenta:")
    cliente = ver_cliente(int(n_cuenta), clientes)
    if cliente is False:
        print("No se encuentra ese cliente")
    else:
        op = input(
            "Que quieres hacer - 'D' Depositar  o 'R' Retirar, cualquier otro letra para salir del sistema: "
        )
        if op == "D":
            deposito = input("Cuanto vas a depositar: ")
            cliente.depositar(float(deposito))
            print(cliente)
            return cliente
        elif op == "R":
            retiro = input("Cuanto quieres retirar: ")
            cliente.retirar(float(retiro))
            print(cliente)
            return cliente
        else:
            print("Ha salido del sistema")
            return False


def main():
    """
    The main function controls a program for managing bank accounts, allowing users to create clients,
    view balances, and exit the program.
    """
    print(60 * "-")
    print("Hola esta es un programa para controlar la cuenta bancaria")
    print(60 * "-")
    aj = Cliente("a", "j", 1, 500)
    ja = Cliente("j", "a", 2, 5000)
    clientes = [aj, ja]
    ini = True
    while ini is True:
        print("Opciones")
        print("[1] Crear cliente")
        print("[2] Ver Balance")
        print("[3] Salir")
        op = input("Que quieres hacer: ")
        match op:
            case "1":
                system("clear")
                clientes.append(crear_cliente(clientes))
            case "2":
                system("clear")
                inicio(clientes)
            case "3":
                system("clear")
                print("Has salido")
                break


main()
