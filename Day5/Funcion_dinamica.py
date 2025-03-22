def chequear_3_cifras(numero):
    """_chequear 3 cifras de un numero_

    Args:
        numero (number): _parametro numerico_

    Returns:
        _boolean_: _Dice ture o false segun el resultado_
    """
    return numero in range(100, 1000)


resultado = chequear_3_cifras(500)
print(resultado)


def chequear_3_cifras1(numero):
    """
    The function `chequear_3_cifras1` checks if a number has three digits.

    :param numero: The parameter "numero" is a variable representing a number that is being checked to
    determine if it has three digits. The function "chequear_3_cifras1" checks if the number falls
    within the range of 100 to 999, inclusive, which indicates that it has three digits
    :return: The function `chequear_3_cifras1` is returning a boolean value indicating whether the input
    `numero` is a 3-digit number (i.e., a number between 100 and 999 inclusive).
    """
    return numero in range(100, 1000)


suma = 5651 + 464

resultado = chequear_3_cifras(suma)
print(resultado)


def chequear_3_cifras2(lista):
    """
    The function `chequear_3_cifras2` checks if any number in a list is a 3-digit number.

    :param lista: The function `chequear_3_cifras2` checks if any number in the given list `lista` is a
    3-digit number (i.e., a number between 100 and 999 inclusive). If it finds at least one 3-digit
    number in the list, it returns
    :return: The function `chequear_3_cifras2` is returning a boolean value. It returns `True` if any
    number in the input list `lista` is a 3-digit number (between 100 and 999), otherwise it returns
    `False`.
    """
    for n in lista:
        if n in range(100, 1000):
            return True
        else:
            pass
    return False


numeros = [12313, 21687, 4984, 9846, 100, 255]


resultado = chequear_3_cifras(numeros)
print(resultado)


def chequear_3_cifras3(lista):
    """
    This Python function filters out numbers in a list that have exactly 3 digits.

    :param lista: The function `chequear_3_cifras3` takes a list of numbers as input and returns a new
    list containing only the numbers that have exactly 3 digits (between 100 and 999 inclusive)
    :return: The function `chequear_3_cifras3` returns a new list `lista_3_cifras` containing only the
    elements from the input list `lista` that have exactly 3 digits (between 100 and 999 inclusive).
    """

    lista_3_cifras = []

    for n in lista:
        if n in range(100, 1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras


resultado = chequear_3_cifras3(numeros)
print(resultado)
