from libs.gestion_donnees import lire_joueurs, afficher_joueurs
import argparse



def parse_arguments():
    parser = argparse.ArgumentParser(description="Gestion du tournoi de tennis de table")
    parser.add_argument("-a", "--afficher", action="store_true",
                        help="Affiche la liste des joueurs")

    parser.add_argument("-n", "--nom",
                    help="Affiche un seul joueur par son nom")

    parser.add_argument("-l", "--licence",
                        help="Affiche un joueur par son numéro de licence")

    
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
        resultat = [j for j in joueurs.values()
                    if args.nom.lower() in j.nom.lower()]

        if resultat:
            for j in resultat:
                print(j)
        else:
            print(f"Aucun joueur trouvé avec le nom {args.nom}")
        
    elif args.afficher:
        afficher_joueurs(joueurs)



   



if __name__ == "__main__":
    main()