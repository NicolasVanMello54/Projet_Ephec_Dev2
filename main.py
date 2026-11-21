from libs.gestion_donnees import lire_joueurs, afficher_joueurs
from libs.gestion_matchs import creer_matchs, saisir_scores, enregistrer_excel
from libs.gestion_classements import determiner_vainqueurs_poules, lire_matchs_excel
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
    parser.add_argument("-c", "--classement", action="store_true",
                        help="Calcule et affiche le classement depuis le fichier de résultats Excel")


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
        matchs_crees = creer_matchs("libs/generated_groups.xlsx")
        saisir_scores(matchs_crees)
        enregistrer_excel(matchs_crees, "libs/resultats_tournoi.xlsx")

        matchs_lus = lire_matchs_excel("libs/resultats_tournoi.xlsx")
        determiner_vainqueurs_poules(matchs_lus)

    elif args.classement:
        try:
            matchs_lus = lire_matchs_excel("libs/resultats_tournoi.xlsx")
            determiner_vainqueurs_poules(matchs_lus)
        except FileNotFoundError as erreur:
            print(f"{erreur}")




if __name__ == "__main__":
    main()