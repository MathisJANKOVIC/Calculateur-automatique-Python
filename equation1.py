from utility import adjust_sign, adjust_x, is_decimal, adjust_type, PRINTING_TIME
import time
import math
import os

def main():
    print("Résolvons l'équation du type ax + b = 0 (a > 0)\n")

    a = input("a = ")
    b = input("b = ")

    #if(is_decimal(a) and is_)

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
    time.sleep(PRINTING_TIME)
    print(f"{adjust_x(a)}x = {-b}")
    time.sleep(PRINTING_TIME)
    print(f"x = {-b}/{a}")
    time.sleep(PRINTING_TIME)
    print(f"x = {-b/a}")
    time.sleep(PRINTING_TIME)
