class Client():
    def __init__(self, clientID, nume, cnp):
        self.__clientID = clientID
        self.__nume = nume
        self.__cnp = cnp

    def getID(self):
        return self.__clientID

    def getName(self):
        return self.__nume

    def getCNP(self):
        return self.__cnp

    def __eq__(self, other):
        if other == None:
            return False
        return self.getID() == other.getID()


def tests():
    s1 = Client(1, "Ion", "123")
    s2 = Client(2, "Vasile", "456")
    s3 = Client(1, "Gheroghe", "789")

    assert s1.getID() == 1
    assert s1.getName() == "Ion"
    assert s1.getCNP() == "123"

    assert s1 != s2
    assert s1 == s3

tests()
