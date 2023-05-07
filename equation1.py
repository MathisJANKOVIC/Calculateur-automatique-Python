from adjustors import *
from utils import *
import time

def main():
    time.sleep(0.3)
    print("Résolvons l'équation du type ax + b = 0 (a != 0)\n")

    a = get_user_value('a', null_ok=False)
    b = get_user_value('b')

    a = adjust_type(a)
    b = adjust_type(b)

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {-b}")
    time.sleep(PRINTING_TIME)
    print(f"x = {-b}/{a}")
    time.sleep(PRINTING_TIME)
    print(f"x = {-b/a}\n")

    input("Pressez 'Entrer' pour continuer... \n")
    whats_next()

if(__name__ == "__main__"):
    main()