descriptions = [
 "Streaming de música en vivo con covers y composiciones",
 "Charla interactiva con la audiencia sobre series y películas",
 "Jugamos a juegos retro y charlamos sobre su historia",
 "Exploramos la mejor música de los 80s y 90s",
 "Programa de entretenimiento con noticias y curiosidades del mundo gamer",
 "Sesión de charla con invitados especiales del mundo del streaming",
 "Música en directo con improvisaciones y peticiones del chat",
 "Un espacio para charlar relajada sobre tecnología y cultura digital",
 "Exploramos el impacto de la música en los videojuegos clásicos"
]

palabras = {"entretenimiento": 0, "música": 0, "charla": 0, "del": 0}

for desc in descriptions:
    for d in desc.split(" "):
        d = d.lower()
        if d in palabras:
            palabras[d] += 1

print(f"Menciones de 'música': {palabras['música']} \n Menciones de 'charla': {palabras['charla']} \n Menciones de 'entretenimiento': {palabras['entretenimiento']}")
#Una prueba..
print(f"Menciones de 'del': {palabras['del']}")
