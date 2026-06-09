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

        # Frame das imagens
        frame_imagens = tk.Frame(self.janela)
        frame_imagens.pack(pady=20)

        # Imagem original
        frame_original = tk.Frame(frame_imagens)
        frame_original.pack(side="left", padx=30)

        tk.Label(
            frame_original,
            text="Imagem Original",
            font=("Arial", 12, "bold")
        ).pack()

        self.label_original = tk.Label(frame_original)
        self.label_original.pack()

        # Imagem modificada
        frame_modificada = tk.Frame(frame_imagens)
        frame_modificada.pack(side="left", padx=30)

        tk.Label(
            frame_modificada,
            text="Imagem Modificada",
            font=("Arial", 12, "bold")
        ).pack()

        self.label_modificada = tk.Label(frame_modificada)
        self.label_modificada.pack()
        '''self.label_modificada.bind(
            "<Motion>",
            self.mostrar_pixel
        )'''

        # Botões
        tk.Button(
            self.janela,
            text="Abrir Imagem",
            command=self.abrir_imagem
        ).pack(pady=5)

        tk.Button(
            self.janela,
            text="Voltar à Original",
            command=self.voltar_original
        ).pack(pady=5)

        # Brilho
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
            command=self.atualizar_imagem
        )

        self.slider_brilho.pack()

        # Contraste
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
            command=self.atualizar_imagem
        )

        self.slider_contraste.pack()
        
        #saturação
        tk.Label(
            self.janela,
            text="Saturação"
        ).pack()

        self.slider_saturacao = tk.Scale(
            self.janela,
            from_=-100,
            to=100,
            orient="horizontal",
            length=300,
            command=self.atualizar_imagem
        )

        self.slider_saturacao.pack()

        tk.Button(
            self.janela,
            text="Mostrar Histograma",
            command=self.abrir_histograma
        ).pack(pady=5)
        
#------------------ PIXEL ----------------

        '''self.label_pixel = tk.Label(
            self.janela,
            text="Pixel: ---",
            font=("Arial", 10)
        )

        self.label_pixel.pack(pady=5)'''
        
       

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

        tk.Button(
            self.janela,
            text="Converter para CMY",
            command=self.converter_para_cmy
        ).pack(pady=5)
        
        tk.Button(
            self.janela,
            text="Salvar Imagem",
            command=self.salvar_imagem
        ).pack(pady=5)

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

    def exibir_imagem_original(self, imagem):

        img = imagem.copy()
        img.thumbnail((600, 450))

        img_tk = ImageTk.PhotoImage(img)

        self.label_original.config(image=img_tk)
        self.label_original.image = img_tk

    def exibir_imagem(self, imagem):

        img = imagem.copy()
        img.thumbnail((600, 450))

        img_tk = ImageTk.PhotoImage(img)

        self.label_modificada.config(image=img_tk)
        self.label_modificada.image = img_tk

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
        
    #------------------ PIXEL ----------------
    '''def mostrar_pixel(self, evento):

        if self.imagem is None:
            return

        x = evento.x
        y = evento.y

        img_np = converter_para_numpy(self.imagem)

        altura, largura = img_np.shape[:2]

        if x >= largura or y >= altura:
            return

        b = img_np[y, x, 0]
        g = img_np[y, x, 1]
        r = img_np[y, x, 2]

        self.label_pixel.config(
            text=f"X={x} Y={y} | R={r} G={g} B={b}"
        )'''

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