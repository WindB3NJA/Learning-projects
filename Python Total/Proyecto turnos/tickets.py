def gen_ticket():
    """
    Generador de numero de tickets
    """
    n = 0
    while True:
        n += 1
        yield n

def usr_ticket(func):
    """
    Decorador para generar el ticket del usuario
    """
    def wrapper(*args):
        return f"Su turno es: {func(*args)} Espere pacientemente hasta su turno"
    return wrapper

# Generamos los tickets para cada sección
Pharmacy = gen_ticket()
Perfumery = gen_ticket()
Cosmetics = gen_ticket()

@usr_ticket
def type_ticket(name_shop):
    """
    Generamos la letra para cada sección
    """
    if name_shop == Pharmacy:
        return f"F - {next(name_shop)}"
    elif name_shop == Perfumery:
        return f"P - {next(name_shop)}"
    elif name_shop == Cosmetics:
        return f"C - {next(name_shop)}"

