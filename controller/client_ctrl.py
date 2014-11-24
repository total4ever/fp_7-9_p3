from domain.client import Client
from domain.val_client import ClientValidator
from repository.client_repo import ClientRepo


class ClientCtrl():
    def __init__(self, val, repo):
        self.__val = val
        self.__repo = repo

    def add(self, id, name, cnp):
        x = Client(id, name, cnp)

        self.__val.validate(x)
        self.__repo.add(x)

    def remove(self, id):
        self.__repo.remove(id)

    def update(self, id, nume, cnp):
        x = Client(id, nume, cnp)
        self.__repo.update(x)

    def getAll(self):
        return self.__repo.getAll()


def tests():
    repo = ClientRepo()
    val = ClientValidator()

    ctrl = ClientCtrl(val, repo)

    ctrl.add(1, "Vasile", "123")

    assert len(ctrl.getAll()) == 1

    ctrl.add(2, "Ion", "456")
    ctrl.update(2, "Gheorghe", "789")

    x = ctrl.getAll()

    assert x[2].getName() == "Gheorghe"

tests()