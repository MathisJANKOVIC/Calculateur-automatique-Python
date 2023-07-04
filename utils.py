PRINTING_TIMELAPS = 0.25
CONTINUE_MESSAGE = " Appuyez sur 'Entrer' pour continuer..."

def is_decimal(value: str) -> bool :
    """Returns True if the specified string is a valid decimal expression convertible into float else returns False."""
    if(value.replace(".","").replace("-","").isdecimal()):
        return True
    else:
        return False

def get_user_value(label: str, null_ok = True) -> str :
    """Prompts the user to enter a number and retries while the user gives an invalid decimal expression.

    Args:
        label (str): label of the variable to print to the user
        null_ok (bool, optional): whether the value can be null (default to true)
    Returns:
        str: user input value
    """
    value = input(f" {label} = ")
    if(null_ok):
        while(not is_decimal(value)):
            print("\n ERREUR : la saisie doit être un nombre en écriture décimale \n Veuillez réessayer : \n")
            value = input(f" {label} = ")
    else:
        while(not is_decimal(value) or value == '0'):
            if(not is_decimal(value)):
                print("\n ERREUR : la saisie doit être un nombre en écriture décimale \n Veuillez réessayer : \n")
            else:
                print(f"\n ERREUR : {label} ne peut être null \nVeuillez réessayer : \n")
            value = input(f" {label} = ")

    return value
