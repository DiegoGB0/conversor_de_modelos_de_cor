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
    media_r = imagem[:, :, 0].mean()
    media_g = imagem[:, :, 1].mean()
    media_b = imagem[:, :, 2].mean()
    
    min_r = imagem[:, :, 0].min()
    max_r = imagem[:, :, 0].max()

    min_g = imagem[:, :, 1].min()
    max_g = imagem[:, :, 1].max()

    min_b = imagem[:, :, 2].min()
    max_b = imagem[:, :, 2].max()
    
    altura, largura = imagem.shape[:2]

    total_pixels = altura * largura

    '''    for i, (nome, cor) in enumerate(canais):

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
        )'''

    for i, (nome, cor) in enumerate(canais):

        hist = cv2.calcHist(
            [imagem],
            [i],
            None,
            [256],
            [0, 256]
        )

        hist = hist.flatten()

        ax.plot(
            hist,
            color=cor,
            linewidth=2,
            label=nome
        )

        ax.fill_between(
            range(256),
            hist,
            color=cor,
            alpha=0.25
        )
        
        
    ax.axvline(media_r, color="red", linestyle="--", alpha=0.7)
    ax.axvline(media_g, color="green", linestyle="--", alpha=0.7)
    ax.axvline(media_b, color="blue", linestyle="--", alpha=0.7)    

    info = (
    f"Pixels: {total_pixels:,}\n\n"
    f"R → Média: {media_r:.1f} | Min: {min_r} | Max: {max_r}\n"
    f"G → Média: {media_g:.1f} | Min: {min_g} | Max: {max_g}\n"
    f"B → Média: {media_b:.1f} | Min: {min_b} | Max: {max_b}"
    )

    ax.text(
        0.02,
        0.98,
        info,
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment="top",
        bbox=dict(
            boxstyle="round",
            facecolor="white",
            alpha=0.8
        )
    )



    ax.set_title(
        f"Histograma do Modelo {titulo}",
        fontsize=16,
        fontweight="bold"
        )
    ax.set_xlabel("Intensidade")
    ax.set_ylabel("Quantidade de Pixels")
    ax.legend()
    ax.grid(
        True,
        linestyle="--",
        alpha=0.5
            )

    canvas = FigureCanvasTkAgg(
        fig,
        master=janela
    )

    canvas.draw()

    canvas.get_tk_widget().pack(
        fill="both",
        expand=True
    )