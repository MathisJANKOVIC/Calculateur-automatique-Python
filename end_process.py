import menu

def print_choices():
    print(" (1) Recommencer")
    print(" (2) Menu Principal")
    print(" (3) Quitter\n")

def get_user_choice():
    choice = input(" Que voulez-vous faire ? ")
    while(choice != '1' and choice != '2' and choice != '3'):
        print("\n ERREUR : saisie invalide\n")
        print_choices()
        choice = input(" Que voulez-vous faire ? ")

    return int(choice)

def redirect(choice, page):
    if(choice == 1):
        if(page == "equation1"):
            import equation1
            equation1.main()
        elif(page == "equation2"):
            import equation2
            equation2.main()
        elif(page == "equation3"):
            import equation3
            equation3.main()
    elif(choice == 2):
        menu.main()
    elif(choice == 3):
        quit()

def end_process(page):
    input(" Appuyez sur 'Entrer' pour continuer... \n ")
    print_choices()
    choice = get_user_choice()
    redirect(choice, page)
