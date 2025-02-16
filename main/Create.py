try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
    from os import listdir
    from os import path, mkdir  
    from pathlib import Path
    from tkinter import END
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class Create(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="nombre de la carpeta")
        self.entrada = tk.Text(self)
        boton = tk.Button(self, text="crear", command=self.crearlo)
        cancelar = tk.Button(self, text="regresar", command=lambda: self.controller.show_frame("Ir"))

        label.pack()
        self.entrada.pack()
        boton.pack()
        cancelar.pack()
    
    def crearlo(self):
        letra = self.entrada.get("1.0","end-1c")
        print(letra)
        direccion = path.join(self.controller.ruta_carpeta, letra)
        try:
            mkdir(direccion)
            print(f"{direccion} ha sido creado ")
        except FileExistsError:
            print(f"{direccion} Ya existe")
        except PermissionError:
            print(f"Permiso denegado para crear en {direccion}")
        self.entrada.insert(END, "")
        self.controller.show_frame("Ir")

