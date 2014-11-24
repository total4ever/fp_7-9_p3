class Console():
    def __init__(self, ctrlClient, ctrlFilm, ctrlGrades):
        self.__ctrlClient = ctrlClient
        self.__ctrlFilm = ctrlFilm
        self.__ctrlRent = ctrlGrades

    def __meniu(self):
        print("1 - Adauga client")
        print("2 - Afisare clienti")

        print("3 - Adauga film")
        print("4 - Afisare filme")

        print("5 - Modifica client")
        print("6 - Sterge client")

        print("7 - Modifica film")
        print("8 - Sterge film")

        print("9 - Inchiriaza")
        print("10 - Returneaza")

        print("inchiriate - Clienti cu filme inchiriate")
        print("top - Cele mai inchiriate filme")

    def __cmd(self):
        return input("Comanda: ")

    def __adaugaClient(self):
        id = int(input("ID client: "))
        name = input("Nume client: ")
        cnp = input("CNP client: ")

        try:
            self.__ctrlClient.add(id, name, cnp)
        except ValueError as msg:
            print(msg)

    def __afiseazaClienti(self):
        lista = self.__ctrlClient.getAll()

        for item in lista:
            x = lista[item]
            print(x.getID(), ":", x.getName(), x.getCNP())

    def __adaugaFilm(self):
        id = int(input("ID film: "))
        nume = input("Titlu: ")
        prof = input("Descriere: ")

        try:
            self.__ctrlFilm.add(id, nume, prof)
        except ValueError as msg:
            print(msg)

    def __afiseazaFilme(self):
        lista = self.__ctrlFilm.getAll()

        for item in lista:
            x = lista[item]
            print(x.getID(), ":", x.getTitlu(), x.getDescriere())

    def __modificaClient(self):
        id = int(input("ID client: "))
        nume = input("Nume nou: ")
        cnp = input("CNP nou: ")

        self.__ctrlClient.update(id, nume, cnp)

    def __stergeClient(self):
        id = int(input("ID client: "))

        self.__ctrlClient.remove(id)

    def __modificaFilm(self):
        id = int(input("ID film: "))
        titlu = input("Titlu nou: ")
        descriere = input("Descriere noua: ")

        self.__ctrlFilm.update(id, titlu, descriere)

    def __stergeFilm(self):
        id = int(input("ID film: "))

        self.__ctrlFilm.remove(id)

    def __inchiriaza(self):
        clientID = int(input("ID client: "))
        filmID = int(input("ID film: "))

        try:
            self.__ctrlRent.rent(clientID, filmID)
        except ValueError as msg:
            print(msg)

    def __returneaza(self):
        clientID = int(input("ID client: "))
        filmID = int(input("ID film: "))

        try:
            self.__ctrlRent.unrent(clientID, filmID)
        except ValueError as msg:
            print(msg)

    def __inchiriate(self):
        for item in self.__ctrlRent.clientiCuFilmeInchiriate():
            print(item.getNumeClient(), item.getInchiriate())

    def __top(self):
        for item in self.__ctrlRent.celeMaiInchiriate():
            print(item.getNumeFilm(), item.getInchiriate())

    def startUI(self):

        while True:
            self.__meniu()
            cmd = self.__cmd()

            if cmd == "1":
                self.__adaugaClient()
            if cmd == "2":
                self.__afiseazaClienti()
            if cmd == "3":
                self.__adaugaFilm()
            if cmd == "4":
                self.__afiseazaFilme()
            if cmd == "5":
                self.__modificaClient()
            if cmd == "6":
                self.__stergeClient()
            if cmd == "7":
                self.__modificaFilm()
            if cmd == "8":
                self.__stergeFilm()
            if cmd == "9":
                self.__inchiriaza()
            if cmd == "10":
                self.__returneaza()

            if cmd == "inchiriate":
                self.__inchiriate()
            if cmd == "top":
                self.__top()