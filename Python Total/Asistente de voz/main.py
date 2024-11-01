import pyttsx3, pywhatkit, pyjokes, webbrowser, datetime, wikipedia
import speech_recognition as sr
import yfinance as yf

# Motor de voz
engine = pyttsx3.init()

# Función para escuchar el micrófono y devolver el texto
def sound_to_text():
    # almacenar el audio en la variable "audio"
    r = sr.Recognizer()

    # config de micrófono
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        # indicar al usuario que puede hablar
        print("Escuchando...")
        # Guardar el audio en la variable "audio"
        audio = r.listen(source)
        text = ""

        try:
            # Traducir mediante google el audio a texto
            text = r.recognize_google(audio, language="es-ES")
            # Imprimir el texto
            print("Has dicho: ", text)
            return text
        # Error de valor desconocido
        except sr.UnknownValueError:
            # Si no se ha podido reconocer el audio
            print("No se ha podido reconocer el audio")
            # Devolver un string del estado
            return "Lo siento, no he podido entender lo que has dicho"
        # Error de conexión
        except sr.RequestError:
            # Si no se ha podido conectar con google
            print("No se ha podido conectar con google")
            # Devolver un string del estado
            return "Lo siento, no he podido conectar con google"
        # Error inesperado
        except:
            # Si no se ha podido realizar la operación
            print("No se ha podido realizar la operación")
            # Devolver un string del estado
            return "Lo siento, no he podido realizar la operación"

# Función para que el asistente hable
def speak(message):
    global engine
    # Configuración de la voz
    spanish = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
    english = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Token\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice", spanish)
    # Hacer que hable el asistente
    engine.say(message)
    engine.runAndWait()

# Función para dar el saludo inicial
def greeting():
    # variable para los datos de hora
    actual_hour = datetime.datetime.now().hour
    if actual_hour < 6 or actual_hour > 20:
        moment ="Buenas noches"
    elif 6 <= actual_hour < 13:
        moment = "Buenos días"
    else:
        moment = "Buenas tardes"
    # Saludo del asistente
    speak(f"{moment}, soy tu asistente virtual, ¿en qué puedo ayudarte?")


# Función para dar el dia de la semana
def give_date():
    # Obtener la fecha actual
    actual_date = datetime.datetime.now()
    # Formatear la fecha
    weekday = actual_date.weekday()
    # Diccionario de días de la semana
    days = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    # Devolver el día de la semana
    speak(f"Hoy estamos a {days[weekday]}")

# Función para dar la hora
def give_hour():
    # Obtener la hora actual
    actual_hour = datetime.datetime.now().strftime("%I:%M %p")
    # Devolver la hora
    speak(f"Son las {actual_hour[1]} horas con {actual_hour[3:5]} minutos {actual_hour[6:]}")

# Funcion central del asistente
def main():
    # Saludo del asistente
    greeting()
    # Bucle infinito
    while True:
        # Escuchar el micrófono y convertirlo a texto
        text = sound_to_text().lower()
        if "abre youtube" in text:
            webbrowser.open("https://www.youtube.com")
            continue
        elif "qué hora es" in text:
            give_hour()
            continue
        elif "qué día es hoy" in text:
            give_date()
            continue
        elif "busca en wikipedia" in text:
            speak("Buscando en wikipedia")
            text = text.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            result = wikipedia.summary(text, sentences=1)
            print(result)
            speak(f"Wikipedia dice: {result}")
            continue
        elif "busca en internet" in text:
            speak("Buscando en internet")
            text = text.replace("busca en internet", "")
            pywhatkit.search(text)
            speak("Esto es lo que he encontrado")
            continue
        elif "reproduce" in text:
            speak("Reproduciendo")
            text = text.replace("reproduce", "")
            pywhatkit.playonyt(text)
            continue
        elif "chiste" in text:
            joke = pyjokes.get_joke("es")
            speak(joke)
            continue
        elif "precio de las acciones de" in text:
            stock = text.split("de")[-1].strip()
            wallet = {"apple": "AAPL", "amazon": "AMZN", "google": "GOOGL", "tesla": "TSLA", "nvidia": "NVDA"}
            try:
                search_stock = wallet[stock]
                search_stock = yf.Ticker(search_stock)
                price = search_stock.info["regularMarketPrice"]
                speak(f"El precio de las acciones de {stock} es de {price} dólares")
                continue
            except:
                speak("No se ha podido encontrar la acción")
                continue
        elif "salir" in text:
            speak("Hasta luego")
            break

main()