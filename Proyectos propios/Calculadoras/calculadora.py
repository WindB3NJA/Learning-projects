############################### es una calculadora dentro del escript#############################################
# class calculator:
#    def dividir(a,b):
#        return a/b
#    def sumar(c,d):
#        return c+d
#    def restar(f,g):
#        return f-g
#    def multiplicar(h,y):
#        return h*y

# dividir = calculator.dividir
# multiplicar = calculator.multiplicar
# restar = calculator.restar
# sumar = calculator.sumar
###############################################################################################################
# esta caluladora es para la consola y interactua con el usuario
while True:
    request = ""
    a = 0
    b = 0
    print("-"*100)
    print("Puedes realizar las siguientes operaciones aritemticas \n1) Sumar \n2) Restar \n3) Multiplicar \n4) Dividir \n5) Si desea apagar esta maravillosa calculadora")
    request = input("que quieres hacer:")
    if request == "1":
        print("ok, estas sumando")
        a = int(input("dime tu primer numero:"))
        b = int(input("dime tu segundo numero:"))
        resultado_suma = a+b
        print(f"Tu suma es {resultado_suma}")
    elif request == "2":
        print("ok, estas restando")
        a = int(input("Dime tu primer numero:"))
        b = int(input("Dime tu segundo numero:"))
        resultado_resta = a-b
        print(f"Tu resta es {resultado_resta}")
    elif request == "3":
        print("ok, estas multiplicando")
        a = int(input("Dime tu primer numero:"))
        b = int(input("Dime tu segundo numero:"))
        resultado_mulitiplicar = a*b
        print(f"Tu multiplicacion es {resultado_mulitiplicar} ")
    elif request == "4":
        print("ok, estas dividiendo")
        a = int(input("dime tu primer numero:"))
        b = int(input("dime tu segundo numero:"))
        resultado_dividir = a/b
        print(f"Tu Division es {resultado_dividir}")
    elif request == "5":
        break

print("fin de la calculadora")
