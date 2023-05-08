import equation1
import equation2
import equation3
import utils

def main():
    utils.clear_console()
    print(" Bienvenue dans le solveur d'équations\n")

    print(" (1) ax + b = 0")
    print(" (2) ax² + bx + c = 0")
    print(" (3) ax + b = cx + d")

    equation = input("\n Quel type d'équation vous voulez résoudre parmi les propositions ci-dessus : ")
    while(equation != '1' and equation != '2' and equation != '3'):

        print("\n ERREUR : saisie invalide\n")

        print(" (1) ax + b = 0")
        print(" (2) ax² + bx + c = 0")
        print(" (3) ax + b = cx + d")

        equation = input("\n Veuillez choisir l'une des propositions ci-dessus : ")

    if(equation == '1'):
        equation1.main()
    elif(equation == '2'):
        equation2.main()
    elif(equation == '3'):
        equation3.main()

if(__name__ == "__main__"):
    main()
