from pythonclimenu import menu
import equation1
import equation2
import equation3

CHOICES = ("ax + b = 0", "ax² + bx + c = 0", "ax + b = cx + d", "Quitter")

def main():
    choice_equation = menu("Quelle équation voulez-vous résoudre ?", CHOICES, (0, 95, 0))

    if(choice_equation == CHOICES[0]):
        equation1.run()
    elif(choice_equation == CHOICES[1]):
        equation2.run()
    elif(choice_equation == CHOICES[2]):
        equation3.run()
    else:
        exit()

if(__name__ == "__main__"):
    main()
