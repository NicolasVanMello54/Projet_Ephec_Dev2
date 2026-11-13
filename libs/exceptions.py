import os


class DatasheetError(Exception):
    pass

class InputTypeError(DatasheetError):
    pass

class JoueurIntrouvable(Exception):
    pass

class AllErrors:
    # eviter l'instanciation de la classe AllErrors
    
    """
    Valide et nettoie une donnée sous forme de chaîne de caractères.

    PRE :
        - Le nom du champ est une chaîne de caractères non vide.
    POST :
        - Retourne la donnée convertie en chaîne de caractères et débarrassée des espaces inutiles en début et fin.
        - Lève une exception InputTypeError si la donnée vaut None ou est vide après nettoyage.
    """
    
    @staticmethod
    def verify_str(value, field_name: str) -> str:
        
        if value is None:
            raise InputTypeError(
                f"Erreur: Le champ '{field_name}' ne contient pas de valeur."
            )
            
        # Connversion en chaine et supression des espaces
        clean_value = str(value).strip()
        
        if not clean_value:
            raise InputTypeError(
                f"Erreur: Le champ '{field_name}' est vide après nettoyage."
            )
            
        return clean_value
    
    
    """
        Vérifie l'existence d'un fichier à un emplacement donné.

        PRE :
            - Le chemin du fichier est une chaîne de caractères non vide.
        POST :
            - Ne retourne rien et ne produit aucun effet de bord si le fichier existe.
            - Lève une exception DatasheetError si le fichier n'existe pas à l'emplacement indiqué.
    
    """

    @staticmethod
    def verify_if_file_exists(destination_file: str) -> None:
        if not os.path.exists(destination_file):
            raise DatasheetError(
                f"Le fichier '{destination_file}' n'existe pas dans ce répertoire."
            )
