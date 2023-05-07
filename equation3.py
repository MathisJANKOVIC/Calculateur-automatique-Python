from adjustors import *
from utils import *
import time

def main():
    print("Résolvons l'équation du type ax + b = cx + d \n")

    a = get_user_value("a")
    b = get_user_value("b")
    c = get_user_value("c")
    d = get_user_value("d")

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

    input("Pressez 'Entrer' pour continuer... \n")
    whats_next()

if(__name__ == "__main__"):
    main()