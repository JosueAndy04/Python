# def mi_funcion():
#     lista = []
#     for x in range(1, 5):
#         lista.append(x * 10)
#     return lista


# def mi_generador():
#     for x in range(1, 5):
#         yield x * 10


# print(mi_funcion())
# print(mi_generador())

# g = mi_generador()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def mi_generador():
#     x = 1
#     yield x

#     x += 1
#     yield x

#     x += 1
#     yield x

# g = mi_generador()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


def perder_vida():
    for vidas in reversed(range(1, 5)):
        if vidas > 2:
            vidas -= 1
            yield f"Te quedan {vidas} vidas"
        elif vidas > 1:
            vidas -= 1
            yield "Te queda 1 vida"
        else:
            yield "Game Over"


"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"
perder_vida = perder_vida()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))



