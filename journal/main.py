# Pour que l'utilisateur saisissent du texte 
# strip => permet d'enlever les espaces avant et après le texte 
texte = input("Écris quelque chose ").strip();
# si le le etxte est vide alors 
if texte =="":
    # afficher(Erreur il faut que tu saisie du texte)
    print("Erreur il faut que tu saisie du texte ")
# sinon
else:
    with open("journal.txt","a") as  fichier:
        fichier.write(texte+"\n")
    print("Texte ajouter avec succèes")
