from utility import *
from time import sleep
from os import system
from math import sqrt
import tkinter

PRINTING_TIME = 0.4
SCREEN_HEIGHT = 720
SCR
window = tkinter.Tk()

window.title("Solver Master")
window.geometry("720x480")
#window.resizable(width=False, height=False)

lab_title = tkinter.Label(window, text="Quel type d'équation vous-voulez résoudre ?", font=("Arial", 17))
lab_title.pack(pady=30)

equations_frame = tkinter.Frame(window)
equations_frame.pack()
equation1 = tkinter.Button(equations_frame, text="ax + b = 0", font=("Arial", 14), fg="black", width=20)
equation1.pack(pady=10)
equation2 = tkinter.Button(equations_frame, text="ax² + bx + c = 0", font=("Arial", 15), width=20)
equation2.pack(pady=10)
equation3 = tkinter.Button(equations_frame, text="ax + b = cx + d", font=("Arial", 15), width=20)
equation3.pack(pady=10)
window.mainloop()


choice = input("\nVeuillez choisir quel type d'équation vous voulez résoudre parmi les propositions ci-dessus : ")
while (choice != '1' and choice != '2' and choice != '3'):
    print("\nERREUR : saisie invalide")
    choice = input("Veuillez choisir l'une des propositions ci-dessus : ")

system("cls")

if (choice == '1'):

    print("Résolvons l'équation du type ax + b = 0 (a > 0)\n")

    a = b = None
    a = num_validation("a", True)
    b = num_validation("b")

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
    sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {-b}")
    sleep(PRINTING_TIME)
    print(f"x = {-b}/{a}")
    sleep(PRINTING_TIME)
    print(f"x = {-b/a}")
    sleep(PRINTING_TIME)

if (choice == '2'):

    print("Résolvons l'équation du type ax² + bx + c = 0 (a > 0) \n")

    a = b = c = None
    a = num_validation("a", True)
    b = num_validation("b")
    c = num_validation("c")

    if (b == 0 and c == 0):

        print(f"\n{a}x² = 0")
        sleep(PRINTING_TIME)
        print(f"x² = 0/{a}")
        sleep(PRINTING_TIME)
        print(f"x² = 0")
        sleep(PRINTING_TIME)
        print(f"x = 0")

    elif (b != 0 and c == 0):

        print(f"\n{a}x² {adjust_sign(b)}x = 0")
        sleep(PRINTING_TIME)
        print(f"x({a}x {adjust_sign(b)}) = 0")
        sleep(PRINTING_TIME)
        print(f"{a}x {adjust_sign(b)} = 0  ou  x = 0")
        sleep(PRINTING_TIME)
        print(f"{a}x = {-b}")
        sleep(PRINTING_TIME)
        print(f"x = {-b}/{a}")
        sleep(PRINTING_TIME)
        print(f"x = {-b/a}")

    elif (b == 0 and c != 0):

        print(f"\n{a}x² {adjust_sign(c)} = 0")
        sleep(PRINTING_TIME)
        print(f"{a}x² = {-c}")
        sleep(PRINTING_TIME)
        print(f"x² = {-c}/{a}")
        sleep(PRINTING_TIME)
        print(f"x² = {-c/a}")
        sleep(PRINTING_TIME)
        if (-c/a < 0):
            print("x = Ø")
            sleep(PRINTING_TIME)
            print(
                "\nUn carré étant toujours positif, l'équation n'admet donc aucune solution réelle.")
        else:
            print(f"√x² = √({-c/a})")
            sleep(PRINTING_TIME)
            print(f"x = {sqrt(-c/a)}  ou  x = {-sqrt(-c/a)}")

    else:

        print(f"\n{adjust_x(a)}x² {adjust_sign(adjust_x(b))}x {adjust_sign(c)} = 0")
        sleep(PRINTING_TIME)
        print("\ndelta = b² - 4ac")
        sleep(PRINTING_TIME)
        print(f"delta = {b}² - 4*{a}*{c}")
        sleep(PRINTING_TIME)
        print(f"delta = {b*b} - 4*{a*c}")
        sleep(PRINTING_TIME)
        print(f"delta = {b*b} - {4*a*c}")
        sleep(PRINTING_TIME)
        delta = b*b - 4*a*c
        print(f"delta = {delta}\n")
        sleep(PRINTING_TIME)

        if (delta < 0):
            print("delta < 0 donc l'équation n'admet aucune solution réelle et x = Ø")

        if (delta == 0):

            print("delta = 0 donc l'équation admet une unique solution réelle :\n")
            sleep(PRINTING_TIME)
            print("x = -b/2a")
            sleep(PRINTING_TIME)
            print(f"x = {-b}/2{a}")
            sleep(PRINTING_TIME)
            print(f"x = {-b}/{2*a}")
            sleep(PRINTING_TIME)
            print(f"x = {-b/(2*a)}")

        if (delta > 0):

            print("delta > 0 donc l'équation admet 2 solutions réelles x1 et x2\n")
            sleep(PRINTING_TIME)
            print("x1 = (-b - √delta)/(2a)")
            sleep(PRINTING_TIME)
            print(f"x1 = ({-b} - √{delta})/(2*{a})")
            sleep(PRINTING_TIME)
            print(f"x1 = ({-b} - {sqrt(delta)})/{2*a}")
            sleep(PRINTING_TIME)
            print(f"x1 = {-b -sqrt(delta)}/{2*a}")
            sleep(PRINTING_TIME)
            print(f"x1 = {(-b -sqrt(delta))/(2*a)}\n")

            sleep(PRINTING_TIME)
            print("x2 = (-b + √delta)/(2a)")
            sleep(PRINTING_TIME)
            print(f"x2 = ({-b} + √{delta})/2*{a}")
            sleep(PRINTING_TIME)
            print(f"x2 = ({-b} + {sqrt(delta)})/{2*a}")
            sleep(PRINTING_TIME)
            print(f"x2 = {-b + sqrt(delta)}/{2*a}")
            sleep(PRINTING_TIME)
            print(f"x2 = {(-b + sqrt(delta))/(2*a)}\n")

    sleep(PRINTING_TIME)

if (choice == '3'):

    print("Résolvons l'équation du type ax + b = cx + d \n")

    a = b = c = d = None
    a = num_validation("a")
    b = num_validation("b")
    c = num_validation("c")
    d = num_validation("d")

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = {adjust_x(c)}x {adjust_sign(d)}")
    sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d)} {adjust_sign(-b)}")
    sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d-b)}")
    sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x {adjust_sign(adjust_x(-c))}x = {d-b}")
    sleep(PRINTING_TIME)
    print(f"{adjust_x(a-c)}x = {d-b}")
    sleep(PRINTING_TIME)
    if (a == c):
        print("x = Ø car l'equation n'admet aucune solution réelle")
    else:
        print(f"x = {d-b}/{a-c}")
        sleep(PRINTING_TIME)
        print(f"x = {(d-b)/(a-c)}")
    sleep(PRINTING_TIME)
