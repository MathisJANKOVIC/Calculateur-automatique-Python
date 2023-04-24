def num_validation(name, cant_be_0 = False):

    while True:
        cst = input(f"{name} = ")
        if (((cst.replace(".", "")).replace("-", "")).isdecimal()):
            if (cant_be_0 == True):
                if (int(cst) != 0):
                    break
                else:
                    print(
                        f"\nERREUR : {name} ne peux être nul \nVeuillez réessayer : \n")
            else:
                break
        else:
            print(
                "\nERREUR : la saisie doit être un nombre en écriture décimale \nVeuillez réessayer : \n")

    if ("." in cst):
        return float(cst)
    else:
        return int(cst)

def adjust_sign(coef):

    if (type(coef) == int or type(coef) == float):
        if (coef > 0):
            return (f"+ {coef}")
        if (coef == 0):
            return ("")
        if (coef < 0):
            return (f"- {-coef}")
    else:
        if (coef == ""):
            return ("+ ")
        if (coef == "-"):
            return ("- ")


def adjust_x(coef):

    if (coef == 1):
        return ("")
    elif (coef == -1):
        return ("-")
    else:
        return (coef)
