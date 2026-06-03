from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import cv2


def mostrar_histograma(imagem, titulo="RGB"):
    janela = tk.Toplevel()
    janela.title(f"Histograma - {titulo}")
    janela.geometry("800x600")

    fig = Figure(figsize=(8, 5))
    ax = fig.add_subplot(111)

    cores = ("b", "g", "r")

    for i, cor in enumerate(cores):
        hist = cv2.calcHist(
            [imagem],
            [i],
            None,
            [256],
            [0, 256]
        )

        ax.plot(hist, color=cor)

    ax.set_title(f"Histograma do Modelo {titulo}")
    ax.set_xlabel("Intensidade")
    ax.set_ylabel("Quantidade de Pixels")

    canvas = FigureCanvasTkAgg(
        fig,
        master=janela
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )