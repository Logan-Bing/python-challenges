from character import Character

class Mage(Character):
    def fireball(self, target):
        print(f"🔥 Le mage {self.name} incante une fireball sur {target.name}! -15 PV")
        target.take_damage(15)

    def attack(self, target):
        print(f"Le mage {self.name} lance une boule de feu sur {target.name} et lui inflige 10 dégâts")
        target.take_damage(10)

    def crier(self, sound="Par les flammes éternelles !"):
        return sound
