from libs.gestion_donnees import lire_joueurs, afficher_joueurs
from libs.gestion_matchs import creer_matchs, saisir_scores, afficher_matchs
from libs.gestion_classements import determiner_vainqueurs_poules
import argparse



def parse_arguments():
    parser = argparse.ArgumentParser(description="Gestion du tournoi de tennis de table")
    parser.add_argument("-a", "--afficher", action="store_true",
                        help="Affiche la liste des joueurs")

    parser.add_argument("-n", "--nom",
                    help="Affiche un seul joueur par son nom")

    parser.add_argument("-l", "--licence",
                        help="Affiche un joueur par son numéro de licence")

    parser.add_argument("-m", "--matchs", action="store_true",
                        help="Lance la saisie des scores et calcule le classement")


    return parser.parse_args()

def main():
    
    args = parse_arguments()
    
    try:

        joueurs = lire_joueurs("data/joueurs.xlsx")
    except FileNotFoundError as erreur:
        print(f"{erreur}")
        return

    if args.licence:
        joueur = joueurs.get(args.licence)
        if joueur:
            print(joueur)
        else:
            print(f"Aucun Joueur avec la licence {args.licence}")
    elif args.nom:
        resultat = []

        for j in joueurs.values():
            if args.nom.lower() in j.nom.lower():
                resultat.append(j)

        if resultat:
            for j in resultat:
                print(j)
        else:
            print(f"Aucun joueur trouvé avec le nom {args.nom}")
        
    elif args.afficher:
        afficher_joueurs(joueurs)

    # si l'option matchs est tapée par l'utilisateur, on joue les fonctions pour montrer le tableau des scores et trouver le vainqueur de chaque poule
    elif args.matchs:
        matchs_crees = creer_matchs()#stocker matchs créés par la fonction de Sophie depuis l'excel d'Ange
        matchs_joues = saisir_scores(matchs_crees)#pour que l'utilisateur encode les scores
        afficher_matchs(matchs_joues)#montrer tableau des scores
        determiner_vainqueurs_poules(matchs_joues)#analyser les poules pour trouver le premier de chacune
    # si l'option matchs est tapée par l'utilisateur, on joue les fonctions pour montrer le tableau des scores et trouver le vainqueur de chaque poule

if __name__ == "__main__":
    main()