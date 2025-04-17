
def horse_racing_format(horses: list[str]) -> None:
    # Inverser la list avec .reverse()
    horses.reverse()

    total = len(horses)
    # Faire une boucle sur les horse return avec index
    for i, horse in enumerate(horses):
        horses[i] = f"{total - i}-{horse}!"

horses = ["Abricot du Laudot", "Black Caviar", "Brigadier Gerard"]
horse_racing_format(horses)
print(horses)
