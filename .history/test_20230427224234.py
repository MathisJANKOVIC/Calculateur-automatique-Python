import tkinter as tk

# Créer une fenêtre principale
window = tk.Tk()

# Créer une nouvelle frame
new_frame = tk.Frame(window)

# Ajouter des widgets à la nouvelle frame
tk.Label(new_frame, text="Nouvelle page").pack()
tk.Button(new_frame, text="Retourner à la page principale",
          command=lambda: window.destroy()).pack()

# Afficher la nouvelle frame
new_frame.pack()

# Démarrer la boucle d'événements
window.mainloop()
