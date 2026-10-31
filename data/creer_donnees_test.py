from openpyxl import Workbook


wb = Workbook()
ws = wb.active
ws.title = "Joueurs"
# en tête du tableau
ws.append(["nom", "prenom", "numero_de_licence", "club","classement","date_naissance", "tableau_demande"])


# donnees de test
ws.append(["Dupont", "Jean", "12345", "Wavre TT", "B14", "2015-01-01", "Jeunes"])
ws.append(["Martin", "Sophie", "67890", "Louvain TT", "C6","2016-05-15", "Jeunes"])
ws.append(["Durand", "Pierre", "54321", "Brussell TT", "B2", "2014-08-20", "Jeunes"])
ws.append(["Lefevre", "Marie", "98765", "Namur TT", "D4","2002-03-10", "Debutants"])
ws.append(["Moreau", "Romy", "84329", "Anvers TT", "C2","2003-07-25", "Debutants"])
ws.append(["Thomas", "Leo", "73829", "Manage TT", "D6", "2001-11-05", "Debutants"])
ws.append(["Bernard", "Brandon", "21983", "Wavre TT", "C8","1999-09-12", "Intermediaires"])
ws.append(["Pernelle", "Alice", "39431", "Liege TT", "C3", "2000-12-25", "Intermediaires"])
ws.append(["Savine", "Emma", "29394", "Liege TT", "C3", "2001-06-30", "Intermediaires"])
ws.append(["Sanchez", "Rick", "19204", "C-137 TT", "D17", "2004-02-18", "Confirmes"])
ws.append(["Smith", "Morty", "19384", "C-137 TT", "B3","2005-08-08", "Confirmes"])
ws.append(["Abel", "Carl", "24018", "Namur TT", "A14", "2006-04-20", "Confirmes"])

wb.save("joueurs.xlsx")
print("Fichier Excel cree avec succes")









