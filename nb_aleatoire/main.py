import random

nb_vie=5
#randint est utiliser pour generer un nombre aleatoire qui est un entier . randint vient de random
nb_aleatoire = random.randint(1,10)

nb_utilisateur = int(input("Entrer un nombre entre 1 et 10 "))
# type => connaître le type de la variable 
# print(type(nb_utilisateur))

while nb_aleatoire != nb_utilisateur:
    nb_vie = nb_vie -1

    print("ton nombre de vie est de ",nb_vie)

    if nb_vie == 0:
        print(f"Tu as perdus,Le nombre aleatoire est de {nb_aleatoire}")
        break

    if nb_utilisateur > nb_aleatoire:
        print("Ton nombre est trop grand")
    else:
        print("Ton nombre est trop petit ")
    
    nb_utilisateur = int(input("Entrer un nombre entre 1 et 10 "))

if nb_vie !=0:
    print(f"Felicitations tu as trouvé le nombre {nb_aleatoire} et il te reste {nb_vie} vie")

