import tkinter as tk
from tkinter import scrolledtext
import markdown
from tkinterweb import HtmlFrame

class MarkdownEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor Markdown con Vista HTML")

        # Configuración de la ventana
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # Área de texto para escribir Markdown
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12))
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Vista previa en un navegador embebido
        self.html_frame = HtmlFrame(root)
        self.html_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Botón para convertir Markdown a HTML y mostrarlo
        self.btn_convert = tk.Button(root, text="Actualizar Vista", command=self.convert_markdown)
        self.btn_convert.grid(row=1, column=0, columnspan=2, pady=5)

    def convert_markdown(self):
        raw_text = self.text_area.get("1.0", tk.END)
        html_content = markdown.markdown(raw_text, extensions=["fenced_code"])
        
        # Aplicar un estilo básico para mejorar la visualización
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

if __name__ == "__main__":
    root = tk.Tk()
    app = MarkdownEditor(root)
    root.mainloop()
