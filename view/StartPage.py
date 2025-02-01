try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from style.botones import boton_direccion

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # contenido 
        label = tk.Label(self, text="Este es el menu principal", font = controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        # botones
        button_buscar = boton_direccion(self, text="Buscar archivo",
                                  command=lambda: controller.show_frame("Buscar"))
        button_ir = tk.Button(self, text = "Ir archivo",
                                command=lambda: controller.show_frame("Ir"))
        button_buscar.pack()
        button_ir.pack()
