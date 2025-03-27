from pathlib import Path, PureWindowsPath

carpeta = Path("/home/anderson-josue/Documents/Python/Day6/prueba.txt")

ruta_windows = PureWindowsPath(carpeta)

print(ruta_windows)

print(carpeta.read_text())
print(carpeta.suffix)
print(carpeta.stem)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")
