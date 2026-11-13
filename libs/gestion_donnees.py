from openpyxl import load_workbook
from libs.joueur import Joueur
import os
from libs.exceptions import JoueurIntrouvable



def lire_joueurs(chemin_fichier):
    """Permet d'extraire la liste de joueurs et leurs parametres du fichier excel 
    et de la stocker dans le dico "joueurs"
    
    Args:
            chemin_fichier(str): le chemin du fichier joueurs.xlsx qui se trouve normalement
            dans le dossier data
            
    returns:
            dict: dictionnaire des joueurs, clé = numéro de licence
            """

    if not os.path.exists(chemin_fichier):
        raise FileNotFoundError(f"Le fichier {chemin_fichier} est introuvable")



    wb = load_workbook(filename=chemin_fichier)

    feuille = wb.active

    joueurs = {}

    for ligne in feuille.iter_rows(min_row=2):
        nom = ligne[0].value
        prenom = ligne[1].value
        numero_de_licence = ligne[2].value
        club = ligne[3].value
        classement = ligne[4].value
        date_naissance = ligne[5].value
        tableau_demande = ligne[6].value

        joueur = Joueur(nom,prenom,numero_de_licence,club,classement,date_naissance,tableau_demande)
        joueurs[numero_de_licence] = joueur

    return joueurs



def afficher_joueurs(joueurs):
    """ Affiche la liste des joueurs dans le terminal  """
    for joueur in joueurs.values():
        print(joueur)




class TableauJoueurs:
    """Classe qui permet de gérer les joueurs"""
    def __init__(self, chemin_fichier):
        self.chemin_fichier = chemin_fichier
        self.joueurs = lire_joueurs(chemin_fichier)



    def recup_joueur_licence(self, numero_de_licence):
        """Permet de récupérer un joueur à partir de son numéro de licence"""
        
        if numero_de_licence in self.joueurs:
            return self.joueurs[numero_de_licence]
        else:
            raise JoueurIntrouvable(f"Le joueur avec le numéro de licence {numero_de_licence} est introuvable.")

    def recup_joueur_nom_prenom(self, nom, prenom):
        """Permet de récupérer un joueur à partir de son nom et prénom"""
        for joueur in self.joueurs.values():
            if joueur.nom.lower() == nom.lower() and joueur.prenom.lower() == prenom.lower():
                return joueur
        raise JoueurIntrouvable(f"Le joueur avec le nom {nom} et le prénom {prenom} est introuvable.")


    def recup_tous_les_joueurs(self):
        """Permet de récupérer tous les joueurs directement en liste d'objets"""
        return list(self.joueurs.values())

    def recup_joueurs_par_club(self, club):
        """Permet de récupérer tous les joueurs d'un club"""
        joueurs_du_club = []
        for joueur in self.joueurs.values():
            if joueur.club == club:
                joueurs_du_club.append(joueur)
        return joueurs_du_club

    def recup_joueurs_par_tableau(self, tableau):
        """Permet de récupérer tous les joueurs d'un tableau"""
        joueurs_du_tableau = []
        for joueur in self.joueurs.values():
            if joueur.tableau_demande == tableau:
                joueurs_du_tableau.append(joueur)
        return joueurs_du_tableau