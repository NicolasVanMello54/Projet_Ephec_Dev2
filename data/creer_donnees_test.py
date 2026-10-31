from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Joueurs"
# en tête du tableau
ws.append(["nom", "prenom", "numero_de_licence", "club","classement", "tableau_demande"])


# donnees de test
ws.append(["Dupont", "Jean", "12345", "Wavre TT", "B14", "Jeunes"])
ws.append(["Martin", "Sophie", "67890", "Louvain TT", "C6", "Jeunes"])
ws.append(["Durand", "Pierre", "54321", "Brussell TT", "B2", "Jeunes"])
ws.append(["Lefevre", "Marie", "98765", "Namur TT", "D4", "Debutants"])
ws.append(["Moreau", "Romy", "84329", "Anvers TT", "C2", "Debutants"])
ws.append(["Thomas", "Leo", "73829", "Manage TT", "D6", "Debutants"])
ws.append(["Bernard", "Brandon", "21983", "Wavre TT", "C8", "Intermediaires"])
ws.append(["Pernelle", "Alice", "39431", "Liege TT", "C3", "Intermediaires"])
ws.append(["Savine", "Emma", "29394", "Liege TT", "C3", "Intermediaires"])
ws.append(["Sanchez", "Rick", "19204", "C-137 TT", "D17", "Confirmes"])
ws.append(["Smith", "Morty", "19384", "C-137 TT", "B3", "Confirmes"])
ws.append(["Abel", "Carl", "24018", "Namur TT", "A14", "Confirmes"])

wb.save("joueurs.xlsx")
print("Fichier Excel cree avec succes")









