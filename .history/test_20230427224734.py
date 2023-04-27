import tkinter as tk

# Créer une fonction qui ouvre une nouvelle fenêtre


def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("Nouvelle fenêtre")
    new_window.geometry("300x200")
    new_label = tk.Label(new_window, text="Ceci est une nouvelle fenêtre")
    new_label.pack()


# Créer la fenêtre principale
root = tk.Tk()
root.title("Fenêtre principale")
root.geometry("400x300")

# Créer un bouton pour ouvrir une nouvelle fenêtre
new_window_button = tk.Button(
    root, text="Nouvelle fenêtre", command=open_new_window)
new_window_button.pack()

# Créer un bouton pour fermer la fenêtre
close_button = tk.Button(root, text="Retour", command=root.destroy)
close_button.pack()

# Boucle principale pour afficher la fenêtre
root.mainloop()
