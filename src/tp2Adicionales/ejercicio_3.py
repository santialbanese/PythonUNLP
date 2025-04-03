#3)
rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo.
Evita el spam. No publiques enlaces sospechosos o repetitivos.
No compartas información personal.
Usa los canales adecuados para cada tema.
Sigue las instrucciones de los moderadores."""

user = input("ingrese una palabra: ").lower()
rules = rules.split("\n")
for rule in rules:
    exist = False
    for word in rule.split():
        if word.strip(".").lower() == user:
            exist = True
    if(exist):
        print(f" - {rule}")