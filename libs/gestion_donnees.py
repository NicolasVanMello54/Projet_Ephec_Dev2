from openpyxl import load_workbook
from libs.joueur import Joueur
import os


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

