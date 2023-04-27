import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("300x200")

        btn_close = tk.Button(self, text="Close", command=self.quit)
        btn_close.pack(pady=10)

        btn_new_window = tk.Button(
            self, text="New Window", command=self.open_new_window)
        btn_new_window.pack(pady=10)

    def open_new_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("New Window")
        new_window.geometry("200x100")

        btn_close = tk.Button(new_window, text="Close",
                              command=new_window.destroy)
        btn_close.pack(pady=10)


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
