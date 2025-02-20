import webview

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
    <h2>Ejemplo de Fórmulas Matemáticas con KaTeX</h2>
    
    <p>Esta es una ecuación en línea: \\( E = mc^2 \\)</p>

    <p>Ecuación en bloque:</p>
    <p>$$
    \\sum_{i=1}^{n} i = \\frac{n(n+1)}{2}
    $$</p>

    <p>Otra ecuación más avanzada:</p>
    <p>$$
    \\int_{0}^{\\infty} e^{-x^2} dx = \\frac{\\sqrt{\\pi}}{2}
    $$</p>
</body>
</html>
"""

# Crear una ventana con el navegador embebido
webview.create_window("KaTeX en Tkinter", html=html_content)
webview.start()
