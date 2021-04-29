#import des modules pour les classes abstraites et les énums
from abc import ABC 
from enum import Enum

#Enumération qui vas citer les protections possible des cartes bottes
class Protection(Enum):
    AS_DU_VOLANT = 0
    CAMION_CITERNE = 1
    INCREVABLE = 2
    PRIORITAIRE = 3

#Enumeration qui vas permettre définir l'effet et les contres effets des cartes attaques et defenses
class Effet(Enum):
    ACCIDENT_DE_LA_ROUTE = 0
    PANNE_ESSENCE = 1
    CREVAISON = 2
    LIMITATION_DE_VITESSE = 3
    FEU_ROUGE = 4
    RIEN = 5

#Enumeration qui vas definir le role des cartes 
class Role(Enum):
    ATTAQUE = 0
    DEFENSE = 1
    BOTTE = 2
    DISTANCE = 3


#Classe Carte abstraite
class Carte(ABC):
    #Construire une carte à l'aide de son nom et de son role
    def __init__(self, nom, role):
        self.__role = role
        self.__nom = nom
    
    #retourne le role de la carte
    @property
    def role(self):
        return self.__role
    #retourne le nom de la carte
    @property
    def nom(self):
        return self.__nom
    
    #methode toString qui vas permmetre l'affichage depuis un print
    def __str__(self):
        return self.__nom + "[" + str(self.__role) + "]"




