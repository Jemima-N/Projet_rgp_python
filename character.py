import random
from items import ITEMS, Weapon, Potion  # Import des objets et des classes nécessaires

# Classe de base Character
class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self):
        """Méthode générique d'attaque à être redéfinie dans les sous-classes"""
        raise NotImplementedError("La méthode attack doit être implémentée dans la sous-classe.")

    def take_damage(self, damage):
        """Réduit les points de vie d'un personnage"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} subit {damage} points de dégâts. Santé restante : {self.health}.")

# Sous-classe Hero (hérite de Character)
class Hero(Character):
    def __init__(self, name="Bob", health=100, strength=15):
        super().__init__(name, health, strength)  # Appel du constructeur de la classe parent

        self.inventory = [ITEMS["couteau"]]  # Bob commence avec un couteau

    def attack(self):
        """Calcul des dégâts pour le Hero, incluant les armes si disponibles."""
        base_damage = random.randint(10, self.strength)
        weapon_damage = sum(item.damage for item in self.inventory if isinstance(item, Weapon))
        total_damage = base_damage + weapon_damage
        print(f"{self.name} attaque avec {total_damage} points de dégâts.")
        return total_damage

    def use_item(self, item_name):
        """Utilise un objet de l'inventaire si disponible."""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if isinstance(item, Potion):
                    self.health += item.healing
                    self.inventory.remove(item)
                    print(f"{self.name} utilise {item.name} et récupère {item.healing} points de vie.")
                    return
        print(f"{self.name} ne possède pas l'objet {item_name}.")

    def add_item(self, item):
        """Ajoute un objet à l'inventaire du héros."""
        self.inventory.append(item)
        print(f"{item.name} a été ajouté à l'inventaire de {self.name}.")

# Sous-classe Monster (hérite de Character)
class Monster(Character):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)  # Appel du constructeur de la classe parent

    def attack(self):
        """Calcul des dégâts pour le monstre."""
        damage = random.randint(1, self.strength)
        print(f"{self.name} attaque avec {damage} points de dégâts.")
        return damage
