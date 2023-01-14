from time import sleep
from os import system
from math import sqrt
printing_time = 0.4

def shielding_num(name,cant_be_0 = False): 
        
    while True:
        cst = input(f"{name} = ")
        if(((cst.replace(".","")).replace("-","")).isdecimal()):
            if(cant_be_0 == True):
                if(int(cst) != 0):
                    break
                else:
                    print(f"\nERREUR : {name} ne peux être nul \nVeuillez réessayer : \n")
            else:
                break
        else:
            print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")

    if("." in cst):
        return float(cst)
    else:
        return int(cst)

def adjust_sign(coef):
         
    if(type(coef) == int or type(coef) == float):
        if(coef > 0):
            return(f"+ {coef}")
        if(coef == 0):
            return("")
        if(coef < 0):
            return(f"- {-coef}")   
    else:
        if(coef == ""):
            return("+ ")
        if(coef == "-"):
            return("- ") 

def adjust_x(coef):
    
    if(coef == 1):
        return("")
    elif(coef == -1):
        return("-")
    else:
        return(coef)

system("cls")
sleep(0.9)
print("Bienvenue dans le solveur d'équations\n")

print("(1) ax + b = 0")
print("(2) ax² + bx + c = 0")
print("(3) ax + b = cx + d")

choice = input("\nVeuillez choisir quel type d'équation vous voulez résoudre parmi les propositions ci-dessus : ")
while (choice != '1' and choice != '2' and choice != '3'):
    print("\nERREUR : saisie invalide")
    choice = input("Veuillez choisir l'une des propositions ci-dessus : ")

system("cls")

if(choice == '1'):
    
    print("Résolvons l'équation du type ax + b = 0 (a > 0)\n")
    
    a = b = None
    a = shielding_num("a",True)
    b = shielding_num("b")

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
    sleep(printing_time)
    print(f"{adjust_x(a)}x = {-b}")
    sleep(printing_time)
    print(f"x = {-b}/{a}")
    sleep(printing_time)
    print(f"x = {-b/a}")
    sleep(printing_time)

if(choice == '2'):
    
    print("Résolvons l'équation du type ax² + bx + c = 0 (a > 0) \n")

    a = b = c = None
    a = shielding_num("a",True)
    b = shielding_num("b")
    c = shielding_num("c")

    if(b == 0 and c == 0):

        print(f"\n{a}x² = 0")
        sleep(printing_time)
        print(f"x² = 0/{a}")
        sleep(printing_time)
        print(f"x² = 0")
        sleep(printing_time)
        print(f"x = 0")

    elif(b != 0 and c == 0):

        print(f"\n{a}x² {adjust_sign(b)}x = 0")
        sleep(printing_time)
        print(f"x({a}x {adjust_sign(b)}) = 0")
        sleep(printing_time)
        print(f"{a}x {adjust_sign(b)} = 0  ou  x = 0")
        sleep(printing_time)
        print(f"{a}x = {-b}")
        sleep(printing_time)
        print(f"x = {-b}/{a}")
        sleep(printing_time)
        print(f"x = {-b/a}")
    
    elif(b == 0 and c != 0):

        print(f"\n{a}x² {adjust_sign(c)} = 0")
        sleep(printing_time)
        print(f"{a}x² = {-c}")
        sleep(printing_time)
        print(f"x² = {-c}/{a}")
        sleep(printing_time)
        print(f"x² = {-c/a}")
        sleep(printing_time)       
        if(-c/a < 0):
            print("x = Ø")
            sleep(printing_time)
            print("\nUn carré étant toujours positif, l'équation n'admet donc aucune solution réelle.")
        else:
            print(f"√x² = √({-c/a})")
            sleep(printing_time)
            print(f"x = {sqrt(-c/a)}  ou  x = {-sqrt(-c/a)}")
    
    else:

        print(f"\n{adjust_x(a)}x² {adjust_sign(adjust_x(b))}x {adjust_sign(c)} = 0")
        sleep(printing_time)
        print("\ndelta = b² - 4ac")
        sleep(printing_time)
        print(f"delta = {b}² - 4*{a}*{c}")
        sleep(printing_time)
        print(f"delta = {b*b} - 4*{a*c}")
        sleep(printing_time)
        print(f"delta = {b*b} - {4*a*c}")
        sleep(printing_time)
        delta = b*b - 4*a*c
        print(f"delta = {delta}\n")
        sleep(printing_time)

        if(delta < 0):
            print("delta < 0 donc l'équation n'admet aucune solution réelle et x = Ø")
        
        if(delta == 0):
            
            print("delta = 0 donc l'équation admet une unique solution réelle :\n")
            sleep(printing_time)
            print("x = -b/2a")
            sleep(printing_time)
            print(f"x = {-b}/2{a}")
            sleep(printing_time)
            print(f"x = {-b}/{2*a}")
            sleep(printing_time)
            print(f"x = {-b/(2*a)}")

        if(delta > 0):            
            
            print("delta > 0 donc l'équation admet 2 solutions réelles x1 et x2\n")
            sleep(printing_time)
            print("x1 = (-b - √delta)/(2a)")
            sleep(printing_time)
            print(f"x1 = ({-b} - √{delta})/(2*{a})")
            sleep(printing_time)
            print(f"x1 = ({-b} - {sqrt(delta)})/{2*a}")
            sleep(printing_time)
            print(f"x1 = {-b -sqrt(delta)}/{2*a}")
            sleep(printing_time)
            print(f"x1 = {(-b -sqrt(delta))/(2*a)}\n")

            sleep(printing_time)
            print("x2 = (-b + √delta)/(2a)")
            sleep(printing_time)
            print(f"x2 = ({-b} + √{delta})/2*{a}")
            sleep(printing_time)
            print(f"x2 = ({-b} + {sqrt(delta)})/{2*a}")
            sleep(printing_time)
            print(f"x2 = {-b + sqrt(delta)}/{2*a}")
            sleep(printing_time)
            print(f"x2 = {(-b + sqrt(delta))/(2*a)}\n")
    
    sleep(printing_time)

if(choice == '3'):
    
    print("Résolvons l'équation du type ax + b = cx + d \n")

    a = b = c = d = None
    a = shielding_num("a")
    b = shielding_num("b")
    c = shielding_num("c") 
    d = shielding_num("d") 

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = {adjust_x(c)}x {adjust_sign(d)}")
    sleep(printing_time)
    print(f"{adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d)} {adjust_sign(-b)}")
    sleep(printing_time)
    print(f"{adjust_x(a)}x = {adjust_x(c)}x {adjust_sign(d-b)}")
    sleep(printing_time)
    print(f"{adjust_x(a)}x {adjust_sign(adjust_x(-c))}x = {d-b}")
    sleep(printing_time)
    print(f"{adjust_x(a-c)}x = {d-b}")
    sleep(printing_time)    
    if(a == c):        
        print("x = Ø car l'equation n'admet aucune solution réelle")
    else:
        print(f"x = {d-b}/{a-c}")
        sleep(printing_time)
        print(f"x = {(d-b)/(a-c)}")
    sleep(printing_time)

"""
if(cant_be_0 == False):

    cst = input(f"{name} = ")
    while(((cst.replace(".","")).replace("-","")).isdecimal() == False): 
        print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        cst = input(f"{name} = ")  
else:

    while(((cst.replace(".","")).replace("-","")).isdecimal() == False or int(cst) == 0):
        
        if(((cst.replace(".","")).replace("-","")).isdecimal() == False):
            print("\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")
        else:
            print(f"ERREUR : {name} ne peux être nul \nVeuillez réessayer : \n")
        cst = input(f"{name} = ")"""