try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class Ir(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        # contenido
        self.ruta = tk.Label(self, text=self.controller.ruta_carpeta)
        self.ruta.pack()
        
    
    def update(self):
        self.ruta.config(text=self.controller.ruta_carpeta)