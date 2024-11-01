import os, re, time, pathlib
from datetime import datetime

def buscar_numero_serie(contenido):
    patron = r'N[a-zA-Z]{3}-\d{5}'
    match = re.search(patron, contenido)
    return match.group(0) if match else None

def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

def recorrer_directorio(ruta_raiz):
    resultados = []
    for carpeta, subcarpetas, archivos in os.walk(ruta_raiz):
        for archivo in archivos:
            if archivo.endswith('.txt'):
                ruta_archivo = os.path.join(carpeta, archivo)
                contenido = leer_archivo(ruta_archivo)
                numero_serie = buscar_numero_serie(contenido)
                if numero_serie:
                    resultados.append((archivo, numero_serie))
    return resultados

def imprimir_resultados(resultados, duracion):
    fecha_hoy = datetime.now().strftime('%d/%m/%y')
    print('----------------------------------------------------')
    print(f'Fecha de búsqueda: {fecha_hoy}\n')
    print('ARCHIVO\t\tNRO. SERIE')
    print('-------\t\t----------')
    for archivo, numero_serie in resultados:
        print(f'{archivo}\t\t{numero_serie}')
    print(f'\nNúmeros encontrados: {len(resultados)}')
    print(f'Duración de la búsqueda: {round(duracion)} segundos')
    print('----------------------------------------------------')

# Programa principal
ruta_raiz = pathlib.Path(os.getcwd()) / "Mi_Gran_Directorio"
inicio = time.time()

resultados = recorrer_directorio(ruta_raiz)

fin = time.time()
duracion = fin - inicio

imprimir_resultados(resultados, duracion)
