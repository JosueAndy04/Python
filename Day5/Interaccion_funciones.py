from random import shuffle

# Lista inicial

palitos = ["-", "--", "---", "----"]


# Mezclar palitos
def mezclar(lista):
    """
    The function "mezclar" shuffles the elements of a given list and returns the shuffled list.
    
    :param lista: The `mezclar` function you provided seems to be intended to shuffle a given list.
    However, the `shuffle` function is not defined in the code snippet you provided. To make this
    function work, you need to import the `shuffle` function from the `random` module
    :return: The function `mezclar` is returning a shuffled version of the input list `lista`.
    """
    shuffle(lista)
    return lista


# Pedirle intento
def probar_suerte():
    """
    The function `probar_suerte` prompts the user to choose a number between 1 and 4 and returns the
    chosen number as an integer.
    :return: The function `probar_suerte` is returning the integer value of the user's input after
    validating that it is one of the numbers in the list ["1", "2", "3", "4"].
    """
    intento = ""

    while intento not in ["1", "2", "3", "4"]:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)


# Comprobar intento
def chequear_intento(lista, intento):
    """
    The function `chequear_intento` checks a specific element in a list and provides different messages
    based on its value.
    
    :param lista: The parameter `lista` is likely a list of items or values. The function
    `chequear_intento` takes two parameters: `lista` and `intento`. The function checks if the element
    at index `intento - 1` in the `lista` is equal to "-"
    :param intento: The `intento` parameter in the `chequear_intento` function is used to specify the
    index of the element in the `lista` that you want to check. The function will then check if the
    element at that index is equal to "-". If it is, it will print "
    """
    if lista[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te salvaste")

    print(f"Te ha tocado {lista[intento - 1]}")


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)
