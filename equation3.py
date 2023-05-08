from utils import PRINTING_TIME, clear_console, get_user_value
from adjustors import adjust_sign, adjust_type, adjust_x
import end_process as ed
import time

def main():
    clear_console()
    print(" Résolvons l'équation du type ax + b = cx + d \n")

    a = get_user_value("a")
    b = get_user_value("b")
    c = get_user_value("c")
    d = get_user_value("d")

    a = adjust_type(a)
    b = adjust_type(b)
    c = adjust_type(c)
    d = adjust_type(d)

    print(f"\n {adjust_x(a)}x {adjust_sign(b)} = {adjust_x(c)}x {adjust_sign(d)}")
    time.sleep(PRINTING_TIME)
    print(f" {adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d)} {adjust_sign(-b)}")
    time.sleep(PRINTING_TIME)
    print(f" {adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d-b)}")
    time.sleep(PRINTING_TIME)
    print(f" {adjust_x(a)}x {adjust_sign(adjust_x(-c))}x = {d-b}")
    time.sleep(PRINTING_TIME)
    print(f" {adjust_x(a-c)}x = {d-b}")
    time.sleep(PRINTING_TIME)

    if(a == c):
        print(" x = Ø car l'equation n'admet aucune solution réelle\n")
    else:
        print(f" x = {d-b}/{a-c}")
        time.sleep(PRINTING_TIME)
        print(f" x = {(d-b)/(a-c)}\n")

    ed.end_process(page = "equation3")

if(__name__ == "__main__"):
    main()