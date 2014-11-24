class RentDTO():
    def __init__(self, idClient, idFilm):
        self.__idClient = idClient
        self.__idFilm = idFilm

        self.__numeFilm = ""
        self.__nrInchiriate = 0

        self.__numeClient = ""

    def getClientID(self):
        return self.__idClient

    def getFilmID(self):
        return self.__idFilm

    def getNumeFilm(self):
        return self.__numeFilm

    def getNumeClient(self):
        return self.__numeClient

    def getInchiriate(self):
        return self.__nrInchiriate

    def setNumeFilm(self, x):
        self.__numeFilm = x

    def setNumeClient(self, x):
        self.__numeClient = x

    def incNrInchiriate(self):
        self.__nrInchiriate += 1


