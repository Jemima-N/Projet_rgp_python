from map import Map

class Game:
    def __init__(self):
        self.running = True
        self.map = Map()

    def start(self):
        print("Bienvenue, aventurier ! Vous êtes prêt à commencer l'aventure !")
        self.map.afficher_carte()
        self.map_navigation()

    def map_navigation(self):
        while self.running:
            if self.map.game_over:
                print("Le jeu est terminé.")
                self.running = False
                break

            direction = input("Entrez une direction (north, south, east, west) ou 'q' pour quitter : ").lower()

            if direction == 'q':
                print("Vous quittez la partie.")
                self.running = False
                break
            elif direction in ["north", "south", "east", "west"]:
                self.map.deplacer(direction)
            else:
                print("Direction invalide. Veuillez entrer 'north', 'south', 'east', 'west', ou 'q' pour quitter.")

# Pour lancer le jeu
if __name__ == "__main__":
    jeu = Game()
    jeu.start()
