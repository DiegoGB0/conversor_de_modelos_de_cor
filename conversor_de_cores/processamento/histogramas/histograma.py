from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import cv2
#inspetor de pixels
from processamento.histogramas.inspetor_px import abrir_inspetor


def mostrar_histograma(imagem, titulo="RGB"):
    janela = tk.Toplevel()
    janela.title(f"Histograma - {titulo}")
    janela.geometry("800x600")
 #------------------- inspetorpx ----------------   
    tk.Button(
        janela,
        text="Inspecionar Pixels",
        command=lambda: abrir_inspetor(imagem)
    ).pack(pady=5)
#----------------------------------------------

    fig = Figure(figsize=(8, 5))
    ax = fig.add_subplot(111)

    canais = [
        ("Vermelho", "r"),
        ("Verde", "g"),
        ("Azul", "b")
    ]

    for i, (nome, cor) in enumerate(canais):

        hist = cv2.calcHist(
            [imagem],
            [i],
            None,
            [256],
            [0, 256]
        )

        ax.plot(
            hist,
            color=cor,
            label=nome
        )

    ax.set_title(f"Histograma do Modelo {titulo}")
    ax.set_xlabel("Intensidade")
    ax.set_ylabel("Quantidade de Pixels")
    ax.legend()
    ax.grid(True)

    canvas = FigureCanvasTkAgg(
        fig,
        master=janela
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )