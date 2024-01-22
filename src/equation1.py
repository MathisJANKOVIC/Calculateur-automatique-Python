from utils import PRINTING_TIMELAPS, CONTINUE_MESSAGE, get_user_value
from adjustors import adjust_sign, adjust_type, adjustx
import main

import time
import os

def run():
    os.system('cls' if(os.name == 'nt') else 'clear')
    print("\n Résolvons l'équation du type ax + b = 0 (a ≠ 0)\n")

    a = get_user_value('a', null_ok=False)
    b = get_user_value('b')

    a = adjust_type(a)
    b = adjust_type(b)

    print(f"\n {adjustx(a)}x {adjust_sign(b)} = 0")
    time.sleep(PRINTING_TIMELAPS)
    print(f" {adjustx(a)}x = {-b}")
    time.sleep(PRINTING_TIMELAPS)
    print(f" x = {-b}/{a}")
    time.sleep(PRINTING_TIMELAPS)
    print(f" x = {-b/a}\n")

    input(CONTINUE_MESSAGE + " ")
    main.main()

if(__name__ == "__main__"):
    main.main()