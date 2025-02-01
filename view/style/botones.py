import tkinter as tk

class boton_direccion(tk.Button):
    def __init__(self, *args, **kwargs):
        if "foreground" not in kwargs:
            kwargs["foreground"] = "#ff0000"
        if "activeforeground" not in kwargs:
            kwargs["activeforeground"] = "#FFA500"
        super().__init__(*args, **kwargs)
