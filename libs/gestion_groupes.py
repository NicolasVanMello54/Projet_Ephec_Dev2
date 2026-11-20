import argparse
import random
import sys
from openpyxl import Workbook
from libs.exceptions import AllErrors
from libs.gestion_donnees import TableauJoueurs




"""
    Répartit aléatoirement les joueurs d'un fichier Excel en poules et enregistre le résultat dans un nouveau fichier Excel.

    PRE :
        - Le fichier d'entrée existe et est au format Excel (.xlsx).
        - Le chemin de sortie est une destination valide.
        - La taille d'une poule est un entier strictement positif (minimum 1).
    POST :
        - Ne retourne rien.
        - Génère un fichier Excel à l'emplacement de sortie contenant les joueurs valides répartis aléatoirement par colonnes (« Poule 1 », « Poule 2 », etc.).
        - Arrête le programme avec un message d'erreur si le fichier d'entrée est introuvable, vide ou invalide.
    """
def generate_groups(input_file, output_file_path, group_length=3):
    try:
        # Validation initiale du fichier via notre classe d'erreurs
        AllErrors.verify_if_file_exists(input_file)

        gestionnaire = TableauJoueurs(input_file)
        players = gestionnaire.recup_tous_les_joueurs()
        if not players:
            print("Erreur: Le fichier de données est vide et ne contient aucun joueur valide.")
            sys.exit(1)


        random.shuffle(players)

        groups = [
            players[i : i + group_length] for i in range(0, len(players), group_length)
        ]

        wb_out = Workbook()
        sheet_out = wb_out.active
        sheet_out.title = "Groups"

        for col_idx, group in enumerate(groups, 1):
            sheet_out.cell(row=1, column=col_idx, value=f"Poule {col_idx}")

        max_rows = max(len(group) for group in groups)
        for row_idx in range(max_rows):
            for col_idx, group in enumerate(groups):
                cell_value = f"{group[row_idx].prenom} {group[row_idx].nom}" if row_idx < len(group) else ""
                sheet_out.cell(
                    row=row_idx + 2, column=col_idx + 1, value=cell_value
                )

        wb_out.save(output_file_path)
        print(f"Succès ! Le fichier des groupes a été créé : {output_file_path}")

    except Exception as e:
        print(f"Erreur : Une erreur inattendue s'est produite : {e}\n")
        sys.exit(1)
  


def main():
    parser = argparse.ArgumentParser(description="Generation des groupes de joueurs")
    
    parser.add_argument(
        "input", 
        nargs="?", 
        default="joueurs.xlsx", 
        help="le fichier Excel contenant les joueurs."
    )
    parser.add_argument("-o", "--output", default="generated_groups.xlsx", help="Nom du fichier Excel de sortie.")
    parser.add_argument("-t", "--taille", type=int, default=3, help="Nombre de joueurs par groupe.")

    args = parser.parse_args()
    generate_groups(args.input, args.output, args.taille)


if __name__ == "__main__":
    main()
