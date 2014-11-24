from domain.dtos import RentDTO
from domain.film import Film
from domain.rent import Rent
from domain.client import Client
from domain.val_rent import RentValidator
from repository.film_repo import FilmRepo
from repository.rent_repo import RentRepo
from repository.client_repo import ClientRepo

class RentCtrl():
    def __init__(self, val, clientRepo, filmRepo, rentRepo):
        self.__val = val
        self.__clientRepo = clientRepo
        self.__filmRepo = filmRepo
        self.__rentRepo = rentRepo

    def rent(self, clientID, filmID):
        clt = self.__clientRepo.find(clientID)
        film = self.__filmRepo.find(filmID)

        g = Rent(clt, film)

        self.__val.validate(g)
        self.__rentRepo.add(g)

    def unrent(self, clientID, filmID):
        clt = self.__clientRepo.find(clientID)
        film = self.__filmRepo.find(filmID)

        r = Rent(clt, film)

        self.__rentRepo.remove(r)

    def clientiCuFilmeInchiriate(self):
        lista = self.__rentRepo.getAllDTO()
        final = []

        for x in lista:
            poz = -1

            for i in range(len(final)):
                if x.getClientID() == final[i].getClientID():
                    poz = i

            if poz == -1:
                y = RentDTO(x.getClientID(), x.getFilmID())
                y.incNrInchiriate()

                final.append(y)
            else:
                final[poz].incNrInchiriate()

        for i in range(len(final)):
            final[i].setNumeClient(self.__clientRepo.find(final[i].getClientID()).getName())

        return final

    def celeMaiInchiriate(self):
        lista = self.__rentRepo.getAllDTO()
        final = []

        for x in lista:
            poz = -1

            for i in range(len(final)):
                if x.getFilmID() == final[i].getFilmID():
                    poz = i

            if poz == -1:
                y = RentDTO(x.getClientID(), x.getFilmID())
                y.incNrInchiriate()

                final.append(y)
            else:
                final[poz].incNrInchiriate()

        for i in range(len(final)):
            final[i].setNumeFilm(self.__filmRepo.find(final[i].getFilmID()).getTitlu())

        return final


def tests():
    val = RentValidator()
    clientRepo = ClientRepo()
    filmRepo = FilmRepo()
    rentRepo = RentRepo()

    ctrl = RentCtrl(val, clientRepo, filmRepo, rentRepo)


    clientRepo.add(Client(1, "Paul", "123"))
    clientRepo.add(Client(2, "Paula", "456"))
    clientRepo.add(Client(3, "Gheorghe", "789"))

    filmRepo.add(Film(1, "F1", "d1"))
    filmRepo.add(Film(2, "f2", "d2"))
    filmRepo.add(Film(3, "f3", "d3"))
    filmRepo.add(Film(4, "f4", "d4"))

    ctrl.rent(1, 2)
    ctrl.rent(1, 1)

    ctrl.rent(2, 2)
    ctrl.rent(2, 3)
    ctrl.rent(2, 4)

    ctrl.rent(3, 2)

    try:
        ctrl.rent(1, 1)
        assert False
    except ValueError:
        assert True

tests()