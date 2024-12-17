from game import Game

def afficher_menu():
    print("Bienvenue Bob, nous vous attendions!")
    print("1. Create a new game")
    print("2. Load a saved game (Not available)")  
    print("3. About")
    print("4.Exit")

def afficher_instructions():
    print("\n--- Instructions ---")
    print("Bob, nous comptons sur vous!")
    print("Utilisez les commandes pour vous déplacer, explorer, et combattre des monstres.")
    print("Votre mission? Combattre les sbires du boss final ainsi que lui-même... enfin... si vous y parvenez.\n")

def introduction():
    """Affiche l'histoire de départ."""
    print("Bob se réveille dans une forêt dense et mystérieuse.")
    print("Il a un sac à dos, et à l'intérieur, il trouve un petit couteau.")
    print("Prêt à affronter les dangers de cette forêt, Bob se lève et commence son aventure...\n")

def afficher_about():
    """Affiche des informations sur le jeu."""
    print("\n--- À propos du jeu ---")
    print("Dans ce jeu, vous incarnez Bob, un héros qui doit combattre des monstres pour sauver la forêt et affronter un terrible boss final.")
    print("Explorez, combattez et collectez des objets pour devenir plus fort et vaincre le mal qui menace cet endroit.\n")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option (1, 2, 3 ou 4) : ")

        if choix == "1":
            introduction()  # Afficher l'histoire de départ
            jeu = Game()
            jeu.start()
        elif choix == "2":
            print("La fonctionnalité 'Charger une partie sauvegardée' n'est pas disponible pour le moment.")  # Message d'indisponibilité
        elif choix == "3":
            afficher_about()  # Afficher des informations sur le jeu
        elif choix == "4":
            print("Merci d'avoir joué ! À bientôt.")  # Message de sortie
            break
        else:
            print("Choix invalide. Veuillez entrer 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
