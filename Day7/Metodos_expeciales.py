class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado cd")


mi_cd = CD("ALmafuerte", "Almafuerte", 24)

print(mi_cd)
print(len(mi_cd))

del mi_cd

# print(mi_cd)
