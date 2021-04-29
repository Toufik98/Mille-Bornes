import random
from os import systeme

from Attaque import Attaque
from Botte import Botte
from Carte import Protection, Effet
from Defense import Defense
from Distance import Distance
from Joueur import Joueur


def init_cartes():
    liste_carte = [Botte("Vehicule prioritaire", Protection.PRIORITAIRE),
                   Botte("Citerne d'essence", Protection.CAMION_CITERNE), Botte("Increvable", Protection.INCREVABLE),
                   Botte("As du volant", Protection.AS_DU_VOLANT)]

    for i in range(0, 5):
        liste_carte.append(Attaque("Feu rouge", Effet.FEU_ROUGE))
        if i < 4:
            liste_carte.append(Attaque("Limite de vitesse", Effet.LIMITATION_DE_VITESSE))
        if i < 3:
            liste_carte.append(Attaque("Panne d'essence", Effet.PANNE_ESSENCE))
            liste_carte.append(Attaque("Crevaison", Effet.CREVAISON))
            liste_carte.append(Attaque("Accident", Effet.ACCIDENT_DE_LA_ROUTE))

    for i in range(0, 14):
        liste_carte.append(Defense("Feu vert", Effet.FEU_ROUGE))
        if i < 6:
            liste_carte.append(Defense("Fin de limite de vitesse", Effet.LIMITATION_DE_VITESSE))
            liste_carte.append(Defense("Essence", Effet.PANNE_ESSENCE))
            liste_carte.append(Defense("Roue de secours", Effet.CREVAISON))
            liste_carte.append(Defense("Reparations", Effet.ACCIDENT_DE_LA_ROUTE))

    for i in range(0,12):
        if i < 10 :
            liste_carte.append(Distance("25 bornes",25))
            liste_carte.append(Distance("50 bornes", 50))
            liste_carte.append(Distance("75 bornes", 75))
        if i < 4:
            liste_carte.append(Distance("200 bornes", 200))
        liste_carte.append(Distance("100 bornes", 100))

    return liste_carte

def init_liste_joueurs(nb_joueur):
    print("Entrez le nom des joueurs du plus jeune au plus vieux")
    liste_joueurs = []
    for i in range(0, nb_joueur):
        nom_joueur = input(f"Entrez le nom du joueur {i+1} :")
        liste_joueurs.append(Joueur(nom_joueur))
        break_line()
    return liste_joueurs

def break_line():
    print("")
    print("----------------------------------\n")



def main():
    liste_carte = init_cartes()
    random.shuffle(liste_carte)
    pioche = liste_carte
    fausse = []
    bon_nb_joueur = False

    while not bon_nb_joueur:
        nb_joueur = int(input("Entrez le nombre de joueur:"))
        if nb_joueur < 2 or nb_joueur > 4:
            print(f"Vous ne pouvez pas jouer à {nb_joueur} joueurs. Une partie se déroule en 2-4 joueurs")
        else:
            bon_nb_joueur = True

    break_line()

    liste_joueurs = init_liste_joueurs(nb_joueur)

    for j in liste_joueurs:
        j.prendre_carte(pioche,fausse,6)

    jeu_continue = True
    tour_jouee = 0
    carte_jouee = 0
    while jeu_continue:
        system('cls')
        print(f"C'est au tour de {liste_joueurs[tour_jouee].nom} !")
        system('pause')
        break_line()

        if not liste_joueurs[tour_jouee].prendre_carte(pioche,fausse,1):
            jeu_continue =  False
        print(liste_joueurs[tour_jouee])
        liste_joueurs[tour_jouee].afficher_main()
        print("8. Jeter une carte")
        print("")
        jeu_erreur = False

        while True:
            jeu_erreur = False
            while True:
                jeu_erreur = False
                carte_jouee = int(input("Quelle carte voulez-vous jouer ? "))
                if carte_jouee < 1 or carte_jouee > 8:
                    break_line()
                    print("Vous ne pouvez pas jouer cette !")
                    jeu_erreur = True
                if not(carte_jouee < 1 or carte_jouee > 8):
                    break
            if carte_jouee == 8:
                carte_jouee = int(input("Quelle carte voulez-vous jeter ? "))
                if carte_jouee < 1 or carte_jouee > 7:
                    break_line()
                    print("Vous ne pouvez pas jeter cette carte !")
                    print("")
                    jeu_erreur = True
                else:
                    liste_joueurs[tour_jouee].jetter_carte(carte_jouee, fausse)
            else:
                jeu_erreur = not liste_joueurs[tour_jouee].jouer_carte(carte_jouee, liste_joueurs)
            if not jeu_erreur:
                break
        if liste_joueurs[tour_jouee].a_gagne():
            print(f"{liste_joueurs[tour_jouee].nom} a gagne!")
            liste_joueurs.pop(tour_jouee)
            nb_joueur -= 1
            system('pause')
        elif not liste_joueurs[tour_jouee].replay():
            if nb_joueur == tour_jouee + 1:
                tour_jouee = 0
            else:
                tour_jouee += 1
        if nb_joueur == 1:
            jeu_continue = False
    print("La partie est terminee")







if __name__ == '__main__':
    main()