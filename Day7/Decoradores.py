class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()

    def pintar_negro(self):
        self.color = "amarillo"
        print(f"El pajaro a cambiado a el color {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)
    
    @staticmethod
    def mirar():
        print('Hola estupido pajaro')
        



mi_pajaro = Pajaro("Negro", "Tucan")

print(f"Mi pajaro {mi_pajaro.especie} es de color {mi_pajaro.color}")

mi_pajaro.piar()
mi_pajaro.volar(50)
mi_pajaro.pintar_negro()
mi_pajaro.alas = False
print(mi_pajaro.alas)

Pajaro.poner_huevos(3)
Pajaro.mirar()