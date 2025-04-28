from monster import Monster

class Goblin(Monster):
    def scratch(self, target):
        print(f"{self.name} griffe {target.name} et lui inflige 5 dégâts")
        target.take_damage(5)

