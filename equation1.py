from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_FAMILY
from utility import adjust_sign, adjust_x, is_decimal, adjust_type
import tkinter.messagebox

ELEMENTS_WIDTH = SCREEN_WIDTH // 100
INPUTS_WIDTH = SCREEN_WIDTH // 80

def main():
    def calculate():
        a = a_input.get()
        b = b_input.get()

        if not(is_decimal(a) or is_decimal(b)):
            return tkinter.messagebox.showerror("Erreur","La saisie doit être un nombre en écriture décimale")

        a = adjust_type(a)
        b = adjust_type(b)

        #print("Résolvons l"équation du type ax + b = 0 (a > 0)\n")

        #a = b = None
        #a = num_validation("a", True)
        #b = num_validation("b")

        #print(f"\n{adjust_x(a)}x {adjust_sign(b)} = 0")
        #print(f"{adjust_x(a)}x = {-b}")
        #print(f"x = {-b}/{a}")
        #print(f"x = {-b/a}")

    window = tkinter.Tk()
    window.title("Solver Master - Equation du type ax + b = 0 ")
    window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
    window.resizable(width = False, height = False)
    window.iconbitmap("logo.ico")
    main_frame = tkinter.Frame(window, pady = SCREEN_HEIGHT//30)
    main_frame.pack()

    a_label = tkinter.Label(main_frame, text = "a =")
    a_label.pack(side="left")

    a_input = tkinter.Entry(main_frame,width=INPUTS_WIDTH)
    a_input.pack(side="left", padx=(2,10))

    b_label = tkinter.Label(main_frame, text="b =")
    b_label.pack(side="left")

    b_input = tkinter.Entry(main_frame,width=INPUTS_WIDTH)
    b_input.pack(side="left", padx=(2,4))

    calculate_button = tkinter.Button(main_frame, text="Calculer", width=INPUTS_WIDTH, command=calculate)
    calculate_button.pack(side="left", padx=(10,0))

    window.mainloop()

if(__name__ == "__main__"):
    main()
