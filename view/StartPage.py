try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

from style.botones import boton_direccion

class StartPage(tk.Frame):

    carpeta = "None"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # contenido 
        label = tk.Label(self, text="Este es el menu principal", font = controller.title_font)
        label.pack(side="top", fill="x", pady = 10)

        # botones
        #button_buscar = boton_direccion(self, text="Buscar archivo", command=lambda: controller.show_frame("Buscar"))
        #button_buscar = tk.Button(self, text="Seleccionar Carpeta", command=lambda: controller.show_frame("seleccionar"))

        direccionar = tk.Label(self, text=self.controller.ruta_carpeta)
        #direccionar.config(text="hola")

        button_buscar = tk.Button(self, text="Seleccionar Carpeta", command= lambda: self.seleccionar_carpeta(direccionar))
        button_crear = tk.Button(self, text = "Crear carpeta",
                                command=lambda: controller.show_frame("Crear"))
        button_go = tk.Button(self, text="Entrar", command=lambda: controller.show_frame("Ir"))
        direccionar.pack()
        button_buscar.pack()
        button_crear.pack()
        button_go.pack()
    
    def seleccionar_carpeta(self, letra : tk.Label):
        self.controller.seleccionar_carpeta()
        letra.config(text=self.controller.ruta_carpeta)

