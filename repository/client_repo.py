from domain.client import Client


class ClientRepo():
    def __init__(self):
        self.__data = {}

    def add(self, item):

        if item.getID() in self.__data:
            raise ValueError("Client existdent deja")

        self.__data[item.getID()] = item

    def remove(self, id):
        if id in self.__data:
            del self.__data[id]

    def find(self, id):
        if id in self.__data:
            return self.__data[id]

        return None

    def update(self, item):
        if item.getID() in self.__data:
            self.__data[item.getID()] = item
        else:
            raise ValueError("Client inexistent")

    def getAll(self):
        return self.__data

def tests():
    s1 = Client(1, "Vasile", "123")

    repo = ClientRepo()

    repo.add(s1)
    assert len(repo.getAll()) == 1

    x = repo.find(1)
    assert x.getName() == "Vasile"

    s2 = Client(1, "Vasile", "123")

    try:
        repo.add(s2)
        assert False
    except ValueError:
        assert True

    s3 = Client(3, "Vasile", "123")

    repo.add(s3)
    assert len(repo.getAll()) == 2

    repo.update(Client(3, "Gheorghe", "456"))
    assert repo.find(3).getName() == "Gheorghe"

    repo.remove(3)
    assert len(repo.getAll()) == 1


tests()