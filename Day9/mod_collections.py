from collections import Counter, defaultdict, namedtuple

numeros = [8, 6, 9, 5, 4, 5, 5, 5, 8, 7, 4, 5, 4, 4]
print(Counter(numeros))
print(Counter("mississippi"))

frase = "al pan pan y al vino vino"
print(Counter(frase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4])
print(serie.most_common(1))
print(list(serie))

mi_dic = {"uno": "verde", "dos": "azul", "tres": "rojo"}
print(mi_dic["dos"])

mi_dic = defaultdict(lambda: "nada")

mi_dic["uno"] = "verde"
print(mi_dic["dos"])

print(mi_dic)

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.75, 79)

print(ariel.nombre)