def round_ranking(scores):
    totals = {chef: sum(notes.values()) for chef, notes in scores.items()}
    ranking = sorted(totals.items(), key=lambda chef: chef[1], reverse=True)
    winner = ranking[0]
    ranking = dict(ranking)
    return winner, ranking

def start_contest(rounds):

    # Inicializo a los chefs, asumiendo que siempre van a ser los mismos cinco
    # y que "rounds" contiene al menos un elemento.

    ranking = {}
    for chef in rounds[0]["scores"].keys():
        ranking[chef] = {"total": 0, "won": 0, "best": 0, "average": 0}

    # Iteración, ronda por ronda

    index = 1
    for current in rounds:
        round_winner, current_ranking = round_ranking(current["scores"])
        position = 1

        print(f"\nRonda {index} - {current["theme"]}")
        print(f"  Ganador: {round_winner[0]} ({round_winner[1]} pts)")
        for key, value in current_ranking.items():
            print(f"    [{position}] {key} - {value} pts")

            # Actualizo el ranking global

            ranking[key]["total"] += value
            if (position == 1):
                ranking[key]["won"] += 1
            if (ranking[key]["best"] < value):
                ranking[key]["best"] = value
            ranking[key]["average"] = (ranking[key]["total"] / index)

            position += 1

        index += 1

    # Ordeno el ranking de forma descendente
    ranking = sorted(ranking.items(), key=lambda item: item[1]["total"], reverse=True)
    ranking = dict(ranking)
    return ranking