from controller.film_ctrl import FilmCtrl
from controller.client_ctrl import ClientCtrl
from controller.rent_ctrl import RentCtrl
from domain.val_film import FilmValidator
from domain.val_rent import RentValidator
from domain.val_client import ClientValidator
from repository.film_repo import FilmRepo
from repository.rent_repo import RentRepo
from repository.client_repo import ClientRepo
from ui.console import Console

valClient = ClientValidator()
valFilm = FilmValidator()
valGrades = RentValidator()

repoClient = ClientRepo()
repoFilm = FilmRepo()
repoGrade = RentRepo()

ctrlClient = ClientCtrl(valClient, repoClient)
ctrlFilm = FilmCtrl(valFilm, repoFilm)
ctrlRent = RentCtrl(valGrades, repoClient, repoFilm, repoGrade)

console = Console(ctrlClient, ctrlFilm, ctrlRent)

console.startUI()
