import platform
import os

PRINTING_TIME = 0.25

def clear_console():
    if(platform.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def is_decimal(value):
    if(value.replace(".","").replace("-","").isdecimal()):
        return True
    else:
        return False

def get_user_value(label, null_ok=True):

    value = input(f" {label} = ")
    if(null_ok):
        while(not is_decimal(value)):
            print("\n ERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
            value = input(f"{label} = ")
    else:
        while(not is_decimal(value) or value =='0'):
            if(not is_decimal(value)):
                print("\n ERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
            else:
                print(f"\n ERREUR : {label} ne peut être null \nVeuillez réessayer : \n")
            value = input(f"{label} = ")

    return value
