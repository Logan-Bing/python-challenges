from character import Character

class Thief(Character):
    def backstab(self, target):
        print(f"🗡️ Le voleur {self.name} utilise backstap sur {target.name}! -12 PV")
        target.take_damage(12)

    def attack(self, target):
        print(f"Le voleur {self.name} frappe dans le dos de {target.name} et lui inflige 10 dégâts")
        target.take_damage(10)

    def crier(self ,sound="Tu ne m'as pas vu venir..."):
        return sound
