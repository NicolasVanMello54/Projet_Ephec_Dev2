def determiner_vainqueurs_poules(liste_matchs):
    brouillon_scores = {} #on utilise ce dictionnaire comme brouillon dans lequel on met les infos le la liste des matchs

    #parcourir les matchs (dictionnaires) dans la liste
    for match in liste_matchs:
        nom_poule = match.poule
        j1 = match.joueur1
        j2 = match.joueur2
        #on met ça dans des variables pour raccourcir l'écriture pour la suite

        if nom_poule not in brouillon_scores:
            brouillon_scores[nom_poule] = {}
            #si la poule examinée n'est pas dans notre brouillon, on l'ajoute

        if j1 not in brouillon_scores[nom_poule]:
            brouillon_scores[nom_poule][j1] = 0
        if j2 not in brouillon_scores[nom_poule]:
            brouillon_scores[nom_poule][j2] = 0
        #nombre de victoires par défaut dans notre brouillon avant de compter les victoires

        if match.score1 > match.score2:
            brouillon_scores[nom_poule][j1] += 1
        elif match.score2 > match.score1:
            brouillon_scores[nom_poule][j2] += 1


    # Trouver le premier du groupe, parcourir les sous dictionnaires dans notre dictionnaire brouillon
    for nom_poule in brouillon_scores:
        print("")  # saut de ligne
        print(str(nom_poule) + " :")

        #variable pour raccourcir l'écriture pour la suite
        scores_joueurs = brouillon_scores[nom_poule]

        for joueur in scores_joueurs:
            victoires = scores_joueurs[joueur]
            print(str(joueur) + " a " + str(victoires) + " victoire(s)")

        #algorythme étape par étape pour trouver le maximum
        vainqueur = ""
        max_victoires = -1

        for joueur in scores_joueurs:
            victoires_actuelles = scores_joueurs[joueur]

            if victoires_actuelles > max_victoires:
                max_victoires = victoires_actuelles
                vainqueur = joueur

        if vainqueur != "":
            print("Le premier est : " + str(vainqueur))
