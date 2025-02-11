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

class Ir(tk.Frame):

    # lista de elementos (direcciones y archivos)
    elementos = []
    nombres = []
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        

        # contenido
        self.ruta = tk.Label(self, text=self.controller.ruta_carpeta)
        self.ruta.pack()

        self.salir = tk.Button(self, text="Salir", command= lambda: self.controller.show_frame("StartPage"))
        self.crear_carpeta = tk.Button(self, text="Crear carpeta")
        self.crear_archivo = tk.Button(self, text="Crear texto")
        self.back = tk.Button(self, text="retroceder", command=lambda: self.retroceder())
        self.back.pack()
        self.salir.pack()
        self.crear_carpeta.pack()
        self.crear_archivo.pack()
    
    def retroceder(self):
        #print(self.controller.ruta_carpeta)
        #print(Path(self.controller.ruta_carpeta).parent.absolute())
        self.controller.ruta_carpeta = Path(self.controller.ruta_carpeta).parent.absolute()
        self.controller.show_frame("Ir")
    
    def direccionar(self, ruta: str):
        #print("##")
        #print(self.controller.ruta_carpeta)
        #print(ruta)
        #print(path.join(self.controller.ruta_carpeta, ruta))
        self.controller.ruta_carpeta = path.join(self.controller.ruta_carpeta, ruta)
        self.controller.show_frame("Ir")

    def update(self):
        #print("update")
        self.ruta.config(text=self.controller.ruta_carpeta)
        self.nombres = listdir(self.controller.ruta_carpeta)

        for botones in self.elementos:
            botones.config(text = "destruido")
            botones.destroy()
        self.elementos = []

        valores = []
        #print(self.nombres)
        for i in range(len(self.nombres)):
            name: str = self.nombres[i]
            if (self.nombres[i].count('.') == 0) or name.endswith(".md"):
                valores.append(self.nombres[i])
        
        #print(valores)
        for i in range(len(valores)):
            self.elementos.append(tk.Button(self, text=valores[i], command=lambda c = i: self.direccionar(self.elementos[c].cget("text"))))
            if valores[i].endswith(".md"):
                self.elementos[i].config(bg="blue");
            self.elementos[i].pack()