#module pour creer une liste aléaoire de carte
import random
from os import system

#import les fichiers des autres classes
from Attaque import Attaque
from Botte import Botte
from Carte import Protection, Effet
from Defense import Defense
from Distance import Distance
from IA import Niveau, IA
from Joueur import Joueur

#Classe Millebornes qui vas modeliser le jeu
class Millebornes():
    def __init__(self):
        self.__liste_cartes = []
        self.__liste_joueurs = []
        self.__ia = []
        self.pioche = []
        self.fausse = []
        self.__nb_joueur = 0

    @property
    def liste_cartes(self):
        return self.__liste_cartes

    @liste_cartes.setter
    def liste_cartes(self, cartes):
        self.__liste_cartes = cartes

    @property
    def liste_joueurs(self):
        return self.__liste_joueurs
    def nbjoueur(self):
        return self.__nb_joueur

    @liste_joueurs.setter
    def liste_joueurs(self, j):
        self.__liste_joueurs = j




    #initialise les 106 carte du jeu 
    def init_cartes(self):
        self.__liste_cartes = [Botte("Vehicule prioritaire", Protection.PRIORITAIRE),
                               Botte("Citerne d'essence", Protection.CAMION_CITERNE), Botte("Increvable", Protection.INCREVABLE),
                               Botte("As du volant", Protection.AS_DU_VOLANT)]

        for i in range(0, 5):
            self.__liste_cartes.append(Attaque("Feu rouge", Effet.FEU_ROUGE))
            if i < 4:
                self.__liste_cartes.append(Attaque("Limite de vitesse", Effet.LIMITATION_DE_VITESSE))
            if i < 3:
                self.__liste_cartes.append(Attaque("Panne d'essence", Effet.PANNE_ESSENCE))
                self.__liste_cartes.append(Attaque("Crevaison", Effet.CREVAISON))
                self.__liste_cartes.append(Attaque("Accident", Effet.ACCIDENT_DE_LA_ROUTE))

        for i in range(0, 14):
            self.__liste_cartes.append(Defense("Feu vert", Effet.FEU_ROUGE))
            if i < 6:
                self.__liste_cartes.append(Defense("Fin de limite de vitesse", Effet.LIMITATION_DE_VITESSE))
                self.__liste_cartes.append(Defense("Essence", Effet.PANNE_ESSENCE))
                self.__liste_cartes.append(Defense("Roue de secours", Effet.CREVAISON))
                self.__liste_cartes.append(Defense("Reparations", Effet.ACCIDENT_DE_LA_ROUTE))

        for i in range(0,12):
            if i < 10 :
                self.__liste_cartes.append(Distance("25 bornes",25))
                self.__liste_cartes.append(Distance("50 bornes", 50))
                self.__liste_cartes.append(Distance("75 bornes", 75))
            if i < 4:
                self.__liste_cartes.append(Distance("200 bornes", 200))
                self.__liste_cartes.append(Distance("100 bornes", 100))

        return self.__liste_cartes
    
    #affiche un saut à la ligne et un trait
    def break_line(self):
        print("")
        print("----------------------------------\n")
    


    
    #Fait tourner une partie
def partie_jeu(mille_bornes):
    # cree les cartes
    mille_bornes.liste_cartes = mille_bornes.init_cartes()
    # cree une sequence aléatoires des cartes
    random.shuffle(mille_bornes.liste_cartes)
    # la liste des cartes est mises dans la pioche
    mille_bornes.pioche = mille_bornes.liste_cartes
    # on cree une fausse vide
    mille_bornes.fausse = []
    # variable indiquant si on a rentré le bon nombre de joueur
    bon_nb_joueur = False

    # tant qu'on a pas fait rentré le bon nobre de joueur on reboucle
    while not bon_nb_joueur:
        mille_bornes.nb_joueur = int(input("Entrez le nombre de joueur:"))
        if mille_bornes.nb_joueur < 2 or mille_bornes.nb_joueur > 4:
            print(f"Vous ne pouvez pas jouer à {mille_bornes.nb_joueur} joueurs. Une partie se déroule en 2-4 joueurs")
        else:
            bon_nb_joueur = True

        mille_bornes.break_line()

        init_liste_joueurs(mille_bornes)

        # donner 6 cartes pour chaque joueur
    for j in mille_bornes.liste_joueurs:
        j.prendre_carte(mille_bornes.pioche, mille_bornes.fausse, 6)

    jeu_continue = True
    tour_jouee = 0
    carte_jouee = 0

    # Boucle principale qui fait toruner le jeu
    while jeu_continue:
        # netoie le terminal de commande pour ne pas avoir l'historique et la liste des cates des autres joueurs pour eviter les triches
        system('cls')
        print(f"C'est au tour de {mille_bornes.liste_joueurs[tour_jouee].nom} !")

        # On met le terminal en pause jusqu'a à ce que le joueur Voulu apppuie sur une touche
        system('pause')
        mille_bornes.break_line()

        # Le joueur prend une carte
        if not mille_bornes.liste_joueurs[tour_jouee].prendre_carte(mille_bornes.pioche, mille_bornes.fausse, 1):
            # Si le joueur n'y a plus de carte
            jeu_continue = False

        # On affiche les détailles du joueurs courant
        print(mille_bornes.liste_joueurs[tour_jouee])
        # On affiche la main du joueur courant
        mille_bornes.liste_joueurs[tour_jouee].afficher_main()
        print("8. Jeter une carte")
        print("")
        jeu_erreur = False

        # Le joueur choisis quel carte jouer et contre qui oubien quel carte à jetter
        while True:
            jeu_erreur = False
            while True:
                jeu_erreur = False
                if isinstance(mille_bornes.liste_joueurs[tour_jouee], IA):
                    carte_jouee = mille_bornes.liste_joueurs[tour_jouee].choice()

                else:
                    carte_jouee = int(input("Quelle carte voulez-vous jouer ? "))
                    if carte_jouee < 1 or carte_jouee > 8:
                        self.break_line()
                        print("Vous ne pouvez pas jouer cette !")
                        jeu_erreur = True
                if not (carte_jouee < 1 or carte_jouee > 8):
                    break

            # Si le joueur veut jetter une carte
            if carte_jouee == 8:
                if isinstance(mille_bornes.liste_joueurs[tour_jouee], IA):
                    mille_bornes.liste_joueurs[tour_jouee].jetter_carte(1, mille_bornes.fausse)
                else:
                    carte_jouee = int(input("Quelle carte voulez-vous jeter ? "))
                    if carte_jouee < 1 or carte_jouee > 7:
                        self.break_line()
                        print("Vous ne pouvez pas jeter cette carte !")
                        print("")
                        jeu_erreur = True
                    else:
                        mille_bornes.liste_joueurs[tour_jouee].jetter_carte(carte_jouee, mille_bornes.fausse)
            else:
                if isinstance(mille_bornes.liste_joueurs[tour_jouee], IA):
                    jeu_erreur = not mille_bornes.liste_joueurs[tour_jouee].jouer_carte_IA(carte_jouee, mille_bornes.liste_joueurs)
                else:
                    jeu_erreur = not mille_bornes.liste_joueurs[tour_jouee].jouer_carte(carte_jouee,mille_bornes.liste_joueurs)
            if not jeu_erreur:
                break

        # affiche le nom du joueur qui a gagnee
        if mille_bornes.liste_joueurs[tour_jouee].a_gagne():
            print(f"{mille_bornes.liste_joueurs[tour_jouee].nom} a gagne!")
            mille_bornes.liste_joueurs.pop(tour_jouee)
            mille_bornes.nb_joueur -= 1
            system('pause')

        elif not mille_bornes.liste_joueurs[tour_jouee].replay():
            if mille_bornes.nb_joueur == tour_jouee + 1:
                tour_jouee = 0
            else:
                tour_jouee += 1
        if mille_bornes.nb_joueur == 1:
            jeu_continue = False
    print("La partie est terminee")

def init_liste_joueurs(mille_bornes):
    print("Entrez le nom des joueurs du plus jeune au plus vieux")

    for i in range(0, mille_bornes.nb_joueur):
        nom_joueur = input(f"Entrez le nom du joueur {i+1} :")
        est_ia =  int(input("s'agit-il d'une AI (0 / 1) ?"))
        if est_ia == 0:
            mille_bornes.liste_joueurs.append(Joueur(nom_joueur,mille_bornes))
        elif est_ia == 1:
            level = int(input("Quel est le niveau souhaite (0) ?"))
            if level == 0:
                mille_bornes.liste_joueurs.append(IA(nom_joueur, Niveau.FACILE,mille_bornes))
            elif level == 1:
                mille_bornes.liste_joueurs.append(IA(nom_joueur, Niveau.MOYEN,mille_bornes))
            elif level == 2:
                mille_bornes.liste_joueurs.append(IA(nom_joueur, Niveau.DIFFICILE,mille_bornes))
    mille_bornes.break_line()

    
def main():
    #creation du jeu
    jeu = Millebornes()
    partie_jeu(jeu)
    
    
if __name__ == '__main__':
    main()
