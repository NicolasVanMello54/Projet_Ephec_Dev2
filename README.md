#Projet Dev II : Tournoi tennis de table

Gestion de tournoi pour le club TTC Les raquettes du Bois

## Groupe 2TL2-7
-Ange
-Sophie
-Mateo
-Nicolas

## Installation
python -m venv .venv
pip install -r requirements.txt


## Données de test  
le fichier 'data/joueurs.xlsx' contient les données pour tester le programme.
Pour le generer :

'''bash
    cd data
    python creer_donnees_test.py
 '''


 ## Utilisation 

 ### lister tous les joueurs 
 python main.py -a

 ### Rechercher un joueur par nom
 python main.py -n nom
 ex : python main.py -n smith

 ### Rechercher un joueur par licence
 python main.py -l numero
 ex: python main.py -l 19384




### Generer les poules

aller dans le dossier libs puis taper
python3 gestion_groupes.py ../data/joueurs.xlsx
le fichier de generation devrait se creer dans le dossier libs "generated_groups.py"


### Saisie des matchs et calcul du classement des poules
Lancer la saisie des scores et afficher automatiquement le premier de chaque poule :

python main.py -m