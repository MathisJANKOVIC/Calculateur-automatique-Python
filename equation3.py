from utils import PRINTING_TIMELAPS, CONTINUE_MESSAGE, get_user_value
from adjustors import adjust_sign, adjust_type, adjust_x
import main
import time
import os

def run():
    os.system("cls" if(os.name == "nt") else "clear")
    print("\n Résolvons l'équation du type ax + b = cx + d \n")

    a = get_user_value("a")
    b = get_user_value("b")
    c = get_user_value("c")
    d = get_user_value("d")

    a = adjust_type(a)
    b = adjust_type(b)
    c = adjust_type(c)
    d = adjust_type(d)

    print(f"\n {adjust_x(a)}x {adjust_sign(b)} = {adjust_x(c)}x {adjust_sign(d)}")
    time.sleep(PRINTING_TIMELAPS)
    print(f" {adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d)} {adjust_sign(-b)}")
    time.sleep(PRINTING_TIMELAPS)
    print(f" {adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d-b)}")
    time.sleep(PRINTING_TIMELAPS)
    print(f" {adjust_x(a)}x {adjust_sign(adjust_x(-c))}x = {d-b}")
    time.sleep(PRINTING_TIMELAPS)
    print(f" {adjust_x(a-c)}x = {d-b}")
    time.sleep(PRINTING_TIMELAPS)

    if(a == c):
        print(" x = Ø car l'equation n'admet aucune solution réelle\n")
    else:
        print(f" x = {d-b}/{a-c}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x = {(d-b)/(a-c)}\n")

    input(CONTINUE_MESSAGE + " ")
    main.main()

if(__name__ == "__main__"):
    run()