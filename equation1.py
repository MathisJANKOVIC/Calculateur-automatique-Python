from utility import *
import time
import os

def main():
    os.system("cls")
    time.sleep(0.3)
    print("Résolvons l'équation du type ax + b = 0 (a != 0)\n")

    a = input("a = ")
    while(not is_decimal(a) or a == "0"):
        if(not is_decimal(a)):
            print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        else:
            print("\nERREUR : a ne peut être null \nVeuillez réessayer : \n")
        a = input("a = ")

    b = input("b = ")
    while(not is_decimal(b)):
        print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        b = input("b = ")

    a = adjust_type(a)
    b = adjust_type(b)

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {-b}")
    time.sleep(PRINTING_TIME)
    print(f"x = {-b}/{a}")
    time.sleep(PRINTING_TIME)
    print(f"x = {-b/a}\n")
    time.sleep(PRINTING_TIME)

if(__name__ == "__main__"):
    main()