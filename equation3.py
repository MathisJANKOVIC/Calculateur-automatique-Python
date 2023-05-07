from utility import *
import time

def main():
    print("Résolvons l'équation du type ax + b = cx + d \n")

    a = input("a = ")
    while(not is_decimal(a)):
        print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        a = input("a = ")

    b = input("b = ")
    while(not is_decimal(b)):
        print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        b = input("b = ")

    c = input("c = ")
    while(not is_decimal(c)):
        print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        c = input("c = ")

    d = input("d = ")
    while(not is_decimal(d)):
        print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        d = input("d = ")

    a = adjust_type(a)
    b = adjust_type(b)
    c = adjust_type(c)
    d = adjust_type(d)

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = {adjust_x(c)}x {adjust_sign(d)}")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d)} {adjust_sign(-b)}")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d-b)}")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x {adjust_sign(adjust_x(-c))}x = {d-b}")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a-c)}x = {d-b}")
    time.sleep(PRINTING_TIME)

    if(a == c):
        print("x = Ø car l'equation n'admet aucune solution réelle\n")
    else:
        print(f"x = {d-b}/{a-c}")
        time.sleep(PRINTING_TIME)
        print(f"x = {(d-b)/(a-c)}\n")

    time.sleep(PRINTING_TIME)

if(__name__ == "__main__"):
    main()