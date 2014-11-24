class RentValidator():
    def validate(self, gr):
        errors = []

        if gr.getClient() == None:
            errors.append("Client invalid")

        if gr.getFilm() == None:
            errors.append("Film invalida")

        if errors != []:
            raise ValueError(errors)

