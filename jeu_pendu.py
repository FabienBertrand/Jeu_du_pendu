import random
import unicodedata #pour convertir les accents

# Fonction pour lire le contenu d'un fichier texte et créer une liste de mots
def creer_liste_de_mots(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        contenu = fichier.read()
        contenu = contenu.replace('\n', ' ')  # Remplacer les sauts de ligne par des espaces pour éviter des mots collés
        contenu = unicodedata.normalize('NFD',contenu)
        contenu = contenu.encode('ascii', 'ignore').decode('ascii') #sert a cpnvertir les lettres avec accents
        mots = contenu.split()  # Diviser le contenu, split() par défaut sépare par les espaces
    return mots


# Fonction qui selectionne un mot aléatoire à partir d une liste de mot
def selectionner_mot_aleatoire(liste_de_mots):
    return random.choice(liste_de_mots)


def jouer_une_partie():
    mot_alea = selectionner_mot_aleatoire(creer_liste_de_mots("mots_pendu.txt"))  # choisi le mot aléatoirement
    nb_vie = 6
    nb_lettre_trouve = 0
    mot_cacher = []
    liste_proposition_joueur = []
    for i in range(len(mot_alea)):  # creer le mot cacher qui suite au proposition révelera au joueur ses lettres
        mot_cacher.append('_')
    print(f"voici le mot a deviner{mot_cacher}")
    while nb_vie > 0 and nb_lettre_trouve != len(mot_alea):  # boucle de game play
        proposition_joueur = input("entrer une lettre")
        if proposition_joueur in mot_alea:
            print(f"Bravo ! la lettre {proposition_joueur} est dans le mot")
            for i in range(len(mot_alea)):
                if proposition_joueur == mot_alea[i]:
                    nb_lettre_trouve += 1
                    mot_cacher[i] = proposition_joueur  # revele la lettre au joueur
            print(f"voici le mot à deviner {mot_cacher}, vous avez {nb_vie} vies restantes")
        else:
            print(f"Raté ! la lettre {proposition_joueur} n'est pas dans le mot")
            nb_vie -= 1
            print(f"voici le mot a deviner {mot_cacher}, vous avez {nb_vie} vies restantes")
        liste_proposition_joueur.append(proposition_joueur)
        liste_proposition_joueur.sort()
        print(f"vous avez déja essayé ces lettre {liste_proposition_joueur}")
    if nb_vie == 0:
        print(f"Vous avez perdu, le mot était {mot_alea}")
    else:
        print(f"Vous avez gagné, le mot était {mot_alea}")
    recommencer = input("Pour recommencer taper True")
    if recommencer:
        return jouer_une_partie()
    else:
        return ("fin du jeu")


print(jouer_une_partie())
