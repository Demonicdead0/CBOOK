import matplotlib.pyplot as plt
import time

latex_expression = r"$e^{i\pi}+1=0$"
fig = plt.figure(figsize=(3, 0.5))  # Dimensions of figsize are in inches
text = fig.text(
    x=0.5,  # x-coordinate to place the text
    y=0.5,  # y-coordinate to place the text
    s=latex_expression,
    horizontalalignment="center",
    verticalalignment="center",
    fontsize=16,
)

a = time.time()
plt.savefig("hola.png")
print("Tiempo recurrido:",time.time() - a)

def latexToPng(formula: str, salida: str) -> None:
    latex_expression = formula
    fig = plt.figure(figsize=(3,0.5))
    text = fig.text(
        x = .5,
        y = .5,
        s = latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=16,
    )
    plt.savefig(salida)