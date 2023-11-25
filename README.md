# Projet_jeu_des_pendu
Jeu du Pendu
Bienvenue au jeu du Pendu ! Ce programme simple en Python vous permet de jouer au Pendu en présentant entre deux thèmes : Animaux et Fruits.

Commentaire jouer
Exécutez le fichier pendu.pypour démarrer le jeu.
Choisissez un thème en participant au numéro correspondant (1 pour Animaux, 2 pour Fruits).
Devinez les lettres du mot choisi en proposant une lettre à la fois.
Vous avez un nombre limité d'essais pour trouver le mot complet.
Continuez à jouer jusqu'à ce que vous gagniez ou que vous épuisiez tous les essais.
Structure du code
pendu.py: Le fichier principal qui contient le code du jeu.
Fonctions :
initialiser(): Affiche un message de bienvenue.
choix_theme(): Permet au joueur de choisir un thème.
choisir_mot(theme): Choisi un mot au hasard dans le thème sélectionné.
afficher_mot_partiel(mot, lettres_trouvees): Affiche le mot partiellement découvert.
rejouer(): Demander au joueur s'il souhaite rejouer.
jeu_pendu(): La fonction principale qui orchestre le jeu.
Dépendances
Ce jeu utilise la bibliothèque randompour choisir des mots au hasard.

Commentaires
N'hésitez pas à ajouter des commentaires supplémentaires dans le code pour une meilleure compréhension.
