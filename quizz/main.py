import random

# Dictionnaire des questions
questions = [
    {
        "question": "Quel mot-clé est utilisé pour définir une fonction ?",
        "choices": ["a) function", "b) func", "c) def"],
        "answer": "c"
    },
    {
        "question": "Quelle fonction est utilisée pour afficher du texte dans la console ?",
        "choices": ["a)  print()", "b) display()", "c) write()"],
        "answer": "a"
    },
    {
        "question": "Comment appelle-t-on une boucle qui se répète un nombre précis de fois ?",
        "choices": ["a) while", "b) for", "c) repeat"],
        "answer": "b"
    }
]
# question data => dictionnaire 
def poser_question(question_data):
    print("\n" + question_data["question"])
    
    for choix in question_data["choices"]:
        print(choix)
    
    while True:
        try:
            reponse = input("Votre réponse (a/b/c) : ").lower()
            
            if reponse not in ["a", "b", "c"]:
                # creer notre propre erreur - controle programme 
                raise ValueError("Réponse invalide")
            
            if reponse == question_data["answer"]:
                print("✅ Bonne réponse !")
                return 1
            else:
                print("❌ Mauvaise réponse !")
                return 0
        #  Si on a value erreur c'est grace a raise ValueError(...)
        except ValueError:
            # si la reponse n'est pas  a b c 
            print(" Veuillez entrer a, b ou c.")
        # CTRL + C
        # except KeyboardInterrupt:
            # affiche interruption du programme 
            # print("\n Interruption du programme.")
            # return 0
        # erreur hors de l'affichage 
        except Exception as e:
            print("Erreur inattendue :", e)
            return 0


def lancer_quiz():
    score = 0
    
    try:
        random.shuffle(questions)

        for question in questions:
            score += poser_question(question)

        print("\n🎯 Quiz terminé !")
        print(f"Votre score : {score} / {len(questions)}")

    except Exception as e:
        print("Erreur pendant le quiz :", e)

def main():
    print("Bienvenue dans le Quiz !")
    
    while True:
        try:
            lancer_quiz()
            
            rejouer = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
            
            if rejouer not in ["o", "n"]:
                raise ValueError
            
            if rejouer != "o":
                print(" Au revoir !")
                break

        except ValueError:
            print(" Entrez 'o' pour oui ou 'n' pour non.")

        except KeyboardInterrupt:
            print("\n Programme interrompu.")
            break


# Lancer le programme
if __name__ == "__main__":
    main()