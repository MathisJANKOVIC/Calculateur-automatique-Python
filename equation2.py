from utils import PRINTING_TIMELAPS, CONTINUE_MESSAGE, get_user_value
from adjustors import adjust_sign, adjust_type, adjust_x
import main

import math
import time
import os

def run():
    os.system('cls' if(os.name == 'nt') else 'clear')
    print("\n Résolvons l'équation du type ax² + bx + c = 0 (a ≠ 0)\n")

    a = get_user_value('a', null_ok=False)
    b = get_user_value('b')
    c = get_user_value('c')

    a = adjust_type(a)
    b = adjust_type(b)
    c = adjust_type(c)

    if(b == 0 and c == 0):
        print(f"\n {a}x² = 0")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x² = 0/{a}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x² = 0")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x = 0\n")

    elif(b != 0 and c == 0):
        print(f"\n {a}x² {adjust_sign(b)}x = 0")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x({a}x {adjust_sign(b)}) = 0")
        time.sleep(PRINTING_TIMELAPS)
        print(f" {a}x {adjust_sign(b)} = 0  ou  x = 0")
        time.sleep(PRINTING_TIMELAPS)
        print(f" {a}x = {-b}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x = {-b}/{a}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x = {-b/a}\n")

    elif(b == 0 and c != 0):
        print(f"\n {a}x² {adjust_sign(c)} = 0")
        time.sleep(PRINTING_TIMELAPS)
        print(f" {a}x² = {-c}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x² = {-c}/{a}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" x² = {-c/a}")
        time.sleep(PRINTING_TIMELAPS)

        if(-c/a < 0):
            print(" x = Ø")
            time.sleep(PRINTING_TIMELAPS)
            print("\n Un carré étant toujours positif, l'équation n'admet donc aucune solution réelle.\n")
        else:
            print(f" √x² = √({-c/a})")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x = {math.sqrt(-c/a)}  ou  x = {-math.sqrt(-c/a)}\n")

    else:
        print(f"\n {adjust_x(a)}x² {adjust_sign(adjust_x(b))}x {adjust_sign(c)} = 0")
        time.sleep(PRINTING_TIMELAPS)
        print("\n delta = b² - 4ac")
        time.sleep(PRINTING_TIMELAPS)
        print(f" delta = {b}² - 4*{a}*{c}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" delta = {b*b} - 4*{a*c}")
        time.sleep(PRINTING_TIMELAPS)
        print(f" delta = {b*b} - {4*a*c}")
        time.sleep(PRINTING_TIMELAPS)
        dd = b*b - 4*a*c
        print(f" delta = {dd}\n")
        time.sleep(PRINTING_TIMELAPS)

        if(dd < 0):
            print(" delta < 0 donc l'équation n'admet aucune solution réelle et x = Ø \n")

        elif(dd == 0):
            print(" delta = 0 donc l'équation admet une unique solution réelle :\n")
            time.sleep(PRINTING_TIMELAPS)
            print(" x = -b/2a")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x = {-b}/2{a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x = {-b}/{2*a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x = {-b/(2*a)}\n")

        elif(dd > 0):
            print(" delta > 0 donc l'équation admet 2 solutions réelles x₁ et x₂\n")
            time.sleep(PRINTING_TIMELAPS)
            print(" x₁ = (-b - √delta)/(2a)")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₁ = ({-b} - √{dd})/(2*{a})")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₁ = ({-b} - {math.sqrt(dd)})/{2*a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₁ = {-b -math.sqrt(dd)}/{2*a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₁ = {(-b -math.sqrt(dd))/(2*a)}\n")

            time.sleep(PRINTING_TIMELAPS)
            print(" x₂ = (-b + √delta)/(2a)")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₂ = ({-b} + √{dd})/2*{a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₂ = ({-b} + {math.sqrt(dd)})/{2*a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₂ = {-b + math.sqrt(dd)}/{2*a}")
            time.sleep(PRINTING_TIMELAPS)
            print(f" x₂ = {(-b + math.sqrt(dd))/(2*a)}\n")

    input(CONTINUE_MESSAGE + " ")
    main.main()

if(__name__ == "__main__"):
    run()