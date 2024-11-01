from time import sleep
from os import system, name
import random as rd

def clear_console():
    # Verifica el sistema operativo
    if name == 'nt':  # Para Windows
        system('cls')
    else:  # Para sistemas Unix (Linux, macOS, etc.)
        system('clear')

def input_response():
    input("Presione cualquier tecla para continuar \n> ")

class people():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class client(people):
    client_number = rd.randrange(1,1000000)
    client_wallet = 1000.20

    def details_client(self):
        return (f"El cliente {self.name} {self.last_name} con el numero de cuenta {self.client_number},"
                f" Posee en su billetera la cantidad de {self.client_wallet}$")

    def deposit_client(self, int_deposit):
        self.client_wallet += int_deposit

    def withdraw_client(self, int_withdraw):
        self.client_wallet -= int_withdraw

cliente = client(input("Ingrese su nombre: ").title(), input("Ingrese su apellido: ").title())
print("Bienvenido", cliente.name, cliente.last_name, "a su cuenta bancaria\n")
while True:
    client_response = input("1) Ver saldo\n2) Depositar\n3) Retirar\n4) Salir\n> ")
    # 1 VER ESTADO DE CUENTA
    if client_response == "1":
        clear_console()
        print(cliente.details_client())
        input_response()
    # 2 DEPOSITAR
    elif client_response == "2":
        clear_console()
        while True:
            client_money = float(input(f"Ingrese la cantidad que desea ingresar a la cuenta {cliente.client_number}\n> "))
            if client_money >= 1:
                cliente.deposit_client(client_money)
                print("Deposito aprobado")
                break

    # 3 Retirar
    elif client_response == "3":
        clear_console()
        while True:
            client_money = float(input(f"Ingrese la cantidad que desea retirar de la cuenta {cliente.client_number}\n> "))
            if client_money <= cliente.client_wallet:
                cliente.withdraw_client(client_money)
                print("Retiro aprobado")
                break
            else:
                print("Fondos insuficientes")
    # 4 SALIR
    elif client_response == "4":
        clear_console()
        print("Gracias por elegir nuestro servicio")
        input_response()
        break
    else:
        print("Ingrese una opción valida")



