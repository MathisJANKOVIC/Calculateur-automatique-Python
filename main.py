import console_menu
import equation1
import equation2
import equation3

EQUATIONS = ("ax + b = 0", "ax² + bx + c = 0", "ax + b = cx + d")

def main():
    choice_equation = console_menu.menu("Quelle équation voulez-vous résoudre ?", EQUATIONS, "\033[48;5;22m")

    if(choice_equation == EQUATIONS[0]):
        equation1.run()
    elif(choice_equation == EQUATIONS[1]):
        equation2.run()
    elif(choice_equation == EQUATIONS[2]):
        equation3.run()

if(__name__ == "__main__"):
    main()
