try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
    from tkinter import filedialog
    from tkinter import scrolledtext
    import markdown
    from tkinterweb import HtmlFrame
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

        # Area de texto para escribir Markdown
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Courier", 12))
        #self.text_area.grid(row = 0, column=0, sticky="nsew", padx=5, pady=5)
        self.text_area.pack()

        # Vista previa en un navegador embebido
        self.html_frame = HtmlFrame(self)
        #self.html_frame.grid(row=0, column = 1, sticky="nsew", padx = 5, pady = 5)
        self.html_frame.pack()

        # botón para convertir Markdown a HTML (posiblemente construya desde cero)
        # Ahora solo estoy usando una librería
        self.btn_convert = tk.Button(self, text="Actualizar", command=self.convert_markdown)

    def convert_markdown(self):
        raw_text = self.text_area.get("1.0", tk.END)
        html_content = markdown.markdown(raw_text, extensions=["fenced_code"])

        styled_html = f"""
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; padding: 10px; }}
                pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; }}
                code {{ color: #d63384; }}
            </style>
        </head>
        <body>{html_content}</body>
        </html>
        """
        self.html_frame.load_html(styled_html)