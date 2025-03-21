import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog


class TextEditor:

    current_file: str|None = None

    last_saved_content: str = ""

    def __init__(self, window):
        self.window = window
        self.text_widget = scrolledtext.ScrolledText(window, wrap=tk.WORD, undo=True, maxundo=-1)
        self.text_widget.pack(expand=True, fill='both')

        self.set_current_file(None)
        self.text_widget.bind("<KeyRelease>", lambda event: self.update_title())
        self.text_widget.bind("<Control-z>", lambda event: self.undo())
        self.text_widget.bind("<Control-y>", lambda event: self.redo())
        self.text_widget.bind("<Control-x>", lambda event: self.cut())
        self.text_widget.bind("<Control-c>", lambda event: self.copy())
        self.text_widget.bind("<Control-v>", lambda event: self.paste())
        self.text_widget.bind("<Control-a>", lambda event: self.select_all())
        self.text_widget.bind("<Control-n>", lambda event: self.new_file())
        self.text_widget.bind("<Control-o>", lambda event: self.open_file())
        self.text_widget.bind("<Control-w>", lambda event: self.close_file())
        self.text_widget.bind("<Control-s>", lambda event: self.save_file())
        self.text_widget.bind("<Control-S>", lambda event: self.save_as_file())

        menu_bar = tk.Menu(window)
        window.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Close", command=self.close_file, accelerator="Ctrl+W")

        edit_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=self.cut, accelerator="Ctrl+X")
        edit_menu.add_command(label="Copy", command=self.copy, accelerator="Ctrl+C")
        edit_menu.add_command(label="Paste", command=self.paste, accelerator="Ctrl+V")
        edit_menu.add_separator()
        edit_menu.add_command(label="Select All", command=self.select_all, accelerator="Ctrl+A")

    def get_content(self) -> str:
        content = self.text_widget.get(1.0, tk.END)
        if content.endswith('\n'):
            content = content[:len(content)-1]
        if content.endswith('\n'):
            content = content[:len(content)-1]
        return content

    def set_content(self, content: str) -> None:
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(tk.END, content)

    def has_unsaved_changes(self) -> bool:
        return self.last_saved_content != self.get_content()

    def clear_unsaved_changes(self) -> None:
        self.last_saved_content = self.get_content()
        self.update_title()

    def update_title(self) -> None:
        self.window.title(f"Text Editor - {self.current_file or 'Untitled'}{'*' if self.has_unsaved_changes() else ''}")

    def set_current_file(self, file_path: str|None) -> None:
        self.current_file = file_path
        self.clear_unsaved_changes()

    def undo(self):
        self.text_widget.event_generate("<<Undo>>")
        return "break"

    def redo(self):
        self.text_widget.event_generate("<<Redo>>")
        return "break"

    def cut(self):
        self.text_widget.event_generate("<<Cut>>")
        return "break"

    def copy(self):
        self.text_widget.event_generate("<<Copy>>")
        return "break"

    def paste(self):
        self.text_widget.event_generate("<<Paste>>")
        return "break"

    def select_all(self):
        self.text_widget.tag_add(tk.SEL, 1.0, tk.END)
        return "break"

    def new_file(self):
        if self.has_unsaved_changes():
            result = messagebox.askyesnocancel("Unsaved Changes", "Changes to the current file will be lost if you create a new file. Create new file anyway?")
            if result is not True:
                return  # user cancelled or pressed no
        self.set_content("")
        self.set_current_file(None)

    def open_file(self):
        if self.has_unsaved_changes():
            result = messagebox.askyesnocancel("Unsaved Changes", "Changes to the current file will be lost if you open a new file. Open new file anyway?")
            if result is not True:
                return  # user cancelled or pressed no
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.set_content(content)
                self.set_current_file(file_path)

    def close_file(self):
        if self.has_unsaved_changes():
            result = messagebox.askyesnocancel("Unsaved Changes", "Changes to the current file will be lost if you close it. Close anyway?")
            if result is not True:
                return  # user cancelled or pressed no
        if self.current_file is None:
            self.window.destroy()
        else:
            self.set_content("")
            self.set_current_file(None)

    def save_file(self):
        if self.current_file is None:
            self.save_as_file()
        else:
            with open(self.current_file, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)
            self.clear_unsaved_changes()
            messagebox.showinfo("Saved", "File saved successfully.")

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)
            self.set_current_file(file_path)
            messagebox.showinfo("Saved", "File saved successfully.")


if __name__ == "__main__":
    window = tk.Tk()
    TextEditor(window)
    window.mainloop()