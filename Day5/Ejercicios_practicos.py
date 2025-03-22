def devolver_distintos(num1, num2, num3):
    """
    This Python function takes three numbers as input and returns the sum if it falls within a specific
    range, the maximum number if the sum is greater than 15, the minimum number if the sum is less than
    10, or prompts the user to input valid numbers.
    
    :param num1: It looks like you were about to provide the value for `num1` but it got cut off. Please
    go ahead and provide the value for `num1` so I can assist you further
    :param num2: It seems like you have provided the code snippet for a function called
    `devolver_distintos`, but you have not provided the value for `num2`. Could you please provide the
    value for `num2` so that I can assist you further with understanding how the function works with the
    given parameters
    :param num3: It seems like you might have missed providing the value for `num3`. Could you please
    provide the value for `num3` so that I can assist you further with the `devolver_distintos`
    function?
    :return: The function `devolver_distintos` returns the sum of the three numbers `num1`, `num2`, and
    `num3` if the sum is in the range of 10 to 15 (inclusive). If the sum is greater than 15, it returns
    the maximum of the three numbers. If the sum is less than 10, it returns the minimum of the three
    numbers
    """
    numeros = [num1, num2, num3]
    suma_total = num1 + num2 + num3

    if suma_total in range(10, 15):
        return suma_total
    elif suma_total > 15:
        return max(numeros)
    elif suma_total < 10:
        return min(numeros)
    else:
        print("Introduce un numero valido")


# Pedir numeros
numero1 = float(input("Escribe un numero: "))
numero2 = float(input("Escribe un numero: "))
numero3 = float(input("Escribe un numero: "))

# LLamar a la funcion
print(devolver_distintos(numero1, numero2, numero3))


def letras_sin_repetir(palabra):
    """
    The function `letras_sin_repetir` takes a string as input, converts it to lowercase, removes
    duplicate letters, sorts the unique letters, and returns them as a list.
    
    :param palabra: The function `letras_sin_repetir` takes a string `palabra` as input and returns a
    sorted list of unique letters in the input string, ignoring case sensitivity
    :return: The function `letras_sin_repetir` returns a sorted list of unique lowercase letters found
    in the input `palabra`.
    """
    letras = list(set(str(palabra).lower()))
    letras.sort()
    return letras


# Llamar a la funcion

print(letras_sin_repetir("Anderson"))


def ceros(*args):
    """
    The function `ceros` checks if there are consecutive zeros in the input arguments.
    :return: The function `ceros` is checking if there are two consecutive zeros in the input arguments.
    If it finds two consecutive zeros, it returns `True`. If it doesn't find two consecutive zeros, it
    returns `False`.
    """
    i = 0
    for arg in args:
        if args[i] == 0 and args[i + 1] == 0:
            return True
        else:
            i += 1
    return False

print(ceros(5, 6, 1, 0, 0, 9, 3, 5))
print(ceros(6, 0, 5, 1, 0, 3, 0, 1))
print(ceros(1, 1, 5, 1, 0, 3, 0, 1))


def contar_primos(num):
    """
    This Python function counts the number of prime numbers up to a given input number.
    
    :param num: The given code defines a function called `contar_primos` that counts the number of prime
    numbers up to a given input number `num`. The function uses a basic prime number checking algorithm
    to find all prime numbers up to the given number
    :return: the number of prime numbers up to the input number 'num'.
    """

    primos = [2]
    i = 3

    if num < 2:
        return 0
    
    while i <= num:
        for n in range(3, i ,2):
            if i % n == 0:
                i += 2
                break
        else:
            primos.append(i)
            i += 2

    print(primos)
    return len(primos)


print(contar_primos(10))
