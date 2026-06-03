import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import numpy as np

# histograma
from processamento.histogramas.histograma import mostrar_histograma

# Imagem / processamento
from processamento.imagem import (
    abrir_imagem,
    converter_para_numpy,
    converter_para_pil
)

#ajustes
from processamento.ajustes.brilho import aplicar_brilho
from processamento.ajustes.contraste import aplicar_contraste

# HSV
from processamento.conversores.rgb_para_hsv import converter as rgb_para_hsv
from processamento.conversores.hsv_para_rgb import converter as hsv_para_rgb

# CMYK
from processamento.conversores.rgb_para_cmyk import converter as rgb_para_cmyk
from processamento.conversores.cmyk_para_rgb import converter as cmyk_para_rgb
# CMY
from processamento.conversores.rgb_para_cmy import converter as rgb_para_cmy
from processamento.conversores.cmy_para_rgb import converter as cmy_para_rgb


class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.imagem = None

        self.configurar_janela()
        self.criar_componentes()
        self.modelo_atual = "RGB"

    def configurar_janela(self):
        self.janela.title("Conversor de Modelos de Cor")
        self.janela.geometry("1600x800")

    # ---------------- UI ----------------
    #jogar isso nos componentes.py
    
    def criar_componentes(self):

        self.label_imagem = tk.Label(self.janela)
        self.label_imagem.pack(pady=20)

        tk.Button(
            self.janela,
            text="Abrir Imagem",
            command=self.abrir_imagem
        ).pack(pady=5)
        # ----------------
        tk.Button(
            self.janela,
            text="Voltar à Original",
            command=self.voltar_original
        ).pack(pady=5)
        # ---------------- BRILHO ----------------
        tk.Label(
            self.janela,
            text="Brilho"
        ).pack()

        self.slider_brilho = tk.Scale(
            self.janela,
            from_=-100,
            to=100,
            orient="horizontal",
            length=300,
            command=self.ajustar_brilho
        )

        self.slider_brilho.pack()

        # ---------------- CONTRASTE ----------------
        tk.Label(
            self.janela,
            text="Contraste"
        ).pack()

        self.slider_contraste = tk.Scale(
            self.janela,
            from_=-100,
            to=100,
            orient="horizontal",
            length=300,
            command=self.ajustar_contraste
        )

        self.slider_contraste.pack()
        #------------------
        tk.Button(
            self.janela,
            text="Mostrar Histograma",
            command=self.abrir_histograma
        ).pack(pady=5)
        tk.Button(
            self.janela,
            text="Converter para HSV",
            command=self.converter_para_hsv
        ).pack(pady=5)
        # ----------------
        tk.Button(
            self.janela,
            text="Converter para CMYK",
            command=self.converter_para_cmyk
        ).pack(pady=5)
        # ----------------
        tk.Button(
            self.janela,
            text="Converter para CMY",
            command=self.converter_para_cmy
        ).pack(pady=5)
        #------------------


    # ---------------- IMAGEM ----------------
    def abrir_imagem(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")]
        )

        if caminho:
            self.carregar_imagem(caminho)

    def carregar_imagem(self, caminho):
        self.imagem_original = abrir_imagem(caminho)
        self.imagem = self.imagem_original.copy()
        self.slider_brilho.set(0)
        self.slider_contraste.set(0)
        self.exibir_imagem(self.imagem)

    def exibir_imagem(self, imagem):
        img = imagem.copy()
        img.thumbnail((800, 500))

        img_tk = ImageTk.PhotoImage(img)

        self.label_imagem.config(image=img_tk)
        self.label_imagem.image = img_tk

        # ---------------- BRILHO ----------------
    def ajustar_brilho(self, valor):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(
            self.imagem_original
        )

        img_brilho = aplicar_brilho(
            img_np,
            int(valor)
        )

        self.imagem = converter_para_pil(
            img_brilho
        )

        self.exibir_imagem(
            self.imagem
        )

    # ---------------- CONTRASTE ----------------
    def ajustar_contraste(self, valor):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(
            self.imagem_original
        )

        img_contraste = aplicar_contraste(
            img_np,
            int(valor)
        )

        self.imagem = converter_para_pil(
            img_contraste
        )

        self.exibir_imagem(
            self.imagem
        )    

    # ----------------  VOLTAR ----------------
    def voltar_original(self):

        if not hasattr(self, "imagem_original"):
            return

        self.imagem = self.imagem_original.copy()
        self.exibir_imagem(self.imagem)
        self.slider_brilho.set(0)
        self.slider_contraste.set(0)
        self.modelo_atual = "RGB"
    # ---------------- HISTOGRAMA ----------------
    def abrir_histograma(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(self.imagem)

        mostrar_histograma(
            img_np,
            titulo=self.modelo_atual
        )

    # ---------------- CONVERSÕES ----------------
    def converter_para_hsv(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(self.imagem_original)
        img_hsv = rgb_para_hsv(img_np)
        self.imagem = converter_para_pil(img_hsv)
        self.exibir_imagem(self.imagem)
        self.modelo_atual = "HSV"


    def converter_para_cmyk(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(self.imagem_original)
        img_cmyk = rgb_para_cmyk(img_np)
        img_cmy_vis = (img_cmyk[:, :, :3] * 255).astype(np.uint8)
        self.imagem = converter_para_pil(img_cmy_vis)
        self.exibir_imagem(self.imagem)
        self.modelo_atual = "CMYK"

    def converter_para_cmy(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(self.imagem_original)

        img_cmy = rgb_para_cmy(img_np)

        img_cmy_vis = (img_cmy * 255).astype(np.uint8)

        self.imagem = converter_para_pil(img_cmy_vis)

        self.exibir_imagem(self.imagem)
        self.modelo_atual = "CMY"
    # ---------------- EXECUÇÃO ----------------
    def executar(self):
        self.janela.mainloop()