import cv2
import face_recognition as fr
import os
import numpy as np
from datetime import datetime

# crear base de datos
ruta = "Day14/Empleados"
mis_imagenes = []
nombre_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}/{nombre}")
    mis_imagenes.append(imagen_actual)
    nombre_empleados.append(os.path.splitext(nombre)[0])


# codficar imagenes
def codificar(imagenes):
    # crear lista codificada
    lista_codificada = []

    # pasar todas las iamgenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada


# registrar ingresos
def registrar_ingresos(persona):
    f = open("Day14/registro.csv", "r+")
    lista_datos = f.readlines()
    nombre_registro = []
    for linea in lista_datos:
        ingreso = linea.split(",")
        nombre_registro.append(ingreso[0])

    if persona not in nombre_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime("%H:%M:%S")
        f.writelines(f"\n{persona},{string_ahora}")


lista_empleados_codificado = codificar(mis_imagenes)

# tomar una imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# leer imagen de la camara
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    # reconocer cara en captura
    cara_captura = fr.face_locations(imagen)

    # codificar cara captura
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coincidencia
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificado, caracodif)
        distancias = fr.face_distance(lista_empleados_codificado, caracodif)

        indice_coincidencias = np.argmin(distancias)

        # mostrar coincidencias si las hay
        if distancias[indice_coincidencias] > 0.6:
            print("No oincide con ninguno de nuestros empleados")
        else:
            #  buscar el nombre del empleado
            nombre = nombre_empleados[indice_coincidencias]

            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(
                imagen,
                nombre,
                (x1 + 6, y2 - 6),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2,
            )

            registrar_ingresos(nombre)

            # mostrar la imagen obtenida
            cv2.imshow("Imagen Web", imagen)

            # mantener ventan abierta
            cv2.waitKey(0)
 