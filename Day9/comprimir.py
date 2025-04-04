# import zipfile
import shutil
# from pathlib import Path

# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

# mi_zip.write('curso.txt')

# mi_zip.close()

# zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')

# zip_abierto.extractall()

# carpeta_origen = Path('/home/anderson-josue/Documents/Python/Day9')

# archivo_destino = 'Todo_comprimido'

# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Todo_comprimido.zip', 'Extraccion', 'zip')