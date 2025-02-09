import tkinter as tk
from tkinter import ttk

class boton_direccion(ttk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style = ttk.Style()
        self.imagen1 = tk.PhotoImage(file="..\\img\\botones\\boton_presionado.png")
        self.imagen2 = tk.PhotoImage(file="..\\img\\botones\\boton_principal.png")
        self.configure(image=self.imagen1)

        self.bind("<ButtonPress>", self.cambiar_a_presionado)
        self.bind("<ButtonRelease>", self.cambiar_a_normal)
    
    def cambiar_a_presionado(self, event= None):
        self.config(image=self.imagen1)

    def cambiar_a_normal(self, event= None):
        self.config(image=self.imagen2)

