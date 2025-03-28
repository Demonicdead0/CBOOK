import tkinter as tk                # python 3
from tkinter import font as tkfont  # python 3
from tkinter import filedialog
from tkinter import scrolledtext
import markdown
from module.markdown2 import markdown2
from tkinterweb import HtmlFrame
from os import listdir
from os import path
from pathlib import Path
import pdfkit
import time
# import weasyprint



class Content(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        #self.grid_propagate(False)

        # contenido 
        #self.label = tk.Label(self,text="hola, este es el menu")
        
        h = self.controller.winfo_screenheight()
        w = self.controller.winfo_screenwidth()

        # Area de texto para escribir Markdown
        print(w,h)
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Courier", 12)
                                                   ,width = w//(2*11), height = 20)
        #self.text_area.grid(row = 0, column=0, sticky="nsew", padx=5, pady=5)
        

        # Vista previa en un navegador embebido
        self.html_frame = HtmlFrame(self,width = 40, height = 20)
        #self.html_frame.grid(row=0, column = 1, sticky="nsew", padx = 5, pady = 5)
        

        # botón para convertir Markdown a HTML (posiblemente construya desde cero)
        # Ahora solo estoy usando una librería
        self.btn_convert = tk.Button(self, text="Actualizar", command=self.convert_markdown)

        self.retroceder = tk.Button(self, text="salir", command= lambda: self.back())

        self.btn_generarPDF = tk.Button(self, text="Generar PDF", command= lambda: self.generar_PDF())

        self.retroceder.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        #self.label.grid(row = 0, column=1, padx=5, pady=5,sticky="ew")
        self.btn_generarPDF.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.btn_convert.grid(row=0, column=2, padx=5, pady=5,sticky="ew")

        self.text_area.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        self.html_frame.grid(row=1, column = 1, columnspan = 2,sticky="nsew", padx=5, pady = 5)

        """
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)

        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)
        """
        

    def generar_PDF(self):
        raw_text = self.text_area.get("1.0", tk.END)
        #html_content = markdown.markdown(raw_text, extensions=["fenced_code"])
        html_content = markdown2(raw_text, self.controller.ruta_carpeta)
        styled_html = f"""
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{ font-family: Arial, sans-serif; padding: 10px; }}
                pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; }}
                code {{ color: #d63384; }}
            </style>

            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
            <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
            <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
                onload="renderMathInElement(document.body);"></script>
        </head>
        <body>{html_content}</body>
        </html>
        """
        archivo = path.join(self.controller.ruta_carpeta, "index.html")
        with open(archivo, "w", encoding = "utf-8") as f:
            f.write(styled_html)

        config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
        download_folder = path.join(path.expanduser("~"), "Downloads")
        pdfkit.from_file(archivo, path.join(download_folder,"hola.pdf"), configuration=config)
        print("pdf generado")

        


    def back(self):

        self.controller.ruta_carpeta = Path(self.controller.ruta_carpeta).parent.absolute()
        self.controller.show_frame("Ir")

    def convert_markdown(self):
        raw_text = self.text_area.get("1.0", tk.END)
        #html_content = markdown.markdown(raw_text, extensions=["fenced_code"])
        #markdown2(raw_text)
        html_content = markdown2(raw_text, self.controller.ruta_carpeta)
        with open("./style/estilo.css","r") as f:
            style = f.read()
        #print(html_content)
        styled_html = f"""
        <html>
        <head>
            <style>
                {style}
            </style>
        </head>
        <body>{html_content}</body>
        </html>
        """
        print(styled_html)
        archivo = path.join(self.controller.ruta_carpeta, "index.html")
        with open(archivo, "w", encoding = "utf-8") as f:
            f.write(styled_html)
            f.close()

        direccionHTML = Path(path.join(self.controller.ruta_carpeta, "index.html")).absolute()
        # Verificar si el archivo existe y cargarlo
        if direccionHTML.exists():
            html_file_url = direccionHTML.as_uri()
            print(f"Cargando desde: {html_file_url}")
            #self.html_frame.load_content("")
            tt = time.time()

            with open("temp/start.html", "r", encoding="utf-8") as f:
                inicio_html = f.read()
            
            self.html_frame.load_html(inicio_html)
            self.html_frame.load_file(html_file_url)
        else:
            print("❌ El archivo HTML no existe.")


        direccion = path.join(self.controller.ruta_carpeta, "main.md")
        with open(direccion, "w") as f:
            f.write(raw_text)
        f.close()
            
    
    def update(self):
        self.text_area.delete("1.0", tk.END)
        direccion = path.join(self.controller.ruta_carpeta, "main.md")
        with open(direccion, "r") as f:
            self.text_area.insert(tk.INSERT, f.read())
        
        self.convert_markdown()
        print(self.controller.ruta_carpeta)
        #self.html_frame.reload()