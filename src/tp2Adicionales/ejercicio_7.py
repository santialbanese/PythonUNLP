import random
import string
from datetime import datetime

def generar_string(longitud):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=longitud))

fecha = datetime.today().date()
f = str(fecha).replace("-", "")
cant_fecha = len(f)
user = input("Ingrese usuario: ")
if len(user) < 15:
    cant = 30 - len(user) - cant_fecha
    print(f"cant: {cant}")
    random_string = generar_string(cant)
    print(f"Código de descuento: {user}-{f}-{random_string}".upper())