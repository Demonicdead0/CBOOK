from cefpython3 import cef
import tkinter as tk

class HTMLViewer:
    def __init__(self):
        self.browser = None
        self.window = tk.Tk()
        self.window.geometry("800x600")

        # Tkinter Textbox for live input
        self.textbox = tk.Text(self.window, height=5)
        self.textbox.pack(fill="x")
        self.textbox.bind("<KeyRelease>", self.update_code)  # Live update

        # Initialize CEF
        self.window.after(100, self.init_cef)
        self.window.mainloop()

    def init_cef(self):
        cef.Initialize()
        self.browser = cef.CreateBrowserSync(url="data:text/html," + self.generate_html("Type code here..."))
        self.window.after(100, self.embed_cef)

    def embed_cef(self):
        """Embed CEF into the Tkinter window"""
        frame_id = self.window.winfo_id()
        self.browser.SetParent(frame_id)
        cef.MessageLoopWork()

    def update_code(self, event=None):
        """Update HTML content live when user types"""
        new_code = self.textbox.get("1.0", tk.END).strip()
        if self.browser:
            js_code = f'document.getElementById("code").innerHTML = `{new_code}`;'
            self.browser.ExecuteJavascript(js_code)

    def generate_html(self, code):
        """Generate HTML with an editable code block"""
        return f"""
        <html>
        <head>
            <style>
                body {{ background-color: #2d2d2d; color: white; font-family: monospace; padding: 20px; }}
                pre {{ background-color: #272822; padding: 10px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <h2>Live Code Preview</h2>
            <pre id="code">{code}</pre>
        </body>
        </html>
        """

if __name__ == "__main__":
    HTMLViewer()
