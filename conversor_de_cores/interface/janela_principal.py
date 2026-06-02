import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

# Imagem / processamento
from processamento.imagem import (
    abrir_imagem,
    converter_para_numpy,
    converter_para_pil
)

# HSV
from processamento.conversores.rgb_para_hsv import converter as rgb_para_hsv

# CMYK
from processamento.conversores.rgb_para_cmyk import converter as rgb_para_cmyk
from processamento.conversores.cmyk_para_rgb import converter as cmyk_para_rgb


class JanelaPrincipal:
    def __init__(self):
        self.janela = tk.Tk()
        self.imagem = None

        self.configurar_janela()
        self.criar_componentes()

    def configurar_janela(self):
        self.janela.title("Conversor de Modelos de Cor")
        self.janela.geometry("1000x700")

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

        tk.Button(
            self.janela,
            text="Converter para HSV",
            command=self.converter_para_hsv
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Converter para CMYK",
            command=self.converter_para_cmyk
        ).pack(pady=5)

    # ---------------- IMAGEM ----------------
    def abrir_imagem(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")]
        )

        if caminho:
            self.carregar_imagem(caminho)

    def carregar_imagem(self, caminho):
        self.imagem = abrir_imagem(caminho)
        self.exibir_imagem(self.imagem)

    def exibir_imagem(self, imagem):
        img = imagem.copy()
        img.thumbnail((800, 500))

        img_tk = ImageTk.PhotoImage(img)

        self.label_imagem.config(image=img_tk)
        self.label_imagem.image = img_tk

    # ---------------- CONVERSÕES ----------------
    def converter_para_hsv(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(self.imagem)

        img_hsv = rgb_para_hsv(img_np)

        self.imagem = converter_para_pil(img_hsv)
        self.exibir_imagem(self.imagem)

    def converter_para_cmyk(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(self.imagem)

        # RGB -> CMYK
        img_cmyk = rgb_para_cmyk(img_np)

        print("Primeiro pixel CMYK:", img_cmyk[0][0])

        # CMYK -> RGB (pra exibir)
        img_rgb = cmyk_para_rgb(img_cmyk)

        self.imagem = converter_para_pil(img_rgb)
        self.exibir_imagem(self.imagem)

    # ---------------- EXECUÇÃO ----------------
    def executar(self):
        self.janela.mainloop()