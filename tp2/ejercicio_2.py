#2)
titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]
max = -1
for aux in titles:
    cant = 0
    for _ in aux.split():
        cant += 1
    if cant > max:
        max = cant
        max_title = aux
print(f"el titulo con mas palabras es: {max_title}")