from Carte import Effet, Protection, Role

#Classe Joueur qui vas permettre de modeliser un Joueur de Mille borne
class Joueur:
    #cree un joueur en prenant comme parametre son nom
    def __init__(self, nom, mille_bornes):
        
        #la liste des attributs :
            
        #Le nom du joueur
        self.__nom = nom
        #le nombre de carte du joueur
        self.__nb_carte = 0
        #les cartes de la main du joueur
        self.__main = []
        #Liste des protections qui sont declenche par les cartes bottes
        self.__protection = []
        #L'effet courant des cartes parades (attaque et defense)
        self.__effet = Effet.FEU_ROUGE
        #la distance total parcourue lors d'une partie
        self.__distance_parcourue = 0
        #compteur de borne 200km  utilisees
        self.__borne_limite = 0
        #variable indiquant si on est attaque par une carte de limitation de vitesse
        self.__vitesse_limite = False
        #variable indiquant si on a le droit de rejouer une autre carte
        self.__replay = False
        #variable indiquant si le joueur est bloquee
        self.bloque = True

        self.mile_bornes = mille_bornes

    #definition des getters pour les attributs privees
    @property
    def nom(self):
        return self.__nom

    def nb_carte(self):
        return self.__nb_carte

    def main(self):
        return self.__main

    def protection(self):
        return self.__protection

    def effet(self):
        return self.__effet

    def distance_parcourue(self):
        return self.__distance_parcourue

    def borne_limite(self):
        return self.__borne_limite

    def vitesse_limite(self):
        return self.__vitesse_limite

    def replay(self):
        return self.__replay
    
    #methode to_string du joueur
    def __str__(self):
        effets = ["Accident","Panne d'essence", "Crevaison", "Limite de vitesse","Feu rouge", "Non"]
        protections = ["As du volant", "Citerne d'essance", "Increvable","Vehicule prioritaire"]
        res = self.__nom + " a atteint: " + str(self.__distance_parcourue)+ " km" + "\n"
        res += "Limite de vitesse: " + str(self.__vitesse_limite) + "\n"
        res += "Attaque ?" + str(effets[self.__effet.value]) + "\n"
        res += "Bottes (s) : [ "
        for i in range(len(self.__protection)):
            res += protections[self.__protection[i].value]
        res += " ]"
        res += "\n" + str(self.__replay)
        return res

    def __eq__(self, other):
        if not isinstance(other, Joueur):
            return False
        if self is other:
            return True
        if self.__effet != other.__effet:
            return False
        if self.__nom != other.__nom:
            return False
        if self.__main != other.__main:
            return False
        if self.__nb_carte != other.__nb_carte:
            return False
        if self.__protection != other.__protection:
            return False
        if self.__distance_parcourue != other.__distance_parcourue:
            return False
        if self.__borne_limite != other.__borne_limite:
            return False
        if self.__vitesse_limite != other.__borne_limite:
            return False
        if self.__replay != other.__replay:
            return False
        return True
    
    #affiche les cartes du joueur une par une 
    def afficher_main(self):
        try:
            for i in range(0, self.__nb_carte):
                print(f"{i+1}. {self.__main[i].nom}")
        except :
            print(f"J'ai {len(self.__main)}")
            print(self.__nb_carte)
    
    #ajoute une carte à la main du joueur 
    def prendre_carte(self, pioche, fausse, nb_carte):
        for i in range(0,nb_carte):
            self.__main.append(pioche[0])
            pioche.pop(0)
            self.__nb_carte += 1
            
            #verifie si la pioche est vide
            if(len(pioche) == 0):
                if(len(fausse) !=0 ):
                    pioche = fausse
                else:
                    print("Il n'y a plus de carte")
                    return False
        return True
    
    
    # def joueur_possede_feu_vert(self, main):
    #     """
        

    #     Parameters
    #     ----------
    #     main : liste
    #         DESCRIPTION.

    #     Returns
    #     -------
    #     bool
    #         DESCRIPTION.

    #     """
    #     for i in self.__main:
    #         if i.role == Role.DEFENSE:
    #             if i.contre_effet == Effet.FEU_ROUGE:
    #                 return True
    #     return False
    
    
    #Jouer la carte selesctionne
    def jouer_carte(self, carte_selectione, liste_joueur):
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
            cible = 0
            for i in range(0, len(liste_joueur)):
                print(f"{i+1}. {liste_joueur[i].nom}")
            print("Contre qui voulez vous jouer cette carte ?")
            cible = int(input())
            #a completer
            if cible < 1 or cible > len(liste_joueur):
                print("Ce joueur n'existe pas")
                erreur_jeu = True
            elif (liste_joueur[cible - 1].est_protege(carte_jouee.effet) or ( liste_joueur[cible - 1].est_affecte() and carte_jouee.effet != Effet.LIMITATION_DE_VITESSE ) or liste_joueur[cible - 1].nom == self.__nom):
                #print(f"l'effet du joueur est : {self.__effet}")
                #print(f"Les protections : {self.__protection}")
                #print(f"liste_joueur[cible - 1].est_protege(carte_jouee.effet): {liste_joueur[cible - 1].est_protege(carte_jouee.effet)}")
                #print(f"liste_joueur[cible - 1].est_affecte:  {liste_joueur[cible - 1].est_affecte()}")
                #print(f"carte_jouee.effet != Effet.LIMITATION_DE_VITESSE: {carte_jouee.effet != Effet.LIMITATION_DE_VITESSE}")
                #print(f"liste_joueur[cible - 1].nom == self.__nom: {liste_joueur[cible - 1].nom == self.__nom}")
                print("Ce joueur ne peut pas etre attaque")
                erreur_jeu = True

            if not erreur_jeu:
                liste_joueur[cible - 1].get_attaque(carte_jouee.effet)


        elif carte_jouee.role == Role.DEFENSE:
            if self.__effet == Effet.RIEN:
                if self.__vitesse_limite and carte_jouee.contre_effet == Effet.LIMITATION_DE_VITESSE:
                    self.__vitesse_limite = False
                elif carte_jouee.contre_effet == Effet.FEU_ROUGE:
                    self.bloque = False
                else: 
                    print("Vous ne pouvez pas utiliser cette carte car vous n'etes pas attaque")
                    erreur_jeu = True
            elif self.__effet == Effet.FEU_ROUGE :
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
                    self.__distance_parcourue += carte_jouee.distance
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

    #defausser une carte
    def jetter_carte(self, carte_selectione, fausse):
        """
        

        Parameters
        ----------
        carte_selectione : int
           Numero de la carte que le joueur aura selesctionne.
        fausse : liste
            Liste des cartes jettees 

        Returns
        -------
        None.

        """
        fausse.append(self.__main[carte_selectione - 1])
        self.__main.pop(carte_selectione - 1)
        self.__nb_carte = self.__nb_carte - 1

    #Recevoir une attaque d'un autre joueur
    def get_attaque(self, effet):
        self.bloque = True
        if effet != Effet.LIMITATION_DE_VITESSE:
            self.__effet = effet
        else:
            self.__vitesse_limite = True
    
    #Retourne True si le joueur est protege par l'effet en argument
    def est_protege(self, effet):
        if effet == Effet.FEU_ROUGE:
            if Protection.PRIORITAIRE in self.__protection:
                return True
            else:
                return False
        elif effet == Effet.LIMITATION_DE_VITESSE:
            if Protection.PRIORITAIRE in self.__protection:
                return True
            else:
                return False
        elif effet == Effet.PANNE_ESSENCE:
            if Protection.CAMION_CITERNE in self.__protection:
                return True
            else:
                return False
        elif effet == Effet.CREVAISON:
            if Protection.INCREVABLE in self.__protection:
                return True
            else:
                return False
        elif effet == Effet.ACCIDENT_DE_LA_ROUTE:
            if Protection.AS_DU_VOLANT in self.__protection:
                return True
            else:
                return False
    
    #Retourne Vraie si le joueur n est pas affectee sinon retourne Faux
    def est_affecte(self):
        if self.__effet != Effet.RIEN:
            return True
        return False
    #Verifie si le joueur a gagnee
    def a_gagne(self):
        if self.__distance_parcourue == 1000:
            return False
    #faire rejouer le joueur 
    def re_jouer(self):
        if self.__replay:
            self.__replay = False
            return True
        else:
            return False
