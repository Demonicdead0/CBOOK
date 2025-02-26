import markdown
import os 
from module.mathToPng import latexToPng
from pathlib import Path

def markdown2(texto: str, ruta: str) -> str:
    """
        hola: hace pequeños ajustes para convertirlo en markdown con ciertas propiedades
    """
    bloques: list = []
    bloques  = texto.split("$$")
    # las posiciones pares son texto y las impares son fórmulas
    resultado = ""
    x = 0
    print(len(bloques))
    for i in range(len(bloques)):
        if i&1:
            # img
            contenido:str = bloques[i].strip()
            ubicacion = os.path.join(ruta, "img", str(x) + ".png")
            latexToPng(contenido, ubicacion)
            ubicacion_url = ("img/") +(str(x) + ".png")
            resultado += f"\n <img src=\"{ubicacion_url}\">\n"
            x+=1
        else:
            # texto
            texto: str = bloques[i]
            texto = texto.replace("|", "***")
            contenido =  markdown.markdown(texto, extensions=["fenced_code"])
            resultado += contenido
    print("completado")
    return resultado

