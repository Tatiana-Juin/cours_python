# with open("taches.txt","w") as file:
#     file.write("creer du contenu")
import json
taches = [

    {
        "nom" : "coder",
        "fait" : False
    },
    {
        "nom" : "manger",
        "fait" : True
    },
]
# Cette ligne permet de créer un fichier (taches.json) ou on va ecrire (w) dedans 
#          nomFichier,  ecrire 
# with open("taches.json","w") as file:
    # envoyer dans mon fichier les informations du tableau qui contient un dictionaire tache
    # json.dump(taches,file,indent=4)

# Lire un fichier json r => read = lire
with open("taches.json","r") as file:
    taches = json.load(file)

# Afficher les taches dans le terminale 
for tache in taches:
    print(tache["nom"],"-",tache["fait"])

