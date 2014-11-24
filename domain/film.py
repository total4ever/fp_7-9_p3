class Film():
    def __init__(self, filmID, titlu, descriere):
        self.__filmID = filmID
        self.__titlu = titlu
        self.__descriere = descriere

    def getID(self):
        return self.__filmID

    def getTitlu(self):
        return self.__titlu

    def getDescriere(self):
        return self.__descriere

    def __eq__(self, other):
        if other == None:
            return False

        return self.getID() == other.getID()

def tests():
    d1 = Film(1, "Epic film", "Cel mai epic film")

    assert d1.getID() == 1
    assert d1.getTitlu() == "Epic film"
    assert d1.getDescriere() == "Cel mai epic film"


tests()

