from Carte import Carte, Role

#Classe Défense qui herite de la class Carte
class Defense(Carte):
    #Le constructeur prend en parametre le nom et le contre-effet de la carte
    def __init__(self, nom, contre_effet):
        #On fait appel au constructeur de la class mere et on fixe le role à Role.DEFENSE
        super().__init__(nom, Role.DEFENSE)
        self.__contre_effet = contre_effet
    
    #Renvoie le contre effet     
    @property
    def contre_effet(self):
        return self.__contre_effet
    #methode to_string
    def __str__(self):
        #On fait appell à to_string de la classe mere et on continue l'implementation
        res = super().__str__()
        res += "\t["+ str(self.__contre_effet) + "]"
        return res