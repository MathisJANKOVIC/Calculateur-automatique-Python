from config import SCREEN_WIDTH, SCREEN_HEIGHT, FONT_FAMILY
import equation1
import equation2
import equation3
import tkinter

def new_equation1():
    window.destroy()
    equation1.main()
def new_equation2():
    window.destroy()
    equation2.main()

def new_equation3():
    window.destroy()
    equation3.main()

window = tkinter.Tk()
window.title("Solver Master - Menu")
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
window.resizable(width = False, height = False)

lab_title = tkinter.Label(window, text="Quel type d'équation vous-voulez résoudre ?", font=(FONT_FAMILY, 17))
lab_title.pack(pady=(SCREEN_HEIGHT/9, SCREEN_HEIGHT/13))

equations_frame = tkinter.Frame(window)
equations_frame.pack()

eq1 = tkinter.Button(equations_frame, text="ax + b = 0", font=("Arial", 14), fg="black", width=SCREEN_WIDTH//33, command=new_equation1)
eq1.pack(pady=SCREEN_WIDTH/65)
eq2 = tkinter.Button(equations_frame, text="ax² + bx + c = 0", font=("Arial", 15), width=SCREEN_WIDTH//33, command=new_equation2)
eq2.pack(pady=SCREEN_WIDTH/65)
eq3 = tkinter.Button(equations_frame, text="ax + b = cx + d", font=("Arial", 15), width=SCREEN_WIDTH//33, command=new_equation3)
eq3.pack(pady=SCREEN_WIDTH/65)

window.mainloop()
