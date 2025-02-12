import tkinter as tk
from tkinter import scrolledtext
from pygments import lex
from pygments.lexers import PythonLexer
from pygments.token import Token
from pygments.style import Style
from pygments.styles import get_style_by_name

class CodeEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Display in Tkinter")
        self.geometry("600x400")

        # Create a ScrolledText widget
        self.text = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Courier", 12))
        self.text.pack(expand=True, fill="both")

        # Sample code
        code = """def hello():
    print("Hello, World!")
"""
        self.insert_code(code, "native")  # Choose style (e.g., 'monokai', 'native', etc.)

    def insert_code(self, code, style_name):
        self.text.config(state="normal")
        self.text.delete("1.0", tk.END)

        lexer = PythonLexer()
        style = get_style_by_name(style_name)

        for token, content in lex(code, lexer):
            tag = str(token)
            self.text.insert(tk.END, content, tag)
            
            if token in style.styles:
                color = style.styles[token]
                if color:
                    fg_color = color.strip().split()[0]  # Extract only the first color
                    if fg_color.startswith("#"):
                        fg_color = fg_color.lstrip("#")  # Remove extra #
                        fg_color = f"#{fg_color}"  # Re-add single #
                    else:
                        fg_color = "black"  # Default color

                    self.text.tag_config(tag, foreground=fg_color)

        self.text.config(state="disabled")


if __name__ == "__main__":
    app = CodeEditor()
    app.mainloop()
