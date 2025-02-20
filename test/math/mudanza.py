import tkinter as tk
from tkinterweb import HtmlFrame

# Código HTML con KaTeX
html_content = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body);"></script>
</head>
<body>
    <h2>Prueba con KaTeX en tkinterweb</h2>
    <p>$$E = mc^2$$</p>
    <p>$$\\frac{a}{b} + \\sqrt{x}$$</p>
</body>
</html>
"""

# Ventana principal
root = tk.Tk()
root.title("KaTeX en Tkinter con tkinterweb")

# Crear el navegador
browser = HtmlFrame(root)
browser.pack(fill="both", expand=True)

# Cargar el HTML con KaTeX
browser.load_html(html_content)

root.mainloop()
