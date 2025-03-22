def prubea(num1, num2, *args, **kwargs):
    """
    The function `prueba` takes two required arguments, any number of additional positional arguments,
    and any number of keyword arguments, and prints them out.
    
    :param num1: The `num1` parameter is the first positional argument that the `prueba` function
    expects to receive
    :param num2: num2 is the second parameter passed to the function prubea
    """
    print(f"El primer valor es {num1}")
    print(f"El primer valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100, 200, 300, 400]
kwargs = {"x": "uno", "y": "dos", "z": "tres"}

prubea(15, 50, *args, **kwargs)
