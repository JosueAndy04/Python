import pygame
import random
from pygame import mixer

# Inicializar pygame
pygame.init()

# crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo del juego
pygame.display.set_caption("Invasion Extraterrestre")
icono = pygame.image.load("/home/anderson-josue/Documents/Python/Day10/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("/home/anderson-josue/Documents/Python/Day10/Fondo.jpg")

# Musica
mixer.music.load("/home/anderson-josue/Documents/Python/Day10/MusicaFondo.mp3")
mixer.music.play(-1)

#  Variable Jugador
img_jugador = pygame.image.load(
    "/home/anderson-josue/Documents/Python/Day10/cohete.png"
)
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Variable enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(
        pygame.image.load("/home/anderson-josue/Documents/Python/Day10/enemigo.png")
    )
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)

# Variable balas
balas = []
img_bala = pygame.image.load("/home/anderson-josue/Documents/Python/Day10/bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 5
bala_visible = False

# Variable puntuacion
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)

texto_x = 10
texto_y = 10

# texto final
fuente_final = pygame.font.Font("freesansbold.ttf", 40)


def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (250, 250))


# Mostrar puntaje
def puntaje_sc(x, y):
    texto = fuente.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Funcion jugador
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Funcion dispara bala
def disparar(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Funcion colision
def colision(enemigo_x, enemigo_y, bala_x, bala_y):
    distancia = ((enemigo_x - bala_x) ** 2 + (enemigo_y - bala_y) ** 2) ** 0.5
    if distancia < 27:
        return True
    else:
        return False


# loop del juego
se_ejecuta = True

while se_ejecuta:
    # Imagen fondo
    pantalla.blit(fondo, (0, 0))

    # Movimiento
    # Iterar evento
    for evento in pygame.event.get():
        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound(
                    "/home/anderson-josue/Documents/Python/Day10/disparo.mp3"
                )
                sonido_bala.play()
                nueva_bala = {"x": jugador_x, "y": jugador_y, "velocidad": -5}
                balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar(bala_x, bala_y)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicacion
    jugador_x += jugador_x_cambio

    # Manterne bordes jugador x
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicacion enemigo
    for e in range(cantidad_enemigos):
        # fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] += enemigo_x_cambio[e]

        # Manterne bordes enemigo x
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1
            enemigo_y[e] += enemigo_y_cambio[e]
        # colision
        for bala in balas:
            colision_bala_enemigo = colision(
                enemigo_x[e], enemigo_y[e], bala["x"], bala["y"]
            )
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound(
                    "/home/anderson-josue/Documents/Python/Day10/Golpe.mp3"
                )
                sonido_colision.play()
                bala_y = 500
                bala_visible = False
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)
    # if bala_y <= -64:
    #     bala_y = 500
    #     bala_visible = False
    # if bala_visible:
    #     disparar(bala_x, bala_y)
    #     bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    # Mostrar puntaje
    puntaje_sc(texto_x, texto_y)

    # actualizar
    pygame.display.update()
