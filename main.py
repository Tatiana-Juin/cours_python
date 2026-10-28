# 1. Variable → permet de stocker des informations que l'on peut modifier.
nom = "Tatiana" # chaine de caratere => str
print(nom)
nom = "Julien"
# integer => nombre entier 
age : int = 29 
# print → permet d'afficher des informations dans la console.
print(nom)
# Pour concaténer du texte, comme ici « Je m'appelle », et afficher la valeur d'une variable, on utilise la virgule (,).
print("Je m'appelle", nom)
# On peut également utiliser les f-strings pour afficher du texte et la valeur des variables.
print(f"J'ai {age} ans")
# Pour nommer une variable ou une liste, on utilise le snake_case. On met un _ entre chaque mot.
# La variable est_trouver est de type booléen, c'est-à-dire que sa valeur ne peut être que True ou False.
est_trouver = False
print(est_trouver)

# Pour faire saisir une valeur à l'utilisateur, on utilise input(). Par défaut, le texte saisi et retourné est de type str (chaîne de caractères).
mdp = input("Saisir un mot de passe de 8 caractère minimum ")
print(mdp)
# Pour que la valeur saisie et retournée soit autre chose qu'une chaîne de caractères, on place le type souhaité avant input(). Cela permet de convertir une valeur de type str vers le type voulu, comme dans l'exemple.
nombre_saisie = int(input("Saisie un nombre "))
print(nombre_saisie)
# CONDITION 
# La condition if / else permet d'exécuter du code selon une condition donnée. 
# Dans cet exemple, on veut afficher un message d'erreur si le mot de passe est inférieur à 8 caractères (len() compte le nombre de caractères). 
# Sinon, il affichera que le mot de passe est valide.
# si la longueur du mdp est strictement inférieur a 8 caractere alors 
if (len(mdp) < 8):
#    affiche dans la console le message (""erreur ton mot de passe doit contenir 8 caractères au minimum"")
   print("erreur ton mot de passe doit contenir 8 caractères au minimum")
#    sinon 
else:
#  affiche dans la console ("le mdp est bon") 
   print("le mdp est bon ")


compteur = 1
# La boucle while s'exécute tant que la condition est vraie . Il faut donc faire attention est prévoir un moyen pour que cette condition devienne fausse, afin d'arrêter la boucle . Sinon tu vas créer une boucle infinie et ta boucle ne va jamais s'arreter et faire buger ton ordianteur . 
# TANT QUE compteur est inferieur ou égale à 3 alors 
while compteur <= 3:
   # affiche  le nombre est 
   print(f"Le nombre est {compteur}")
   # Ajoute 1 à ton compteur. C’est grâce à cela qu’à un moment tu auras 4 et que tu ne rentreras plus dans la condition, ce qui évite la boucle infinie.
   compteur = compteur + 1

age_personne =  20
# Dans cette exemple, je te montre comment convertir le type d'une variable 
convertir_age_person = str(age_personne)
# type eprmet de connaître le type d'une variable. 
print(type(convertir_age_person))
print(convertir_age_person)

# for → on l’utilise quand on connaît le nombre d’itérations (c’est-à-dire le nombre de fois que l’on va boucler). Attention, la boucle commence à 0.
for i in range(5):
    print(f"tour numero {i}")
  
# FONCTION
#  Une fonction regroupe du code que l'on peut réutiliser. Il suffit d’appeler la fonction.  . 
#  X est le paramètre de la fonction 
def carre(x):
   return x * x
# Ici on appelle la fonction et 5 est l'ARGUMENT 
print(carre(5))

#Tableau - liste 
# Liste  d’éléments que tu vas pouvoir modifier. Au début, tu vas déclarer ta liste et ses différentes valeurs. Tu vas pouvoir en ajouter et en supprimer. Le tableau commence par l’index 0.
fruits = ['pomme','banane','orange']
# affiche le premier élément de la liste 
print(fruits[0])
# Affiche le deuxième élément 
print(fruits[1])

#Ajoute un élément dans la liste à la fin 
fruits.append("Kiwi")
#Modifie la valeur du deuxième élément de la liste
fruits[1]="mangue"
print(fruits)
# supprime un élément de la liste 
fruits.remove("pomme")
# print(fruits)
# for in → permet d’afficher les éléments d’une liste.
# pour f de fruits(liste) alors
for f in fruits:
   print(f"J'aime {f}")

# DICTIONNAIRE
#Permet de stocker des données avec des clés 
# nom => est la clé
# Tania est la valeur du nom 
personne = {
   "nom" : "Tania",
   "age" : 29
}
# Pour afficher la valeur d’un nom, on fait nom_dictionnaire[nom_cle]
print(personne["nom"])

