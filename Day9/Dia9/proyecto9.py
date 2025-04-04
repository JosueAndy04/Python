"""
Buscador de numeros de serie
"""

from pathlib import Path
import os
from datetime import datetime
import re
import time
import math

ruta = Path("/home/anderson-josue/Documents/Python/Day9/Dia9/Mi_Gran_Directorio")


def nombre_arhivo():
    fecha = datetime.today()
    print(f"Fecha de busqueda: [{fecha.day}/{fecha.month}/{fecha.year}]")
    print("ARCHIVO\t\t NRO. SERIE")
    print("-" * 7 + "\t\t " + "-" * 10)
    total = []
    for archivo in os.walk(ruta):
        for nombre in archivo[2]:
            if nombre.endswith(".txt"):
                ruta_archivo = Path(archivo[0] + "/" + nombre)
                text = ruta_archivo.read_text()
                for linea in text.splitlines():
                    resultado = re.compile(r"N\w{3}-\d{5}").search(linea)
                    if resultado:
                        print(f"{nombre}\t {resultado.group()}")
                        total.append(resultado.group())
    print('Numeros encontrados: ' + str(len(total)))

def main():
    inicio = time.time() 
    nombre_arhivo()
    fin = time.time()
    resultado = math.ceil(fin - inicio)
    print(f'Duracion de la busqueda: {resultado} segundos')
    print('-' * 50)

main()