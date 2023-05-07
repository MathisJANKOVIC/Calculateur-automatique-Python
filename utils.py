PRINTING_TIME = 0.25

def is_decimal(value):
    if(value.replace(".","").replace("-","").isdecimal()):
        return True
    else:
        return False

def get_user_value(label, null_ok=True):

    value = input(f"{label} = ")
    if(null_ok):
        while(not is_decimal(value)):
            print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
            value = input(f"{label} = ")
    else:
        while(not is_decimal(value) or value =='0'):
            if(not is_decimal(value)):
                print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
            else:
                print(f"\nERREUR : {label} ne peut être null \nVeuillez réessayer : \n")
            value = input(f"{label} = ")

    return value

def print_choices():
    print("(1) Menu Principal")
    print("(2) Quitter\n")

def get_choice():
    choice = input("Que voulez-vous faire ? ")
    while(choice != '1' and choice != '2'):
        print("\nERREUR : saisie invalide\n")
        print_choices()
        choice = input("Que voulez-vous faire ? ")

    return choice

def handle_choice(choice):
    if(choice == '1'):
            import menu
            menu.main()
    else:
        quit()

def whats_next():
    print_choices()
    choice = get_choice()
    handle_choice(choice)
