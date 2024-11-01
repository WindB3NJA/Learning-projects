from random import randrange

user_new = True
attemps = 8

while attemps != 0:
    if user_new:
        print("Bienvenido al juego adivina el numero")
        user_name = input("Cual es tu nickname?: ")
        hidden_number = randrange(1, 100)
        user_new = False

    user_number = int(input("El numero secreto esta entre el 1 hasta el 100, ¿Cual crees que es el numero?: "))

    attemps -= 1
    if hidden_number == user_number:
        print(f"\n¡Haz acertado el numero secreto {user_name}!, te ha tomado {8 - attemps} intentos")
        break
    elif 0 < user_number <= 100 and user_number < hidden_number:
        print(f"\nOjo {user_name} el numero es más grande (⬆)")
        print(f"Tienes {attemps} intentos")
    elif 0 < user_number <= 100 and user_number > hidden_number:
        print(f"\nOjo {user_name} el numero es más Chico (⬇)")
        print(f"Tienes {attemps} intentos")
    else:
        print("\nCaracter invalido")

