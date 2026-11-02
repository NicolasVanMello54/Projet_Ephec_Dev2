import os


class DatasheetError(Exception):
    pass

class InputTypeError(DatasheetError):
    pass

class JoueurIntrouvable(Exception):
    pass

class AllErrors:
    # eviter l'instanciation de la classe AllErrors
    
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

    @staticmethod
    def verify_if_file_exists(destination_file: str) -> None:
        if not os.path.exists(destination_file):
            raise DatasheetError(
                f"Le fichier '{destination_file}' n'existe pas dans ce répertoire."
            )
