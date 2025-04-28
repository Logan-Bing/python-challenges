from character import Character

class Warrior(Character):
    def power_strike(self, target):
        print(f"💥 Le guerrier {self.name} utilise 💪 power strike sur {target.name} et lui inflige 20 dégâts!")
        target.take_damage(20)

    def attack(self, target):
        print(f"Le guerrier {self.name} frappe violemment {target.name} et lui inflige 10 dégâts!")
        target.take_damage(10)

    def crier(self , sound="POUR LA GLOIRE !"):
        return sound



