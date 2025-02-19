import tkinter as tk
from tkinter import font as tkfont
from StartPage import *
from style.botones import *
from tkinter import filedialog
from Ir import *
from Content import *
from Create import *
from CrearCbook import *

class App(tk.Tk):
    ruta_carpeta = "sin cambio"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        heigh = self.winfo_screenheight()
        width = self.winfo_screenwidth()

        self.geometry("%dx%d" % (width, heigh))
        """El container es donde acumularemos los frames"""
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        #container.grid_columnconfigure(0, weight=1)
        #container.grid_columnconfigure(1, weight=1)
        #container.grid_columnconfigure(2, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Ir, Content, Create, CreateCbook):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row = 0, column = 0, sticky= "nsew")
        self.show_frame("StartPage")
    
    def show_frame(self, page_name):
        '''Muestra un frame con el nombre dado'''
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()

    def seleccionar_carpeta(self):
        self.ruta_carpeta = filedialog.askdirectory()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


# prueba de ejecucion

if __name__ == "__main__":
    app = App()
    app.mainloop()