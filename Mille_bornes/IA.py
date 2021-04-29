from enum import Enum

from Carte import Effet, Role, Protection
from Distance import Distance
from Joueur import Joueur


class Niveau(Enum):
    FACILE = 0
    MOYEN = 1
    DIFFICILE = 2


class IA(Joueur):
    def __init__(self, nom, mille_bornes, niveau):
        super().__init__(nom , mille_bornes)
        self.__niveau = niveau
        self.__ia = True
        

    @property
    def niveau(self):
        return self.__niveau
    @niveau.setter
    def niveau(self, n):
        if isinstance(Niveau.FACILE,type(n)) or isinstance(Niveau.MOYEN,type(n)) or isinstance(Niveau.DIFFICILE,type(n)):
            if 0 <= n.value <1:
                self.__niveau = n
            else:
                print("Impossible d'appliquer ce niveau ")

    def choice(self):
        trouvee = False
        if self.__niveau == Niveau.FACILE:
            if not self.bloque:
                for carte in self.__main:
                    if isinstance(carte, Distance):
                        if not self.__vitesse_limite and carte.distance < 50:
                            return self.__main.index(carte) + 1
            else:
                if self.__effet == Effet.CREVAISON:
                    for carte in self.__main:
                        if carte.role == Role.BOTTE:
                            if carte.protection == Protection.INCREVABLE:
                                return self.__main.index(carte) + 1

                        if carte.role == Role.DEFENSE:
                            if carte.contre_effet == Effet.CREVAISON:
                                return self.__main.index(carte) + 1
                        return 8

                elif self.__effet == Effet.PANNE_ESSENCE:
                    for carte in self.__main:
                        if carte.role == Role.BOTTE:
                            if carte.protection == Protection.CAMION_CITERNE:
                                return self.__main.index(carte) + 1

                        if carte.role == Role.DEFENSE:
                            if carte.contre_effet == Effet.PANNE_ESSENCE:
                                return self.__main.index(carte) + 1
                        return 8

                elif self.__effet == Effet.ACCIDENT_DE_LA_ROUTE:
                    for carte in self.__main:
                        if carte.role == Role.BOTTE:
                            if carte.protection == Protection.AS_DU_VOLANT:
                                return self.__main.index(carte) + 1

                        if carte.role == Role.DEFENSE:
                            if carte.contre_effet == Effet.ACCIDENT_DE_LA_ROUTE:
                                return self.__main.index(carte) + 1
                        return 8

                elif self.__effet == Effet.FEU_ROUGE:
                    for carte in self.__main:
                        if carte.role == Role.BOTTE:
                            if carte.protection == Protection.PRIORITAIRE:
                                return self.__main.index(carte) + 1

                        if carte.role == Role.DEFENSE:
                            if carte.contre_effet == Effet.FEU_ROUGE:
                                return self.__main.index(carte) + 1
                        return 8
                elif self.__effet == Effet.RIEN:
                    for carte in self.__main:
                        if carte.role == Role.DEFENSE:
                            if carte.contre_effet == Effet.FEU_ROUGE:
                                return self.__main.index(carte) + 1
                        return 8


        return 1

    def jouer_carte_IA(self, carte_selectione, liste_joueur):
        """

        Parameters
        ----------
        carte_selectione : int
            Numero de la carte que le joueur aura selesctionne
        liste_joueur : liste
            Liste des joueurs de la partie

        Returns
        -------
        bool
            Retourne True si tout c est bien passe sinon elle retourne false

        """
        # -1 car le numerotage propose commence par 1
        carte_jouee = self.__main[carte_selectione - 1]
        erreur_jeu = False
        self.__replay = False

        if carte_jouee.role == Role.BOTTE:
            self.__protection.append(carte_jouee.protection)
            if self.est_protege(self.__effet):
                self.__effet = Effet.RIEN
                if self.est_protege(Effet.LIMITATION_DE_VITESSE):
                    self.__vitesse_limite = False
            self.__replay = True
        elif carte_jouee.role == Role.ATTAQUE:
            self.bloque = True
            cible = 0
            for i in range(0, len(liste_joueur)):
                print(f"{i + 1}. {liste_joueur[i].nom}")
            print("Contre qui voulez vous jouer cette carte ?")
            for j in self.__mille_bornes.liste_joueurs:
                if j.effet == Effet.RIEN:
                    cible = self.__mille_bornes.liste_joueurs.index(j) + 1
                    break

            # a completer
            if cible < 1 or cible > len(liste_joueur):
                print("Ce joueur n'existe pas")
                erreur_jeu = True
            elif (liste_joueur[cible - 1].est_protege(carte_jouee.effet) or (
                    liste_joueur[cible - 1].est_affecte() and carte_jouee.effet != Effet.LIMITATION_DE_VITESSE) or
                  liste_joueur[cible - 1].nom == self.__nom):

                print("Ce joueur ne peut pas etre attaque")
                erreur_jeu = True

            if not erreur_jeu:
                liste_joueur[cible - 1].get_attaque(carte_jouee.effet)

        elif carte_jouee.role == Role.DEFENSE:
            if self.__effet == Effet.RIEN:
                if self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                else:
                    print("Vous ne pouvez pas utiliser cette carte car vous n'etes pas attaque")
                    erreur_jeu = True
            elif self.__effet == Effet.FEU_ROUGE:
                self.bloque = False
                if carte_jouee.contre_effet == Effet.FEU_ROUGE:
                    self.__effet = Effet.RIEN
                elif self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                else:
                    print("Vous ne pouvez pas utiliser cette carte car elle ne corrige pas votre attaque")
                    erreur_jeu = False
            elif self.__effet == Effet.LIMITATION_DE_VITESSE:
                if carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__effet = Effet.RIEN
                elif self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                else:
                    print("Vous ne pouvez pas utiliser cette carte car elle ne corrige pas votre attaque")
                    erreur_jeu = True
            elif self.__effet == Effet.PANNE_ESSENCE:
                if carte_jouee.contre_effet == Effet.PANNE_ESSENCE:
                    self.__effet = Effet.RIEN
                elif self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                else:
                    print("Vous ne pouvez pas utiliser cette carte car elle ne corrige pas votre attaque")
                    erreur_jeu = True
            elif self.__effet == Effet.CREVAISON:
                if carte_jouee.contre_effet == Effet.CREVAISON:
                    self.__effet = Effet.RIEN
                elif self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                else:
                    print("Vous ne pouvez pas utiliser cette carte car elle ne corrige pas votre attaque")
                    erreur_jeu = True
            elif self.__effet == Effet.ACCIDENT_DE_LA_ROUTE:
                if carte_jouee.contre_effet == Effet.ACCIDENT_DE_LA_ROUTE:
                    self.__effet = Effet.RIEN
                elif self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                else:
                    print("Vous ne pouvez pas utiliser cette carte car elle ne corrige pas votre attaque")
                    erreur_jeu = True
        elif carte_jouee.role == Role.DISTANCE:
            if self.bloque == False:
                if self.__distance_parcourue + carte_jouee.distance > 1000:
                    print("Vous ne pouvez pas depasser 1000 bornes")
                    erreur_jeu = True
                elif self.__borne_limite == 2 and carte_jouee.distance == 200:
                    print("Vous ne pouvez pas jouer plus de deux cartes 200 bornes")
                    erreur_jeu = True
                elif self.__effet != Effet.RIEN:
                    print("Vous etes attaque, vous ne pouvez toujours pas avancer !")
                    erreur_jeu = True
                elif self.__vitesse_limite and carte_jouee.distance >= 50:
                    print("Vous avez une limite de vitesse, vous ne pouvez pas autant avancer !")
                    erreur_jeu = True
                else:
                    if (self.joueur_possede_feu_vert(self.__main)):
                        self.__distance_parcourue += carte_jouee.distance
                    else:
                        print("Vous ne pouvez pas avancer car vous ne possédez pas un feu vert!!")
                    if carte_jouee.distance == 200:
                        self.__borne_limite += 1
            else:
                print("Vous ne pouvez pas avancer car vous n'avez pas de feu vert")
                erreur_jeu = True

        if erreur_jeu:
            return False
        self.__main.pop(carte_selectione - 1)
        self.__nb_carte -= 1
        return True






