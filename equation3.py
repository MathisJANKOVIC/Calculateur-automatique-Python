def main():
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