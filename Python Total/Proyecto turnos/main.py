"""
Proyecto: Sistema de turnos
Secciones: Farmacia, Perfumería, Cosméticos
Cada sección tiene su letra inicial y un número que se incrementa en 1 cada vez que se genera un ticket
Ejemplo: F - 1, P - 1, C - 1
"""
# Importamos las clases de tickets para generar los tickets
from tickets import *


try:
    # Creamos un bucle para atender a los usuarios
    while True:
        r = input("Ingrese la sección en la que desea ser atendido: \n1. Farmacia\n2. Perfumería\n3. Cosméticos.\n exit para salir\n> ")
        if r == "1":
            # Imprimimos el ticket de la farmacia
            print(type_ticket(Pharmacy))
        elif r == "2":
            # Imprimimos el ticket de la perfumería
            print(type_ticket(Perfumery))
        elif r == "3":
            # Imprimimos el ticket de cosméticos
            print(type_ticket(Cosmetics))
        elif r == "exit":
            break
# Manejamos la excepción en caso de que el usuario ingrese un valor no numérico
except TypeError:
    print("Por favor, ingrese un número válido.")



