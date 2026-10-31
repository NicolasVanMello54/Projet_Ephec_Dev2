from datetime import date



class Joueur:
    def __init__(self, nom,prenom,numero_de_licence,club,classement,date_naissance,tableau_demande,score=0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_de_licence = numero_de_licence
        self.__club = club
        self.__classement = classement
        self.__date_naissance = date.fromisoformat(date_naissance)
        self.tableau_demande = tableau_demande
        self.__score = score


    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def prenom(self) -> str:
        return self.__prenom

    @property
    def numero_de_licence(self) -> int:
        return self.__numero_de_licence

    @property
    def date_naissance(self) -> date:
        return self.__date_naissance

    @property
    def age(self) -> int:
        aujourdhui = date.today()
        ans = today.year - self.__date_naissance.year
        if (today.month, today.day) < (self.__date_naissance.month, self.__date_naissance.day):
            ans -= 1
        return ans


    @property
    def score(self) -> int:
        return self.__score

    @property
    def club(self) -> str:
        return self.__club

    @property
    def classement(self) -> str:
        return self.__classement


    def changer_classement(self,classement):
        self.__classement = classement


    def changer_club(self,club):
        self.__club = club
    


    def ajouter_score(self, points):
        if points < 0:
            raise ValueError("On ne peut pas retirer de points !")
        self.__score += points

    def __str__(self):
        return f"{self.prenom} {self.nom} | Licence : {self.numero_de_licence} | Club : {self.club} | Classement : {self.classement} | Score: {self.score}"







