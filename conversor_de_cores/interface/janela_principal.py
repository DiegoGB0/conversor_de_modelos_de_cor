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

# ajustes
from processamento.ajustes.brilho import aplicar_brilho
from processamento.ajustes.contraste import aplicar_contraste
from processamento.ajustes.saturacao import aplicar_saturacao

# CONVERSORES
from processamento.conversores.rgb_para_hsv import converter as rgb_para_hsv
from processamento.conversores.rgb_para_cmyk import converter as rgb_para_cmyk
from processamento.conversores.rgb_para_cmy import converter as rgb_para_cmy

#criar botao
from interface.componentes import criar_botao

from interface.estilos import (
    criar_titulo,
    criar_label_ajuste,
    criar_frame_imagens,
    criar_frame_ajustes,
    criar_frame_botoes,
    criar_grupo,
    criar_divisoria
)

import customtkinter as ctk

class JanelaPrincipal:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        
        self.janela = ctk.CTk()
        self.imagem = None
        self.imagem_original = None
        self.imagem_base = None

        self.configurar_janela()
        self.criar_componentes()

        self.modelo_atual = "RGB"

    def configurar_janela(self):
        self.janela.title("Conversor de Modelos de Cor")
        self.janela.geometry("1600x800")

    # ---------------- UI ----------------

    def criar_componentes(self):

        # Área principal
        frame_principal = ctk.CTkFrame(self.janela)
        frame_principal.pack(
            anchor="w",
            padx=50,
            pady=20
        )

        # area das imagens
        frame_imagens = criar_frame_imagens(
            frame_principal
        )

        # area dos ajustes
        frame_ajustes = criar_frame_ajustes(
            frame_principal
        )
        
        #area dos botoes
        frame_botoes = criar_frame_botoes(
            self.janela
        )
        # GRUPOS DE BOTÕES
        grupo_1 = criar_grupo(frame_botoes)

        criar_divisoria(frame_botoes)

        grupo_2 = criar_grupo(frame_botoes)

        criar_divisoria(frame_botoes)

        grupo_3 = criar_grupo(frame_botoes)

        criar_divisoria(frame_botoes)

        grupo_4 = criar_grupo(frame_botoes)

        # ---------------- IMAGEM ORIGINAL ----------------

        frame_original = ctk.CTkFrame(frame_imagens)
        frame_original.pack(
            side="left",
            padx=30
        )

        criar_titulo(
            frame_original,
            "Imagem Original"
        )

        self.label_original = ctk.CTkLabel(
            frame_original,
            text=""
        )

        self.label_original.pack()

        # ---------------- IMAGEM MODIFICADA ----------------

        frame_modificada = ctk.CTkFrame(
            frame_imagens
        )

        frame_modificada.pack(
            side="left",
            padx=30
        )

        criar_titulo(
            frame_modificada,
            "Imagem Modificada"
        )

        self.label_modificada = ctk.CTkLabel(
            frame_modificada,
            text=""
        )

        self.label_modificada.pack()

        # ---------------- BOTÕES ----------------

        criar_botao(
            grupo_1,
            "Abrir Imagem",
            self.abrir_imagem
        )

        criar_botao(
            grupo_1,
            "Voltar à Original",
            self.voltar_original
        )

# ---------------- BRILHO ----------------

        criar_label_ajuste(
            frame_ajustes,
            "☀ Brilho"
        )

        self.slider_brilho = ctk.CTkSlider(
            frame_ajustes,
            from_=-100,
            to=100,
            command=self.atualizar_imagem,
            width=220
        )

        self.slider_brilho.set(0)

        self.slider_brilho.pack(
            padx=15,
            pady=10
        )

        # ---------------- CONTRASTE ----------------

        criar_label_ajuste(
            frame_ajustes,
            "◐ Contraste"
        )

        self.slider_contraste = ctk.CTkSlider(
            frame_ajustes,
            from_=-100,
            to=100,
            command=self.atualizar_imagem,
            width=220
        )

        self.slider_contraste.set(0)

        self.slider_contraste.pack(
            padx=15,
            pady=10
        )

        # ---------------- SATURAÇÃO ----------------

        criar_label_ajuste(
            frame_ajustes,
            "🎨 Saturação"
        )

        self.slider_saturacao = ctk.CTkSlider(
            frame_ajustes,
            from_=-100,
            to=100,
            command=self.atualizar_imagem,
            width=220
        )

        self.slider_saturacao.set(0)

        self.slider_saturacao.pack(
            padx=15,
            pady=10
        )

        # ---------------- OUTROS BOTÕES ----------------

        criar_botao(
            grupo_3,
            "Mostrar Histograma",
            self.abrir_histograma
        )

        criar_botao(
            grupo_2,
            "Converter para HSV",
            self.converter_para_hsv
        )

        criar_botao(
            grupo_2,
            "Converter para CMYK",
            self.converter_para_cmyk
        )

        criar_botao(
            grupo_2,
            "Converter para CMY",
            self.converter_para_cmy
        )

        criar_botao(
            grupo_4,
            "Salvar Imagem",
            self.salvar_imagem
        )
    # ---------------- IMAGEM ----------------

    def abrir_imagem(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")]
        )

        if caminho:
            self.carregar_imagem(caminho)

    def carregar_imagem(self, caminho):
        self.imagem_original = abrir_imagem(caminho)
        self.imagem_base = self.imagem_original.copy()
        self.imagem = self.imagem_base.copy()

        self.slider_brilho.set(0)
        self.slider_contraste.set(0)
        self.slider_saturacao.set(0)
        self.exibir_imagem_original(self.imagem_original)
        self.exibir_imagem(self.imagem)

    def exibir_imagem_label(self, label, imagem):

        img = imagem.copy()
        img.thumbnail((600, 450))

        img_tk = ImageTk.PhotoImage(img)

        label.configure(image=img_tk)
        label.image = img_tk


    def exibir_imagem_original(self, imagem):
        self.exibir_imagem_label(self.label_original, imagem)


    def exibir_imagem(self, imagem):
        self.exibir_imagem_label(self.label_modificada, imagem)

    # ---------------- AJUSTES ----------------

    def atualizar_imagem(self, valor=None):

        if self.imagem_original is None:
            return

        img_np = converter_para_numpy(
            self.imagem_base
        )

        # brilho
        brilho = self.slider_brilho.get()

        img_np = aplicar_brilho(
            img_np,
            brilho
        )

        # contraste
        contraste = self.slider_contraste.get()

        img_np = aplicar_contraste(
            img_np,
            contraste
        )
        
        #saturação
        saturacao = self.slider_saturacao.get()

        img_np = aplicar_saturacao(
            img_np,
            saturacao
        )

        self.imagem = converter_para_pil(
            img_np
        )

        self.exibir_imagem(
            self.imagem
        )

    # ---------------- VOLTAR ----------------

    def voltar_original(self):

        if self.imagem_original is None:
            return
        
        self.imagem_base = self.imagem_original.copy()
        self.imagem = self.imagem_original.copy()

        self.exibir_imagem(
            self.imagem
        )

        self.slider_brilho.set(0)
        self.slider_contraste.set(0)
        self.slider_saturacao.set(0)

        self.modelo_atual = "RGB"

    # ---------------- HISTOGRAMA ----------------

    def abrir_histograma(self):

        if self.imagem is None:
            return

        img_np = converter_para_numpy(
            self.imagem
        )

        mostrar_histograma(
            img_np,
            titulo=self.modelo_atual
        )
        

    # ---------------- CONVERSÕES ----------------

    def converter_para_hsv(self):

        if self.imagem_original is None:
            return

        img_np = converter_para_numpy(
            self.imagem_original
        )

        img_hsv = rgb_para_hsv(
            img_np
        )

        self.imagem_base = converter_para_pil(
            img_hsv
        )
        
        self.imagem = self.imagem_base.copy()

        self.exibir_imagem(
            self.imagem
        )

        self.modelo_atual = "HSV"

    def converter_para_cmyk(self):

        if self.imagem_original is None:
            return

        img_np = converter_para_numpy(
            self.imagem_original
        )

        img_cmyk = rgb_para_cmyk(
            img_np
        )

        img_cmy_vis = (
            img_cmyk[:, :, :3] * 255
        ).astype(np.uint8)

        self.imagem_base = converter_para_pil(
            img_cmy_vis
        )
        self.imagem = self.imagem_base.copy()

        self.exibir_imagem(
            self.imagem
        )

        self.modelo_atual = "CMYK"

    def converter_para_cmy(self):

        if self.imagem_original is None:
            return

        img_np = converter_para_numpy(
            self.imagem_original
        )

        img_cmy = rgb_para_cmy(
            img_np
        )

        img_cmy_vis = (
            img_cmy * 255
        ).astype(np.uint8)

        self.imagem_base = converter_para_pil(
            img_cmy_vis
        )
        self.imagem = self.imagem_base.copy()

        self.exibir_imagem(
            self.imagem
        )

        self.modelo_atual = "CMY"
    
#------------------ SALVAR IMAGEM ----------------
        
    def salvar_imagem(self):

        if self.imagem is None:
            return

        caminho = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG", "*.png"),
                ("JPEG", "*.jpg"),
                ("BMP", "*.bmp")
            ]
        )

        if caminho:
            self.imagem.save(caminho)

    # ---------------- EXECUÇÃO ----------------

    def executar(self):
        self.janela.mainloop()