class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beeeee')


vaca1 = Vaca('AURORA')
oveja = Oveja('Joly')

vaca1.hablar()
oveja.hablar()

animales = [vaca1, oveja]

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja)
animal_habla(vaca1)