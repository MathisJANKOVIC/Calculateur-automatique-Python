from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_FAMILY
from utility import num_validation, adjust_sign, adjust_x
import tkinter

def main():
    window = tkinter.Tk()
    window.title("Solver Master - Equation du type ax + b = 0 ")
    window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    window.resizable(width = False, height = False)
    print("Résolvons l'équation du type ax + b = 0 (a > 0)\n")

    a = b = None
    a = num_validation("a", True)
    b = num_validation("b")

    print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
    print(f"{adjust_x(a)}x = {-b}")
    print(f"x = {-b}/{a}")
    print(f"x = {-b/a}")
