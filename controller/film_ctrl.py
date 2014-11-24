from domain.film import Film
from domain.val_film import FilmValidator
from repository.film_repo import FilmRepo


class FilmCtrl():
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def add(self, id, titlu, descr):
        x = Film(id, titlu, descr)

        self.__val.validate(x)
        self.__repo.add(x)

    def remove(self, id):
        self.__repo.remove(id)

    def update(self, id, titlu, descr):
        x = Film(id, titlu, descr)
        self.__repo.update(x)

    def getAll(self):
        return self.__repo.getAll()


# # TESTS

def tests():
    repo = FilmRepo()
    val = FilmValidator()

    ctrl = FilmCtrl(val, repo)

    ctrl.add(1, "Film 1", "Actiune")

    assert len(ctrl.getAll()) == 1

    ctrl.add(2, "Film 2", "Alta actiune")
    ctrl.update(2, "Film x", "Epic...")

    x = ctrl.getAll()

    assert x[2].getDescriere() == "Epic..."


tests()