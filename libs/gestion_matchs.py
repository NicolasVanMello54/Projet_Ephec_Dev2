
from pathlib import Path
from openpyxl import load_workbook


# Chemin du fichier Excel créé par Donald
FICHIER_GROUPES = Path(__file__).resolve().parent / "generated_groups.xlsx"


class Match:
    """Représente un match entre deux joueurs."""

    def __init__(self, joueur1, joueur2, poule):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.poule = poule
        self.score1 = None
        self.score2 = None


def creer_matchs(fichier_excel=FICHIER_GROUPES):
    """Lit les poules Excel et crée tous les matchs."""

    matchs = []

    if not fichier_excel.exists():
        raise FileNotFoundError(
            f"Le fichier des groupes est introuvable : {fichier_excel}"
        )

    wb = load_workbook(fichier_excel, data_only=True)
    feuille = wb.active

    # Chaque colonne représente une poule
    for colonne in range(1, feuille.max_column + 1):

        nom_poule = feuille.cell(row=1, column=colonne).value

        if nom_poule is None:
            continue

        joueurs = []

        # Récupérer les joueurs de la poule
        for ligne in range(2, feuille.max_row + 1):
            joueur = feuille.cell(row=ligne, column=colonne).value

            if joueur is not None and str(joueur).strip():
                joueurs.append(str(joueur).strip())

        # Créer chaque confrontation une seule fois
        for i in range(len(joueurs)):
            for j in range(i + 1, len(joueurs)):
                match = Match(
                    joueurs[i],
                    joueurs[j],
                    nom_poule
                )
                matchs.append(match)

    wb.close()
    return matchs


def saisir_scores(matchs):
    """Permet de saisir manuellement les scores des matchs."""

    for numero, match in enumerate(matchs, start=1):

        print("\n------------------------------")
        print(f"{match.poule} - Match {numero}")
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
                print("Erreur : entrez des nombres entiers.")

    return matchs


def afficher_matchs(matchs):
    """Affiche les matchs et leurs scores."""

    print("\n========== RÉSULTATS DES MATCHS ==========")

    for match in matchs:
        print(
            f"{match.poule} : "
            f"{match.joueur1} {match.score1} - "
            f"{match.score2} {match.joueur2}"
        )


def main():
    """Lance la création des matchs et la saisie des scores."""

    try:
        matchs = creer_matchs()

        if not matchs:
            print("Aucun match n'a été trouvé.")
            return

        print(f"{len(matchs)} matchs ont été créés.")

        for match in matchs:
            print(
                f"{match.poule} : "
                f"{match.joueur1} contre {match.joueur2}"
            )

        saisir_scores(matchs)
        afficher_matchs(matchs)

    except (FileNotFoundError, PermissionError, OSError) as erreur:
        print(f"Erreur lors de la lecture du fichier Excel : {erreur}")


if __name__ == "__main__":
    main()
