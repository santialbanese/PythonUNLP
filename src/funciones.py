def todasRondas(rounds, tablaFinal, numRonda):
    for round in rounds:
        maxPtsRound = 0
        userMax = None
        for user in tablaFinal:
            pts = 0
            if round[user]["deaths"]:
                tablaFinal[user]["deaths"] += 1
                pts -= 1
            tablaFinal[user]["kills"] += round[user]["kills"]
            tablaFinal[user]["assists"] += round[user]["assists"]
            pts += round[user]["kills"] * 3 + round[user]["assists"] 
            if pts > maxPtsRound:
                maxPtsRound = pts
                userMax = user
            tablaFinal[user]["puntos"] += pts
        tablaFinal[userMax]["mvps"] += 1
        numRonda += 1
        puntosTotales(tablaFinal, numRonda, userMax)
    return tablaFinal

def puntosTotales(tablaFinal, numRonda, userMax): 
    tablaOrdenada = sorted(tablaFinal.items(), key=lambda x: x[1]["puntos"], reverse=True)
    if numRonda == 5:
        print("Ranking final: ")
    else:
        print(f"Ronda {numRonda}:")
    print("Jugador  ", " Kills  ", " Asistencias  ", " Muertes  ", " MVPs  ", " Puntos  ")
    print("-"*60)
    for user, stats in tablaOrdenada:
        print(f"{user}       {stats['kills']}           {stats['assists']}           {stats['deaths']}          {stats['mvps']}        {stats['puntos']}")
    print(f"MVP RONDA {numRonda}: {userMax}")
    print("-"*60)