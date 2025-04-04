import os 
# import shutil
from pathlib import Path
# import send2trash

# archivo = open('curso.txt', 'w') 
# archivo.write('texto de prueba')
# archivo.close()

ruta = Path('/home/anderson-josue/Documents/Python/Day8')
# shutil.move('curso.txt', ruta)
# shutil.rmtree No utilizar nunca 
# send2trash.send2trash('curso.txt')

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En la carpeta {ruta}')
    print('Las subcarpeta son:')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son: ')
    for arch in archivo:
        if arch.startswith('2015'):
            print(f'\t{arch}')
    print('\n')
