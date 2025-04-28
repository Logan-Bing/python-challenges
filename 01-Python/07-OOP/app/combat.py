def combat(hero, monster):
    print(f"⚔️ Début du combat entre {hero.name} et {monster.name} !")

    while hero.life_points > 0 and monster.life_points > 0:
        hero.attack(monster)
        if monster.life_points <= 0:
            print(f"🏆 {hero.name} a vaincu {monster.name} !")
            break

        monster.bite(hero)  # ou scratch() pour certains monstres
        if hero.life_points <= 0:
            print(f"💀 {monster.name} a vaincu {hero.name} !")
            break
