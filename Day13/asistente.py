import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar nuestro microfono y devolver el audio comotexto
def trasformar_audio_en_texto():
    # almacenar recognizer en variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:
        # tiempo de espera
        r.pause_threshold = 0.5

        # informar que comenzo la grabacion
        print("ya puedes hablar")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio, language="es-ar")

            # prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # devolver pedido
            return pedido

        # en caso de que no comprenda el audio
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("ups, no entendi")

            # devolver error
            return "sigo esperando"

        # en caso de no resolver el pedido
        except sr.RequestError:
            # prueba de que no comprendio el audio
            print("ups, no hay servicio")

            # devolver error
            return "sigo esperando"

        # error inesperado
        except:
            # prueba de que no comprendio el audio
            print("ups, algo ha salido mal")

            # devolver error
            return "sigo esperando"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    for voice in engine.getProperty("voices"):
        if "spanish" in voice.name.lower() or "es" in str(voice.languages).lower():
            engine.setProperty("voice", voice.id)
            break

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario con nombres de dias
    calendario = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo",
    }

    # decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# informar que hora es
def pedir_hora():

    # crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # decir la hora
    hablar(hora)

# saludo incial
def saludo_inicial():

    # crear variabel con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas Noches'
    elif 6<= hora.hour < 13:
        momento = 'Buenos Dias'
    else:
        momento = 'Buenas Tardes'

    # decir saludo
    hablar(f'{momento} Hola, que molestas?')


# funcion central del asistente
def pedir_cosas():

    # activar saludo inicial
    saludo_inicial()

    # variable corte
    comenzar = True

    # loop central
    while comenzar:

        # activar el micro y guardar el pedido en un string
        pedido = trasformar_audio_en_texto().lower()

        if 'abrir' in pedido:
            hablar('Abriendo')
            webbrowser.open('https://www.youtube.com/')
            continue
        elif 'navegador' in pedido:
            hablar('Abriendo')
            webbrowser.open('https://www.google.com/')
            continue
        elif 'dia' in pedido:
            pedir_dia()
            continue
        elif 'hora' in pedido:
            pedir_hora()
            continue
        elif 'wikipedia' in pedido:
            hablar('Wiki')
            pedido = pedido.replace('wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        elif 'internet' in pedido:
            pedido = pedido.replace('internet', '')
            pywhatkit.search(pedido)
            hablar('Esto encontre: ')
            continue
        elif 'reproducir' in pedido:
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke())
            continue
        elif 'acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon':'AMZN', 'google': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('No molestes')
                continue
        elif 'adios' in pedido:
            hablar('Me la saco jose delgado')
            break

pedir_cosas()
