reaccion = int(input("Ingrese su tiempo de reacción en ms: "))
if reaccion < 200:
    print("Categoría: Rápido.")
elif reaccion <= 500:
    print("Categoría: Normal.")
else:
    print("Categoría: Lento.")