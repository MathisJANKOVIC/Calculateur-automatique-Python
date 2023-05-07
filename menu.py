import equation1
import equation2
import equation3
import platform
import time
import os

def clear_console():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def main():
    clear_console()
    time.sleep(0.3)

    print("Bienvenue dans le solveur d'équations\n")
    print("(1) ax + b = 0")
    print("(2) ax² + bx + c = 0")
    print("(3) ax + b = cx + d")

    equation = input("\nQuel type d'équation vous voulez résoudre parmi les propositions ci-dessus : ")
    while(equation != '1' and equation != '2' and equation != '3'):

        print("\nERREUR : saisie invalide\n")
        time.sleep(1)

        print("(1) ax + b = 0")
        print("(2) ax² + bx + c = 0")
        print("(3) ax + b = cx + d")

        equation = input("\nVeuillez choisir l'une des propositions ci-dessus : ")

    clear_console()
    if(equation == '1'):
        equation1.main()
    elif(equation == '2'):
        equation2.main()
    elif(equation == '3'):
        equation3.main()

if(__name__ == "__main__"):
    main()
