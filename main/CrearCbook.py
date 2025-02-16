try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
    from os import listdir
    from os import path, mkdir  
    from pathlib import Path
    from tkinter import END
    import json
    import datetime
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

class CreateCbook(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Nombre del archivo")
        self.entrada = tk.Text(self)
        boton = tk.Button(self, text="crear", command= lambda: self.crearlo())
        cancelar = tk.Button(self, text="regresar", command=lambda: self.controller.show_frame("Ir"))
        label.pack()
        self.entrada.pack()
        boton.pack()
        cancelar.pack()
    
    def crearlo(self):
        letra = self.entrada.get("1.0", "end-1c")
        print(letra)
        direccion = path.join(self.controller.ruta_carpeta, letra)
        try: 
            mkdir(direccion)
            print(f"{direccion} ha sido creado")
            inicio = path.join(direccion, "ini.cfg")
            f = open(inicio, "w")
            with open("model/template/template.cfg") as ff:
                js = json.loads(ff.read())
            js["name"] = letra
            dt = datetime.datetime.now()
            js["creation"] = dt.strftime("%m/%d/%Y : %H.%M")
            f.write(str(js))
            f.close()

        except FileExistsError:
            print(f"{direccion} Ya existe")
        except PermissionError:
            print(f"Permiso denegado para crear en la direccion {direccion}")
        self.entrada.insert(END, "")
        self.controller.show_frame("Ir")
