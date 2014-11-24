from domain.film import Film


class FilmValidator():
    def validate(self, disc):
        errors = []

        if disc.getID() < 0:
            errors.append("ID negativ")

        if disc.getTitlu() == "":
            errors.append("Nume vid")

        if disc.getDescriere() == "":
            errors.append("Profesor vid")

        if errors != []:
            raise ValueError(errors)

def tests():
    d1 = Film(-1, "Titlu", "Descr")

    val = FilmValidator()

    try:
        val.validate(d1)
        assert False
    except ValueError:
        assert True

    d2 = Film(1, "", "Descr")
    try:
        val.validate(d2)
        assert False
    except ValueError:
        assert True

    d3 = Film(1, "Nume", "")
    try:
        val.validate(d3)
        assert False
    except ValueError:
        assert True

tests()