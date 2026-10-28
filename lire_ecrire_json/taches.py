import json

try:
    with open("taches.json","r") as file:
        taches = json.load(file)
except:
    taches= []
# L'utilsiateur saisie du texte
nom_tache = input("Veuillez saisir une tâche ? ").strip()

# creation d'une nouvelle taches 
nouvelle_tache = {
    "nom":nom_tache,
    "fait" : False
}

taches.append(nouvelle_tache)

with open("taches.json","w") as file:
    json.dump(taches,file,indent=4)

print("Tâche ajoutée avec succées au fichier")