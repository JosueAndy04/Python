class Animal:
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    # modificado
    def hablar(self):
        return super().hablar()

    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")


pajaro_amarillo = Pajaro(2, "amarillo", 300)

pajaro_amarillo.nacer()
pajaro_amarillo.hablar()


class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('jajajjaj')
    
    def hablar(self):
        print('que tal')

class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar()

mi_nieto.reir()

print(Nieto.__mro__)