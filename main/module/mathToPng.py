from matplotlib import pyplot as plt

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