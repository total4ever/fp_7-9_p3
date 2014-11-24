from domain.film import Film
from domain.dtos import RentDTO
from domain.rent import Rent
from domain.client import Client


class RentRepo():
    def __init__(self):
        self.__data = []

    def add(self, rent):
        if self.__exists(rent) == -1:
            self.__data.append(rent)
        else:
            raise ValueError("Asociere existenta")

    def remove(self, rent):
        poz = self.__exists(rent)

        if poz != -1:
            del self.__data[poz]
        else:
            raise ValueError("Asociere inexistenta")

    def __exists(self, rent):
        for i in range(len(self.__data)):
            if self.__data[i] == rent:
                return i

        return -1
    def getAllDTO(self):
        final = []
        for item in self.__data:
            x = RentDTO(item.getClient().getID(), item.getFilm().getID())
            final.append(x)
        return final


def tests():
    c1 = Client(1, "Vaile", "123")
    c2 = Client(2, "Ion", "123")
    c3 = Client(3, "Maria", "123")

    f1 = Film(1, "Godfather", "EPIC")
    f2 = Film(2, "Saw", "Mai epic")

    repo = RentRepo()

    r1 = Rent(c1, f1)
    r2 = Rent(c1, f2)
    r3 = Rent(c2, f1)
    r4 = Rent(c3, f2)

    repo.add(r1)
    repo.add(r2)
    repo.add(r3)
    repo.add(r4)

    assert len(repo.getAllDTO()) == 4

    try:
        repo.remove(Rent(c2, f2))
        assert False
    except ValueError:
        assert True

    repo.remove(r2)

    assert len(repo.getAllDTO()) == 3


tests()