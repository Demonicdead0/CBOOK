from matplotlib import pyplot as plt

def latexToPng(formula: str, salida: str) -> None:
    latex_expression = r"$%s$" % formula
    print(latex_expression)
    fig = plt.figure(figsize=(max(len(latex_expression)*0.2,3),1))
    text = fig.text(
        x = .5,
        y = .5,
        s = latex_expression,
        horizontalalignment="center",
        verticalalignment="center",
        fontsize=10,
        
    )
    plt.savefig(salida)
    print(f"save in {salida}")