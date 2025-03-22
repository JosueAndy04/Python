precios_cafe = [("capuchino", 1.5), ("Expreso", 1.2), ("Moka", 1.9)]


def cafe_mas_caro(lista_precios):
    """
    The function `cafe_mas_caro` takes a list of coffee prices and returns the name and price of the
    most expensive coffee.
    
    :param lista_precios: The function `cafe_mas_caro` takes a list of tuples where each tuple contains
    the name of a coffee and its price. The function iterates through the list to find the most
    expensive coffee and returns a tuple with the name of the most expensive coffee and its price
    :return: The function `cafe_mas_caro` is returning a tuple containing the name of the most expensive
    coffee in the list `lista_precios` and its corresponding price.
    """
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        else:
            pass
    return (cafe_mas_caro, precio_mayor)


cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafe mas caro es {cafe} cuyo precio es {precio}")
