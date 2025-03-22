def suma(*args):
    """
    The function "suma" takes in any number of arguments and returns the sum of all the arguments.
    :return: The function `suma` is returning the total sum of all the arguments passed to it.
    """
    total = 0

    for arg in args:
        print(arg)
        total += arg
    return total


print(suma(5, 1, 5, 6, 6, 5))
