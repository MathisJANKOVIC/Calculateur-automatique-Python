import console_menu
import equation1
import equation2
import equation3

EQUATIONS_OPTIONS = ("ax + b = 0", "ax² + bx + c = 0", "ax + b = cx + d")

def main():
    choice_equation = console_menu.console_menu("Quelle équation voulez-vous résoudre ?", EQUATIONS_OPTIONS, "\033[48;5;22m")

    if(choice_equation == EQUATIONS_OPTIONS[0]):
        equation1.run()
    elif(choice_equation == EQUATIONS_OPTIONS[1]):
        equation2.run()
    elif(choice_equation == EQUATIONS_OPTIONS[2]):
        equation3.run()

if(__name__ == "__main__"):
    main()
