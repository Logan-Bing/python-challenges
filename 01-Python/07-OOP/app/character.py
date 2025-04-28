
class Character:
    def __init__(self, name, level=1, life_points=100, inventory=None):
        self.name = name
        self.level = level
        self.life_points = life_points
        self.inventory = inventory if inventory is not None else []

    def display_infos(self):
        print("🧙‍♂️ Character Stats")
        print(f"📛 Name: {self.name}")
        print(f"🎖️  Level: {self.level}")
        print(f"❤️  Life points: {self.life_points}")

    def attack(self, target):
        print(f"{self.name} attaque {target.name} et lui inflige 10 dégâts")
        target.take_damage(10)

    def take_damage(self, amount):
        self.life_points -= amount
        if self.life_points < 0:
            self.life_points = 0
        print(f"{self.name} a maintenant {self.life_points} points de vies")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name} ajouter à l'inventaire de {self.name}")

    def show_inventory(self):
        print(f"🎒 Inventaire de {self.name}")
        for item in self.inventory:
            print(f"- {item.name} : {item.effect}")

    def crier(self, sound="Aaaaargh !"):
        return sound

    @classmethod
    def since_text(cls, str):
        name, level, pv = str.split(",")
        return cls(name, int(level), int(pv))

    @staticmethod
    def is_alive(life_points):
        return life_points > 0
