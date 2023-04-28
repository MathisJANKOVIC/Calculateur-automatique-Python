def main():
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