
import argparse
import os
from openpyxl import load_workbook, Workbook


class Match:
    def __init__(self, joueur1, joueur2, poule):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.poule = poule
        self.score1 = None
        self.score2 = None


def creer_matchs(fichier_excel):
    """Lit les poules et crée les matchs entre les joueurs."""

    if not os.path.isfile(fichier_excel):
        raise FileNotFoundError(
            f"Le fichier {fichier_excel} n'existe pas."
        )

    workbook = load_workbook(fichier_excel, data_only=True)
    feuille = workbook.active

    matchs = []

    try:
        for colonne in feuille.iter_cols(min_row=1, values_only=True):
            joueurs = [
                valeur for valeur in colonne
                if valeur is not None
            ]

            if len(joueurs) < 3:
                continue

            nom_poule = joueurs[0]
            joueurs = joueurs[1:]

            for i in range(len(joueurs)):
                for j in range(i + 1, len(joueurs)):
                    match = Match(
                        joueurs[i],
                        joueurs[j],
                        nom_poule
                    )
                    matchs.append(match)

    finally:
        workbook.close()

    return matchs


def saisir_scores(matchs):
    """Demande les scores de chaque match."""

    for numero, match in enumerate(matchs, start=1):

        print(f"\nMatch {numero} - {match.poule}")
        print(f"{match.joueur1} contre {match.joueur2}")

        while True:
            try:
                score1 = int(input(f"Score de {match.joueur1} : "))
                score2 = int(input(f"Score de {match.joueur2} : "))

                if score1 < 0 or score2 < 0:
                    print("Les scores ne peuvent pas être négatifs.")
                    continue

                match.score1 = score1
                match.score2 = score2
                break

            except ValueError:
                print("Veuillez entrer des nombres entiers.")


def enregistrer_excel(matchs, fichier_sortie):
    """Enregistre les matchs et leurs scores dans Excel."""

    workbook = Workbook()
    feuille = workbook.active
    feuille.title = "Matchs et scores"

    feuille.append([
        "Poule",
        "Joueur 1",
        "Score 1",
        "Score 2",
        "Joueur 2"
    ])

    for match in matchs:
        feuille.append([
            match.poule,
            match.joueur1,
            match.score1,
            match.score2,
            match.joueur2
        ])

    # Ajuste automatiquement la largeur des colonnes
    for colonne in feuille.columns:
        largeur = max(
            len(str(cell.value)) if cell.value is not None else 0
            for cell in colonne
        )
        feuille.column_dimensions[
            colonne[0].column_letter
        ].width = largeur + 3

    workbook.save(fichier_sortie)
    workbook.close()

    print(
        f"\nLes matchs et les scores ont été enregistrés "
        f"dans {fichier_sortie}."
    )


def creer_parser():
    """Configure les arguments de la ligne de commande."""

    parser = argparse.ArgumentParser(
        description="Gestion des matchs du tournoi de tennis de table"
    )

    parser.add_argument(
        "-f",
        "--fichier",
        required=True,
        help="Fichier Excel contenant les poules"
    )

    return parser


def main():
    parser = creer_parser()
    args = parser.parse_args()

    try:
        matchs = creer_matchs(args.fichier)

        if not matchs:
            print("Aucun match n'a été trouvé.")
            return

        print(f"\nNombre de matchs créés : {len(matchs)}")

        saisir_scores(matchs)

        enregistrer_excel(
            matchs,
            "resultats_tournoi.xlsx"
        )

    except (FileNotFoundError, PermissionError, OSError) as erreur:
        parser.error(str(erreur))


if __name__ == "__main__":
    main()
