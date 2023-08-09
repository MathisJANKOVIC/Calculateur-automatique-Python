import sys

PRINTING_TIMELAPS = 0.25
CONTINUE_MESSAGE = " Pressez la touche 'entrée' pour continuer..."

def is_decimal(value: str) -> bool:
    """Returns True if the specified string is a valid decimal expression convertible into float else returns False."""
    if(value.replace(".","").replace("-","").isdecimal()):
        return True
    else:
        return False

def get_user_value(label: str, null_ok = True) -> str:
    """Prompts the user to enter a number and retries while the user gives an invalid decimal expression.

    Args:
        label: label of the variable to print to the user
        null_ok (optional): whether the value can be null (default to True)
    Returns:
        value: user input value
    """
    value = input(f" {label} = ")
    if(null_ok):
        while(not is_decimal(value)):
            sys.stdout.write("\n\033[31m La saisie doit être un nombre en écriture décimale \033[0m")
            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")

            value = input(f" {label} = ")

        sys.stdout.write("\n")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")
    else:
        while(not is_decimal(value) or value == '0'):
            if(not is_decimal(value)):
                sys.stdout.write("\n\033[31m La saisie doit être un nombre en écriture décimale \033[0m")
            else:
                sys.stdout.write(f"\n\033[31m {label} ne peut être nul \033[0m")

            sys.stdout.write("\033[K")
            sys.stdout.write("\033[F" * 2)
            sys.stdout.write("\033[K")

            value = input(f" {label} = ")

        sys.stdout.write("\n")
        sys.stdout.write("\033[K")
        sys.stdout.write("\033[F")

    return value
