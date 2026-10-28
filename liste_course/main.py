tab_ingredient=[]
programme_actif = True
nb_ingredient = 0

print("Bienvenue sur ma liste de course")

while programme_actif:
    print("veuillez faire un choix en entrant un nombre")
    print("1 - Ajouter un ingredient ")
    print("2 - Supprimer un ingredient ")
    print("3 - Quitter et voir la liste des courses")

    nb_saisie = int(input("quel est ton nombre ? "))

    match nb_saisie:
        case 1:
            ingredient = input("Quel est ton ingredient ? ").lower().strip();

            if ingredient in tab_ingredient:
                print(f"Cette ingredient {ingredient} existe deja dans le tableau")
            else:
                tab_ingredient.append(ingredient)
                nb_ingredient+=1
                print(f"L'ingredient {ingredient} à était ajouter avec succès")
        case 2:
            if nb_ingredient ==0:
                print("Il n'y a pas d'ingredient dans la liste de course ")
            else:
                ingredient_supprimer = input("Ingredient a supprimer").lower().strip()

                if ingredient_supprimer in tab_ingredient:
                    tab_ingredient.remove(ingredient_supprimer)
                    nb_ingredient -=1
                    print(f"L'ingredient à etait supprimer")
                else:
                    print("L'ingredient saisie n'ai pas dans la liste de course" )
        case 3:
            print("Arret du programme")
            programme_actif = False
            print(tab_ingredient)
        case _:
            print("Tu dois taper 1 pour ajouter un ingredient, 2 pour en supprimer ou 3 pour quitter l'application")



