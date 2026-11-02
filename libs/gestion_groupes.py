import argparse
import random
import sys
from openpyxl import load_workbook, Workbook
from exceptions import AllErrors, InputTypeError


class Player:
    def __init__(self, player_name_from_datasheet):
        self.ranking= player_name_from_datasheet

    @property
    def ranking(self) -> str:
        return self.__ranking

    @ranking.setter
    def ranking(self, value) -> None:
        self.__ranking = AllErrors.verify_str(value, field_name="Nom")


def generate_groups(input_file, output_file_path, group_length=3):
    try:
        # Validation initiale du fichier via notre classe d'erreurs
        AllErrors.verify_if_file_exists(input_file)
        
        wb = load_workbook(input_file)
        entry_sheet = wb.active

        players = []
        for row in entry_sheet.iter_rows(min_col=1, max_col=1, values_only=True):
            value = row[0]
            if value is not None:
                try:
                    # Protection par la classe Joueur
                    player = Player(value)
                    players.append(player.ranking)
                except InputTypeError as e:
                    print(f"Cellule invalide : {e}")

        if not players:
            print("Erreur: Le fichier de données est vide et ne contient aucun joueur valide.")
            sys.exit(1)

        if players[0].lower() in ["nom", "prenom", "numero_de_licence", "club", "date_naissance", "tableau_demande", "classement"]:
            players.pop(0)

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
                cell_value = group[row_idx] if row_idx < len(group) else ""
                sheet_out.cell(
                    row=row_idx + 2, column=col_idx + 1, value=cell_value
                )

        wb_out.save(output_file_path)
        print(f"✅ Succès ! Le fichier des groupes a été créé : {output_file_path}")

    except:
        print(f"Erreur : Une erreur inattendue s'est produite:\n")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generation des groupes de joueurs")
    
    parser.add_argument(
        "input", 
        nargs="?", 
        default=" joueurs.xlsx", 
        help="le fichier Excel contenant les joueurs."
    )
    parser.add_argument("-o", "--output", default="generated_groups.xlsx", help="Nom du fichier Excel de sortie.")
    parser.add_argument("-t", "--taille", type=int, default=3, help="Nombre de joueurs par groupe.")

    args = parser.parse_args()
    generate_groups(args.input, args.output, args.taille)


if __name__ == "__main__":
    main()
