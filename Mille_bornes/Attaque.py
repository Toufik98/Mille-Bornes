from Carte import Carte, Role

#Classe Attaque qui herite de la class Carte
class Attaque(Carte):
    def __init__(self, nom, effet):
        super().__init__(nom, Role.ATTAQUE)
        self.__effet = effet

    @property
    def effet(self):
        return self.__effet

    def __str__(self):
        res = super().__str__()
        res += "\t["+ str(self.__effet) + "]"
        return res

