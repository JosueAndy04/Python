from pathlib import Path

base = Path.home()

# guia = Path(base, 'Europa', 'Spain', Path("Barcelona", "Sagrada_Familia.txt"))

# guia2 = guia.with_name('La_Pedrera.txt')

# print(guia.parent.parent.parent)

# print(base)
# print(guia)
# print(guia2)

guia = Path(Path.home(), 'Europa')

for txt in Path(guia).glob('*.txt'):
    print(txt)


# guia1 = Path('Europa', 'Spain', 'Barcelona', 'La Sagrada Familia.txt')
# en_europa = guia1.relative_to(Path('Europa'))
# en_spain = guia1.relative_to(Path('Europa', 'Spain'))
# print(en_europa)
# print(en_spain)