from domain.film import Film
from domain.client import Client


class Rent():
    def __init__(self, client, film):
        self.__client = client
        self.__film = film

    def getClient(self):
        return self.__client

    def getFilm(self):
        return self.__film

    def __eq__(self, other):
        if other == None:
            return False

        return self.getClient() == other.getClient() and self.getFilm() == other.getFilm()


def tests():
    c1 = Client(1, "Vasilica", "123")
    f1 = Film(1, "How I", "whatever")

    r1 = Rent(c1, f1)

    assert r1.getClient() == c1
    assert r1.getFilm() == f1

tests()