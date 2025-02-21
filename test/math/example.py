from PIL import Image

# Compatibilidad con versiones antiguas
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS

from tkinter import Tk

from tkhtmlview import HTMLLabel

# Crear la ventana principal
root = Tk()
root.title("Imagen desde URL")
root.geometry("400x400")

# HTML con imagen desde URL
html_code = """
<h1>Imagen en línea</h1>
<img src="https://media.istockphoto.com/id/1985248194/photo/businessman-using-laptop-computer-with-digital-padlock-on-internet-technology-networking.jpg?s=2048x2048&w=is&k=20&c=9qSW4Y_THSsxS7LasJNxS0Tcvt8tIcICVyWy8_aCCNw=" width="200" height="100">
"""

# Mostrar la imagen en la ventana
label = HTMLLabel(root, html=html_code)
label.pack(fill="both", expand=True)

root.mainloop()
