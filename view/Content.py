try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
    from os import listdir
    from os import path
    from pathlib import Path
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2


class Content(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # contenido 
        self.label = tk.Label(self,text="hola, este es el menu")
        self.label.pack()