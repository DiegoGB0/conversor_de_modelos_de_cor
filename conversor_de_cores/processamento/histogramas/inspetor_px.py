import customtkinter as ctk
from PIL import Image, ImageTk, ImageDraw


def abrir_inspetor(imagem):

    janela = ctk.CTkToplevel()

    janela.title("Inspetor de Pixels")
    janela.geometry("1200x800")

    janela.bind(
        "<Escape>",
        lambda e: janela.destroy()
    )

    # ================= CONTAINER PRINCIPAL =================

    frame_principal = ctk.CTkFrame(
        janela,
        fg_color="transparent"
    )

    frame_principal.pack(
        fill="both",
        expand=True,
        padx=20,
        pady=20
    )

    # ================= ÁREA DA IMAGEM =================

    frame_imagem = ctk.CTkFrame(
        frame_principal
    )

    frame_imagem.pack(
        side="left",
        fill="both",
        expand=True,
        padx=(0, 15)
    )

    ctk.CTkLabel(
        frame_imagem,
        text="IMAGEM DE INSPEÇÃO",
        font=("Arial", 18, "bold")
    ).pack(pady=15)

    altura_original, largura_original = imagem.shape[:2]

    img_pil = Image.fromarray(imagem)

    img_pil.thumbnail(
        (800, 650)
    )

    largura_exibida = img_pil.width
    altura_exibida = img_pil.height

    img_tk = ImageTk.PhotoImage(
        img_pil
    )

    label_img = ctk.CTkLabel(
        frame_imagem,
        text="",
        image=img_tk
    )

    label_img.image = img_tk

    label_img.pack(
        pady=10
    )

    label_img.configure(
        cursor="crosshair"
    )

    # ================= PAINEL LATERAL =================

    frame_lateral = ctk.CTkFrame(
        frame_principal,
        width=300
    )

    frame_lateral.pack(
        side="right",
        fill="y"
    )

    frame_lateral.pack_propagate(
        False
    )

    # ---------- TÍTULO ----------

    ctk.CTkLabel(
        frame_lateral,
        text="DETALHES DO PIXEL",
        font=("Arial", 16, "bold")
    ).pack(
        anchor="w",
        padx=15,
        pady=(20, 15)
    )

    # ---------- INFORMAÇÕES ----------

    label_info = ctk.CTkLabel(
        frame_lateral,
        text="Passe o mouse sobre a imagem",
        justify="left",
        anchor="w",
        font=("Arial", 14)
    )

    label_info.pack(
        anchor="w",
        padx=15,
        pady=(0, 20)
    )

    # ---------- AMOSTRA DE COR ----------

    ctk.CTkLabel(
        frame_lateral,
        text="AMOSTRA DE COR",
        font=("Arial", 14, "bold")
    ).pack(
        anchor="w",
        padx=15
    )

    label_cor = ctk.CTkFrame(
        frame_lateral,
        width=220,
        height=80,
        corner_radius=12
    )

    label_cor.pack(
        padx=15,
        pady=10
    )

    label_cor.pack_propagate(
        False
    )

    # ---------- LUPA ----------

    ctk.CTkLabel(
        frame_lateral,
        text="VISTA AMPLIADA",
        font=("Arial", 14, "bold")
    ).pack(
        anchor="w",
        padx=15,
        pady=(15, 5)
    )

    frame_lupa = ctk.CTkFrame(
        frame_lateral,
        width=220,
        height=220,
        corner_radius=12
    )

    frame_lupa.pack(
        padx=15,
        pady=5
    )

    frame_lupa.pack_propagate(
        False
    )

    label_lupa = ctk.CTkLabel(
        frame_lupa,
        text=""
    )

    label_lupa.pack(
        expand=True
    )

    # ---------- RODAPÉ ----------

    ctk.CTkLabel(
        frame_lateral,
        text="Modo inspeção ativo.\nPressione ESC para sair.",
        justify="left"
    ).pack(
        anchor="w",
        padx=15,
        pady=20
    )

    # ================= EVENTO =================

    def mostrar_pixel(evento):

        x_tela = evento.x
        y_tela = evento.y

        if not (
            0 <= x_tela < largura_exibida and
            0 <= y_tela < altura_exibida
        ):
            return

        x = int(
            x_tela * largura_original / largura_exibida
        )

        y = int(
            y_tela * altura_original / altura_exibida
        )

        b = int(imagem[y, x, 0])
        g = int(imagem[y, x, 1])
        r = int(imagem[y, x, 2])

        hex_cor = f"#{r:02X}{g:02X}{b:02X}"

        # ---------- INFO ----------

        label_info.configure(
            text=
            f"Posição: ({x}, {y})\n\n"
            f"RGB: ({r}, {g}, {b})\n\n"
            f"HEX: {hex_cor}"
        )

        # ---------- COR ----------

        label_cor.configure(
            fg_color=hex_cor
        )

        # ---------- LUPA ----------

        inicio_x = max(
            0,
            x - 10
        )

        fim_x = min(
            largura_original,
            x + 10
        )

        inicio_y = max(
            0,
            y - 10
        )

        fim_y = min(
            altura_original,
            y + 10
        )

        regiao = imagem[
            inicio_y:fim_y,
            inicio_x:fim_x
        ]

        img_zoom = Image.fromarray(
            regiao
        )

        img_zoom = img_zoom.resize(
            (220, 220),
            Image.NEAREST
        )

        # ---------- MIRA CENTRAL ----------

        draw = ImageDraw.Draw(
            img_zoom
        )

        centro = img_zoom.width // 2

        # sombra preta

        draw.line(
            (
                centro - 16,
                centro,
                centro + 16,
                centro
            ),
            fill="black",
            width=4
        )

        draw.line(
            (
                centro,
                centro - 16,
                centro,
                centro + 16
            ),
            fill="black",
            width=4
        )

        # linha branca

        draw.line(
            (
                centro - 15,
                centro,
                centro + 15,
                centro
            ),
            fill="white",
            width=2
        )

        draw.line(
            (
                centro,
                centro - 15,
                centro,
                centro + 15
            ),
            fill="white",
            width=2
        )

        zoom_tk = ImageTk.PhotoImage(
            img_zoom
        )

        label_lupa.configure(
            image=zoom_tk
        )

        label_lupa.image = zoom_tk

    label_img.bind(
        "<Motion>",
        mostrar_pixel
    )