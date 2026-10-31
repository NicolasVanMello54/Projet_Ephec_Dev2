from libs.gestion_donnees import lire_joueurs, afficher_joueurs
import argparse



def parse_arguments():
    parser = argparse.ArgumentParser(description="Gestion du tournoi de tennis de table")
    parser.add_argument("-a", "--afficher", action="store_true",
                        help="Affiche la liste des joueurs")
    return parser.parse_args()

def main():
    args = parse_arguments()
    try:

        joueurs = lire_joueurs("data/joueurs.xlsx")
    except FileNotFoundError as erreur:
        print(f"{erreur}")
        return

    if args.afficher:
        afficher_joueurs(joueurs)

   



if __name__ == "__main__":
    main()