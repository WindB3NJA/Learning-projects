"""
Módulo calculadora: Contiene una función para ejecutar una calculadora básica.

Funciones:
    calculadora: Ejecuta una calculadora básica que permite realizar operaciones aritméticas simples.
"""


def calculadora():
    """
    Ejecuta una calculadora básica que permite realizar operaciones aritméticas simples.
    Opciones:
    1) Sumar los dos números.
    2) Restar los dos números.
    3) Multiplicar los dos números.
    4) Cambiar los números elegidos.
    5) Apagar calculadora.
    """

    opcion = 0
    while True:
        print("""\nDime, ¿qué quieres hacer?\n 1) Sumar los dos números\n 2) Restar los dos números\n 3) Multiplicar los dos números\n 4) Cambiar los números elegidos\n 5) Apagar calculadora""")
        try:
            opcion = int(input("Elige una opción: "))
            n1 = float(input("Introduce tu primer número: "))
            n2 = float(input("Introduce tu segundo número: "))

            if opcion == 1:
                resultado = n1 + n2
                print(" ")
                print("RESULTADO: La suma de", int(n1), "+", int(n2), "es igual a",
                      int(resultado) if resultado.is_integer() else resultado)
            elif opcion == 2:
                resultado = n1 - n2
                print(" ")
                print("RESULTADO: La resta de", int(n1), "-", int(n2), "es igual a",
                      int(resultado) if resultado.is_integer() else resultado)
            elif opcion == 3:
                resultado = n1 * n2
                print(" ")
                print("RESULTADO: El producto de", int(n1), "*", int(n2), "es igual a",
                      int(resultado) if resultado.is_integer() else resultado)
            elif opcion == 4:
                n1 = float(input("Introduce tu primer número: "))
                n2 = float(input("Introduce tu segundo número: "))
                print("Números cambiados exitosamente.")
            elif opcion == 5:
                break
        except ValueError:
            print("Opción no válida. Por favor, ingresa un número.")

    print("Calculadora apagada.")


# Ejecutar la calculadora
calculadora()
