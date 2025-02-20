import tkinter as tk
from tkinter import *
from cefpython3 import cefpython as cef
import ctypes
import sys

def main():
    sys.excepthook = cef.ExceptHook  # Manejo de errores
    settings = {
        "multi_threaded_message_loop": True  # Usar CEF en modo multihilo
    }
    cef.Initialize(settings)

    win = Tk()
    win.minsize(800, 600)
    win.grid_columnconfigure(0, weight=1)
    win.grid_columnconfigure(1, weight=2)
    win.grid_rowconfigure(0, weight=1)

    # Editor de texto
    editor_frame = Frame(win, bg="white")
    editor_frame.grid(row=0, column=0, sticky="nswe")
    text_editor = tk.Text(editor_frame, wrap=tk.WORD)
    text_editor.pack(fill=tk.BOTH, expand=True)
    text_editor.insert(tk.END, "Hola, puedes editarme sin problemas ahora!")

    # Crear el frame del navegador
    frame = Frame(win, bg='black')
    frame.grid(row=0, column=1, sticky=('nswe'))

    # Navegador embebido
    browser_frame = BrowserFrame(frame)
    browser_frame.pack(fill=tk.BOTH, expand=tk.YES)

    texto = tk.Label(frame, text="Hola, me llamo Jhamsid")
    texto.pack()

    # Cerrar la aplicación correctamente
    def cerrar():
        cef.Shutdown()
        win.destroy()

    win.protocol("WM_DELETE_WINDOW", cerrar)
    win.mainloop()

class BrowserFrame(tk.Frame):
    def __init__(self, mainframe, navigation_bar=None):
        super().__init__(mainframe)
        self.navigation_bar = navigation_bar
        self.closing = False
        self.browser = None
        self.mainframe = mainframe
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)
        self.bind("<Configure>", self.on_configure)
        self.focus_set()

    def embed_browser(self):
        """Inicializar el navegador embebido."""
        window_info = cef.WindowInfo()
        rect = [0, 0, self.winfo_width(), self.winfo_height()]
        window_info.SetAsChild(self.get_window_handle(), rect)
        self.browser = cef.CreateBrowserSync(
            window_info,
            url="file:///C:/Users/USER/Desktop/proyectos/2025/enero/cbook/test/math/index.html"
        )
        assert self.browser

    def get_window_handle(self):
        if self.winfo_id() > 0:
            return self.winfo_id()
        else:
            raise Exception("No se pudo obtener el ID de la ventana")

    def on_configure(self, _):
        if not self.browser:
            self.embed_browser()

    def on_focus_in(self, _):
        if self.browser:
            self.browser.SetFocus(True)

    def on_focus_out(self, _):
        pass

    def on_root_close(self):
        if self.browser:
            self.browser.CloseBrowser(True)
            self.clear_browser_references()
        else:
            self.destroy()

    def clear_browser_references(self):
        self.browser = None


if __name__ == '__main__':
    main()
