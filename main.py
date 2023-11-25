import random  # Importer la bibliothèque pour choisir des mots au hasard

# Fonction pour initialiser le jeu
def initialiser():
    print("Bienvenue au jeu du Pendu!")

# Fonction pour choisir un thème (Animaux ou Fruits)
def choix_theme():
    print("Choisissez un thème :")
    print("1. Animaux")
    print("2. Fruits")
    choix = input("Entrez le numéro du thème : ")
    return "Animaux" if choix == "1" else "Fruits"

# Fonction pour choisir un mot au hasard dans le thème sélectionné
def choisir_mot(theme):
    animaux = ["tigre", "lapin", "chat", "koala"]
    fruits = ["mangue", "avocat", "framboise", "pomme"]
    mots = animaux if theme == "Animaux" else fruits
    return random.choice(mots)

# Fonction pour afficher le mot partiellement découvert
def afficher_mot_partiel(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "_ "
    return mot_affiche.strip()

# Fonction pour le choix de jouer à nouveau
def rejouer():
    choix = input("Voulez-vous rejouer? (Oui/Non): ").lower()
    return choix == "oui"

# Fonction principale du jeu
def jeu_pendu():
    initialiser()
    
    while True:  # Boucle infinie pour permettre de rejouer
        theme = choix_theme()
        mot_a_deviner = choisir_mot(theme)
        tentatives_max = len(mot_a_deviner) + 1
        lettres_trouvees = []

        print(f"\nThème choisi : {theme}")
        print("Mot à deviner :", afficher_mot_partiel(mot_a_deviner, lettres_trouvees))

        tentatives = 0

        while tentatives < tentatives_max:
            proposition = input("Proposez une lettre : ").lower()

            if proposition in lettres_trouvees:
                print("Vous avez déjà deviné cette lettre.")
            elif proposition in mot_a_deviner:
                lettres_trouvees.append(proposition)
                print("Bonne devinette!")
            else:
                tentatives += 1
                print(f"Essai incorrect. Essais restants : {tentatives_max - tentatives}")

            mot_partiel = afficher_mot_partiel(mot_a_deviner, lettres_trouvees)
            print("Mot à deviner :", mot_partiel)

            if "_" not in mot_partiel:
                print("Félicitations, vous avez gagné!")
                break

        if "_" in mot_partiel:
            print(f"Désolé, vous avez épuisé tous les essais. Le mot était : {mot_a_deviner}")

        if not rejouer():
            print("Merci d'avoir joué !")
            break

# Appel de la fonction principale pour démarrer le jeu
jeu_pendu()
