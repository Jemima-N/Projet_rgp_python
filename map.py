import random
from character import Hero
from character import Monster  

class Map:
    def __init__(self):
        self.carte = [
            ["#", "#", ".", ".", "#"],
            [".", ".", "@", ".", "."],
            ["#", ".", ".", ".", "#"],
            [".", ".", "#", ".", "."],
            [".", ".", ".", ".", "."]
        ]
        self.x = 2  # Position initiale du joueur sur l'axe x
        self.y = 1  # Position initiale du joueur sur l'axe y
        self.hero = Hero()  
        self.game_over = False
        self.monstres_vaincus = 0
        self.boss_final = False  
    def afficher_carte(self):
        for i, ligne in enumerate(self.carte):
            for j, case in enumerate(ligne):
                if i == self.y and j == self.x:
                    print("@", end=" ")  
                else:
                    print(case, end=" ")  
            print()

    def deplacer(self, direction):
        if direction == "north" and self.y > 0:
            self.y -= 1
        elif direction == "south" and self.y < len(self.carte) - 1:
            self.y += 1
        elif direction == "east" and self.x < len(self.carte[0]) - 1:
            self.x += 1
        elif direction == "west" and self.x > 0:
            self.x -= 1
        else:
            print("Vous ne pouvez pas vous déplacer dans cette direction.")
            return

        self.afficher_carte()  # Afficher la carte après déplacement
        if not self.game_over:
            self.evenement_aleatoire()  # Gérer les événements après chaque déplacement

    def evenement_aleatoire(self):
        """Génère un événement aléatoire lorsque le joueur se déplace."""
        if self.monstres_vaincus < 3:
            evenement = random.choice([None, "combat", "objet", "rien"])
        else:
            evenement = random.choice([None, "combat", "rien"])

        if evenement == "combat":
            print("Un monstre apparaît ! Préparez-vous à combattre !")
            self.combat()
        elif evenement == "objet":
            objet = self.trouver_objet()  
            print(f"Vous avez trouvé un objet : {objet}")
        else:
            print("Rien d'intéressant ici.")

    def trouver_objet(self):
        """Retourne un objet aléatoire parmi une liste d'objets."""
        objets = ["Épée magique", "Bouclier en bois", "Potion de soin", "Boussole en argent", "Carte du trésor"]
        return random.choice(objets)

    def combat(self):
        """Simule un combat contre un monstre avec un type spécifique."""
        # Dictionnaire avec les caractéristiques des monstres
        monstres_stats = {
            "Goblin": {"health": 50, "attack_power": 10},
            "Orc": {"health": 80, "attack_power": 15},
            "Vampire": {"health": 70, "attack_power": 12},
            "Dragon": {"health": 150, "attack_power": 30},
            "Griffon": {"health": 100, "attack_power": 25}
        }

        # Si le boss final est activé, crée le boss
        if self.boss_final:
            type_monstre = "Boss Final"
            monstre = Monster(type_monstre, 200, 50)  # Boss Final avec 200 PV et 50 de puissance d'attaque
        else:
            # Choisir un monstre au hasard et récupérer ses stats
            type_monstre = random.choice(list(monstres_stats.keys()))
            stats = monstres_stats[type_monstre]
            monstre = Monster(type_monstre, stats["health"], stats["attack_power"])

        print(f"Vous êtes en combat contre un {monstre.name} !")
        
        # Combat jusqu'à ce qu'un des deux (le joueur ou le monstre) perde toute sa vie
        while self.hero.health > 0 and monstre.health > 0:
            action = input("Choisissez une action: 'attaquer' ou 'fuir' : ").lower()
            if action == "attaquer":
                degats_joueur = self.hero.attack()
                degats_monstre = monstre.attack()
                monstre.take_damage(degats_joueur)
                self.hero.take_damage(degats_monstre)
                print(f"Vous infligez {degats_joueur} dégâts au {monstre.name}.")
                print(f"Le {monstre.name} vous inflige {degats_monstre} dégâts.")
                print(f"Vie du joueur: {self.hero.health} | Vie du {monstre.name}: {monstre.health}")
            elif action == "fuir":
                print("Vous avez fui le combat.")
                return
            else:
                print("Action non valide.")
        
        if self.hero.health > 0:
            print(f"Vous avez vaincu le {monstre.name} !")
            self.monstres_vaincus += 1
            if self.monstres_vaincus == 3:
                self.boss_final = True
                print("Vous avez battu tous les monstres. Le Boss Final apparaît !")
        else:
            print(f"Vous avez été vaincu par le {monstre.name}...")
            self.game_over = True  # Fin du jeu après la défaite


