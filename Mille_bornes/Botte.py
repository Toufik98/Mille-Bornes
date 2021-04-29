from Carte import Carte, Role

#Classe Botte qui herite de la class Carte
class Botte(Carte):
    def __init__(self, nom, protection):
        super().__init__(nom, Role.BOTTE)
        self.__protection = protection

    @property
    def protection(self):
        return self.__protection

    def __str__(self):
        res = super().__str__()
        res += "\t["+ str(self.__protection) + "]"
        return res