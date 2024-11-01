# Calculadora de temperatura en Fahrenheit y en Celcuis
# Aqui se le pide al usuario en que tipo de temperatura desea realizar la convercion.
respuesta = input("""Bienvenido a la calculadora de Fahrenheit(ºF) a Celcius(ºC) o de Celcius(ºC) a Fahrenheit(ºF) 
-C) Celcius(ºC) a Fahrenheit(ºF) 
-F)Fahrenheit(ºF) a Celcius(ºC)
Ingrese la opcion que desea realizar:""")
if respuesta in ("c", "C"):
    print("Usted a seleccionado la opcion Celcuis(ºC) a Fahrenheit(ºF)")
    temperatura = float(input("Ingrese la temperatura:"))
    Formula_fahrenheit = round((temperatura * 1.8) + 32, 2)
    print(f"{Formula_fahrenheit}ºF")
elif respuesta in ("f", "F"):
    print("Usted a seleccionado la opcion Fahrenheit(ºF) a Celcius(ºC)")
    temperatura = float(input("Ingrese la temperatura:"))
    Formula_fahrenheit = round((temperatura-32) / 1.8, 2)
    print(f"{Formula_fahrenheit}ºC")
else:
    print("Lamentablemente no se puede realizar la opcion digitada")
