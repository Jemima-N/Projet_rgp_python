class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

class Potion(Item):
    def __init__(self, name, description, healing):
        super().__init__(name, description)
        self.healing = healing

class Armor(Item):
    def __init__(self, name, description, defense):
        super().__init__(name, description)
        self.defense = defense

class Compass(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

class Scroll(Item):
    def __init__(self, name, description, spell_effect):
        super().__init__(name, description)
        self.spell_effect = spell_effect


knife = Weapon(name="Couteau", description="Un petit couteau, pratique pour se défendre.", damage=5)
healing_potion = Potion(name="Potion de soin", description="Une potion qui soigne 20 points de vie.", healing=20)
armor = Armor(name="Armure légère", description="Une armure qui offre une protection modérée.", defense=10)
compass = Compass(name="Boussole", description="Une boussole qui permet de s'orienter dans la forêt.")
scroll_fireball = Scroll(name="Parchemin de Boule de Feu", description="Un parchemin contenant un sort puissant de boule de feu.", spell_effect="Attaque de feu 30 points de dégâts")
magic_sword = Weapon(name="Épée magique", description="Une épée puissante qui inflige des dégâts élevés.", damage=30)
wooden_shield = Armor(name="Bouclier en bois", description="Un bouclier simple mais utile, offrant une protection modeste.", defense=5)
silver_compass = Compass(name="Boussole en argent", description="Une boussole en argent, plus précise pour l'orientation.")
treasure_map = Item(name="Carte du trésor", description="Une carte mystérieuse menant à un trésor caché.")

# Liste d'objets potentiellement trouvables
ITEMS = {
    "couteau": knife,
    "potion": healing_potion,
    "armure": armor,
    "boussole": compass,
    "parchemin_feu": scroll_fireball,
    "épée_magique": magic_sword,
    "bouclier_boix": wooden_shield,
    "boussole_argent": silver_compass,
    "carte_tresor": treasure_map
}

