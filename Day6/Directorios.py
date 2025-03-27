# import os
from pathlib import Path

# ruta = os.getcwd()

# print(ruta)

# ruta = os.chdir('/home/anderson-josue/Documents/Python/Alternativo/otro-archivo.txt')

# archivo = open('otro-archivo.txt')

# print(ruta)

# ruta = os.makedirs("/home/anderson-josue/Documents/Python/Alternativo1")

# ruta = "/home/anderson-josue/Documents/Python/Alternativo1"

# nombre de base
# elemento = os.path.basename(ruta)
# print(elemento)

# nombre del directorio
# elemento = os.path.dirname(ruta)

# ambos elementos por tupla
# elemento = os.path.split(ruta)

# eliminar carpeta
# os.rmdir('/home/anderson-josue/Documents/Python/Alternativo1')

# para otro sistema operativo
carpeta = Path("/home/anderson-josue/Documents/Python/Alternativo1")
archivo = carpeta / "otro_archivo.txt"

mi_archivo = open(archivo)
print(mi_archivo.read())

# otra manera
carpeta = (
    Path("/home/anderson-josue/Documents/Python/Alternativo1") / "otro_archivo.txt"
)

mi_archivo = open(carpeta)
print(mi_archivo.read())
