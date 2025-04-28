from character import Character

class Monster(Character):
    def bite(self, target):
        print(f"{self.name} mord {target.name} et lui inflige 5 dégâts")
        target.take_damage(5)
