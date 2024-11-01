"""
    El juego del ahoracdo con vidas
"""

import random as rd

lista_palabras = [
    "abecedario", "abogado", "aceituna", "acuario", "aeropuerto", "agricultura",
    "albahaca", "alfabeto", "almohada", "amistad", "anaranjado", "antena",
    "apreciar", "arbol", "arquitectura", "ascensor", "atardecer", "auditorio",
    "aurora", "aventura", "ayuntamiento", "bailarina", "barco", "biblioteca",
    "bicicleta", "binocular", "blusa", "bocadillo", "bodega", "bosque", "botella",
    "bromista", "bucanero", "bufanda", "buho", "caballero", "cachorro", "cadena",
    "cafeteria", "calendario", "camara", "campana", "canasta", "candado", "canguro",
    "cansancio", "cantar", "capitan", "caravana", "carpintero", "cartera",
    "castillo", "catedral", "cebolla", "celular", "cementerio", "ceramica",
    "cereza", "cerveza", "charco", "chef", "chimenea", "chocolate", "ciencia",
    "cientifico", "cine", "ciudad", "clavel", "cocina", "cohete", "coleccion",
    "comedia", "cometa", "comida", "comision", "companero", "computadora",
    "concierto", "construccion", "copa", "corazon", "corbata", "corona",
    "cosmonauta", "criatura", "crucero", "cuaderno", "cuchara", "cuento",
    "cultura", "cuota", "curiosidad", "danzar", "deporte", "desayuno", "diamante",
    "diccionario", "dinosaurio", "diversion", "dormitorio", "duda", "educacion",
    "elefante", "emocion", "enciclopedia", "energia", "enfermero", "entrevista",
    "equipo", "escuela", "espejo", "esquiador", "estadio", "estrella", "euforia",
    "evolucion", "excursion", "experiencia", "explorador", "fabrica", "familia",
    "fantasia", "farmacia", "ferrocarril", "festival", "fidelidad", "figura",
    "filosofia", "flauta", "flor", "foca", "fotografia", "fragancia", "fruta",
    "galaxia", "galeria", "gallo", "ganador", "gaviota", "gemelos", "geografia",
    "gigante", "gimnasio", "globo", "golondrina", "gorro", "granja", "gratitud",
    "guitarra", "gusano", "habilidad", "hamburguesa", "harina", "helado",
    "herramienta", "heroe", "hielo", "historia", "hoguera", "hogar", "hoja",
    "hormiga", "hospital", "hotel", "humor", "idea", "iglesia",
    "imaginacion", "impresora", "insecto", "instrumento", "invento", "isla",
    "jabon", "jardin", "jirafa", "jornada", "joven", "juguete", "jungla",
    "kilogramo", "kilometro", "koala", "lampara", "lenguaje", "leyenda",
    "libertad", "libro", "limonada", "lince", "literatura", "luz", "madera",
    "madrugada", "maestro", "magia", "maleta", "mamifero", "manzana", "maraton",
    "mariposa", "marisco", "mascara", "medicina", "melodia", "memoria",
    "mercado", "meteorito", "mezcla", "milagro", "mineral", "minuto",
    "montana", "museo", "musica", "naranja", "navegante", "neblina", "necesidad",
    "negocio", "nieve", "nino", "noche", "nube", "oasis", "oceano", "oficina",
    "orquesta", "oveja", "pajaro", "palacio", "paleta", "pantalon", "paquete",
    "paraguas", "parque", "partitura", "paseo", "patineta", "pecera", "pelota",
    "pelicula", "pestana", "piano", "piedra", "pintura", "planeta", "planta",
    "plato", "pluma", "poesia", "poeta", "policia", "pollo", "portal", "pradera",
    "profesor", "programa", "proyecto", "puente", "queso", "radiografia",
    "rapido", "raton", "refrigerador", "reino", "reloj", "resfriado", "respuesta",
    "rey", "rincon", "rio", "robot", "rosa", "rumbo", "ruta", "sabiduria",
    "safari", "salud", "sandwich", "saxofon", "secreto", "semilla", "serpiente",
    "silla", "sirena", "sitio", "sol", "sonrisa", "sueno", "supermercado",
    "surco", "tabla", "tambor", "teatro", "tecnologia", "telescopio",
    "templo", "tenedor", "tesoro", "tiempo", "tigre", "tiza", "tornillo",
    "torre", "tren", "trompeta", "tronco", "tubo", "turismo", "uvas", "vacaciones",
    "valle", "vampiro", "ventana", "verdura", "viento", "villa", "violin",
    "volcan", "yate", "yogur", "zanahoria", "zoologico"
]

vidas = 6

def eleccion_de_palabra():
    return str(rd.choices(lista_palabras)[0])

def mostrar_guiones(palabra_oculta):
    """
    la funcion es encargada de tomar el string de la palabra oculta y convertirla en una lista separada con guiones
    """
    i = 0 # contador de elementos de lista
    palabra_oculta = list(palabra_oculta)
    palabra_guion_oculta = list(palabra_oculta)
    for letra in palabra_guion_oculta:
        palabra_guion_oculta[i] = "_"
        i += 1

    return palabra_oculta, palabra_guion_oculta


def encontrar_indices(palabra, letra_buscada):
    indices = [indice for indice, letra in enumerate(palabra) if letra == letra_buscada]
    return indices


def empezar_jugada(palabra_oculta, palabra_guion_oculta):
    global vidas
    print("Bienvenido al juego del ahorcado")
    while vidas > 0:
        print(f"""{palabra_guion_oculta}
> Tienes {vidas} vidas.""")
        letra_usuario = list(input("Introduzca letra o palabra: ").lower())
        for letra in letra_usuario:
            if letra in palabra_oculta:
                print(f"\nHaz encontrado la letra [{letra}] de la palabra! ")
                for numero_indice in encontrar_indices(palabra_oculta, letra):
                    palabra_guion_oculta[numero_indice] = letra
                if palabra_guion_oculta == palabra_oculta:
                    return print("Haz terminado el juego!")
            else:
                vidas -= 1
                if vidas == 0:
                    return print("Ya no tienes más vidas")


def iniciar_juego():
    palabra_ronda = mostrar_guiones(eleccion_de_palabra())
    empezar_jugada(palabra_ronda[0], palabra_ronda[1])



#iniciar el juego
iniciar_juego()