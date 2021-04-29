from Carte import Carte, Role

#Classe Distance qui herite de la classe Carte
class Distance(Carte):
    def __init__(self, nom, distance):
        super().__init__(nom, Role.DISTANCE)
        self.__distance = distance

    @property
    def distance(self):
        return self.__distance

    def __str__(self):
        res = super().__str__()
        res += "\t" + str(self.__distance) + "km"
        return res
