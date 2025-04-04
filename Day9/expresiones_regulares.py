# expresiones regulares
# /d digito numerico v\d.\d\d v5.00
# /w caracter alfanumerico \w\w\w-\w\w sol-do
# /s expacio en blanco numero\s\d\d
# /D no numerico \D\D\D
# /W no alfanumerico \W\W\W
# /S no espacio en blanco \S\S\S
# CUANTIFICADORES
# +   1 o mas veces codigo_\d-\d+
# {n} se repite n veces \d-\d{4}
# {n,m} se repite de n a m veces \w{3,5}
# {n,} desde n hacia arriba -\d{4,}-
# * 0 o mas veces \w\s*\w
# ? 1 o 0 casas?
import re

# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
# patron = 'ayuda'
# busqueda = re.search(patron, texto)
# print(busqueda.end())

# texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
# patron = 'ayuda'
# busqueda = re.findall(patron, texto)
# print(busqueda)

# for hallazgo in re.finditer(patron, texto):
#     print(hallazgo.span())

texto = "Llama al 564-525-6588 ya mismo"

# patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')

resultado = re.search(patron, texto)

print(resultado.group(1))

# clave = input('Introduce clave: ')

# patron = r'\D{1}\w{7}'

# chequear = re.search(patron, clave)
# print(chequear)

# texto = "No atendemos los lunes por la tarde"

# buscar = re.search(r"lunes|martes", texto)
# buscar1 = re.search(r"....demos", texto)
# buscar2 = re.search(r"^\D", texto)
# buscar3 = re.search(r"\D$", texto)
# buscar4 = re.findall(r"[^\s]+", texto)


# print(buscar)
# print(buscar1)
# print(buscar2)
# print(buscar3)
# print(buscar4)


def verificar_email(email):
    buscar = re.search(r'\w+@\w+\.\w+', email)
    if buscar:
        print('ok')
    else:
        print('error')

verificar_email('anderjosue456gmail.com.br')