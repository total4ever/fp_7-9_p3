from domain.client import Client


class ClientValidator():
    def validate(self, cl):
        errors = []

        if cl.getName() == "":
            errors.append("Nume vid")

        if cl.getID() < 0:
            errors.append("ID negativ")

        if cl.getCNP == "":
            errors.append("CNP vid")


        if errors != []:
            raise ValueError(errors)


# # TESTS

def tests():
    val = ClientValidator()

    c1 = Client(-1, "Paul", "123")

    try:
        val.validate(c1)
        assert False
    except ValueError:
        assert True

    c2 = Client(1, "", "")

    try:
        val.validate(c2)
        assert False
    except ValueError:
        assert True


tests()