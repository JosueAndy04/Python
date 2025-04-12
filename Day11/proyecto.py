import bs4
import requests

# crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iterar paginas
for pagina in range(1, 51):

    # crear sopa de cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    soup = bs4.BeautifulSoup(resultado.text, 'lxml')

    # sleccionar datos de los libros
    libros = soup.select('.product_pod')

    # iterar libros
    for libro in libros:

        # chequear quye tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)


# ver titulos
for t in titulos_rating_alto:
    print(t)
