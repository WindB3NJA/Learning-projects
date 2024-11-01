"""
    Se crea una calculadora consecutiva con el fin de aplicar conocimientos de loops y funciones
"""
# Variables para en control de flujo
bool_while = True
bool_friOpUser = True

# Funcion que se encargara de controlar el flujo de las
# desiciones y operaciones que se dese realizar


def func_opflow(int_choise):
    if int_choise == 1:
        val_num2 = int(input("Digite el Segundo numero:"))
        val_result = val_num1 + val_num2
    elif int_choise == 2:
        val_num2 = int(input("Digite el Segundo numero:"))
        val_result = val_num1 - val_num2
    elif int_choise == 3:
        val_num2 = int(input("Digite el Segundo numero:"))
        val_result = val_num1 * val_num2
    elif int_choise == 4:
        val_num2 = int(input("Digite el Segundo numero:"))
        val_result = val_num1 / val_num2
    else:
        if int_choise == 0:
            return print("Gracias por usar la calculadora")
        else:
            return print("Ingrese una opcion valida")
    return val_result


# Algoritmo
while bool_while is True:
    if bool_friOpUser is True:
        print("Bienvenido a la calculadora consecutiva")
        print("""Usted puede realizar las siguientes operaciones:
        1) Para Sumar
        2) Para Restar
        3) Para Multiplicar
        4) Para Dividir
        0) Para salir de la calculadora""")
        print("-"*50)
        int_choise = int(input("Ingrese una de las opciones:"))
        if int_choise == 0:
            bool_while = False
        val_num1 = int(input("Digite el El Primer numero:"))
        val_result = func_opflow(int_choise)
        val_num1 = val_result
        if val_result is None:
            print("-"*50)
        else:
            print(f"El resultado de la operacion es: {val_result}")
            print("-"*50)
            bool_friOpUser = False
    else:
        print("""Usted puede realizar las siguientes operaciones:
        1) Para Sumar
        2) Para Restar
        3) Para Multiplicar
        4) Para Dividir
        0) Para salir de la calculadora""")
        print("-"*50)
        int_choise = int(input("Ingrese una de las opciones:"))
        if int_choise == 0:
            bool_while = False
        val_num1 = val_result
        print(f"El primer numero es {val_num1}")
        val_result = func_opflow(int_choise)
        if val_result is None:
            print("-"*50)
        else:
            print(f"El resultado de la operacion es: {val_result}")
            print("-"*50)
