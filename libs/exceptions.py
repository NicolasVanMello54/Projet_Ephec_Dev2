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
                f"Error : The field '{field_name}' contains a null value."
            )
            
        # Connversion en chaine et supression des espaces
        clean_value = str(value).strip()
        
        if not clean_value:
            raise InputTypeError(
                f"Error : The field '{field_name}' is empty after cleaning."
            )
            
        return clean_value

    @staticmethod
    def verify_if_file_exists(destination_file: str) -> None:
        if not os.path.exists(destination_file):
            raise FileNotFoundError(
                f"File Not Found : The file '{destination_file}' does not exist in this directory."
            )
