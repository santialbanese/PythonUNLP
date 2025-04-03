rounds = [
 {
#1ra ronda
 'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
 'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
 'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
#2da ronda
 'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
 'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
 'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
 'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
 'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
 },
 {
#3er ronda
 'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
 'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
 'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
 'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
#4ta ronda
 'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
 'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
 'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
 'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
 },
 {
#5ta ronda
 'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
 'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
 'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
 'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
 'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
 }
]

tablaFinal = {
 'Shadow': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0},
 'Blaze': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0},
 'Viper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0},
 'Frost': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0},
 'Reaper': {'kills': 0, 'assists': 0, 'deaths': 0, 'mvps': 0, 'puntos': 0}
}
def todasRondas():
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
    return tablaFinal


def puntosTotales(): 
    tablaOrdenada = sorted(tablaFinal.items(), key=lambda x: x[1]["puntos"], reverse=True)
    print("Ranking final: ")
    print("Jugador  ", " Kills  ", " Asistencias  ", " Muertes  ", " MVPs  ", " Puntos  ")
    print("-"*60)
    for user, stats in tablaOrdenada:
        print(f"{user}       {stats['kills']}           {stats['assists']}           {stats['deaths']}          {stats['mvps']}        {stats['puntos']}")
    print("-"*60)