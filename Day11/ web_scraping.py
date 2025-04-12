import bs4
import requests 

resultado = requests.get('https://www.escueladirecta.com/l/products?productType=course&page=1')

soup = bs4.BeautifulSoup(resultado.text, 'lxml')

# parrafo_espacial = soup.select('p')[3].getText()
# print(parrafo_espacial)
# print(soup.select('title')[0].getText())
# columna_lateral = soup.select('.section a')
# print(columna_lateral)
# for p in columna_lateral:
#     print(p.getText())

# imagenes = soup.select('img')[0]['src']

# imagen_curso = requests.get(imagenes)

# f = open('imagen.jpg', 'wb')
# f.write(imagen_curso.content)
# f.close()

