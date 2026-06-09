import tkinter as tk
from PIL import Image, ImageTk


def abrir_inspetor(imagem):

    janela = tk.Toplevel()

    janela.title("Inspetor de Pixels")
    janela.geometry("1200x800")

    janela.bind(
        "<Escape>",
        lambda e: janela.destroy()
    )

    tk.Label(
        janela,
        text="Modo inspeção ativo. Pressione ESC para sair.",
        font=("Arial", 12, "bold")
    ).pack(pady=10)

    # ---------------- IMAGEM ----------------

    altura_original, largura_original = imagem.shape[:2]

    img_pil = Image.fromarray(imagem)

    img_pil.thumbnail((700, 500))

    largura_exibida = img_pil.width
    altura_exibida = img_pil.height

    img_tk = ImageTk.PhotoImage(img_pil)

    label_img = tk.Label(
        janela,
        image=img_tk,
        cursor="crosshair"
    )

    label_img.image = img_tk
    label_img.pack()

    # ---------------- INFORMAÇÕES ----------------

    label_info = tk.Label(
        janela,
        text="Passe o mouse sobre a imagem",
        font=("Arial", 12, "bold"),
        justify="left"
    )

    label_info.pack(pady=10)

    # ---------------- AMOSTRA DE COR ----------------

    label_cor = tk.Label(
        janela,
        width=15,
        height=5,
        bg="white",
        relief="solid",
        bd=2
    )

    label_cor.pack(pady=10)

    # ---------------- LUPA ----------------

    label_lupa = tk.Label(
        janela,
        bd=2,
        relief="solid"
    )

    label_lupa.pack(pady=10)

    # ---------------- EVENTO DO MOUSE ----------------

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

        # informações

        label_info.config(
            text=
            f"Posição: ({x}, {y})\n\n"
            f"RGB: ({r}, {g}, {b})\n\n"
            f"HEX: {hex_cor}"
        )

        # quadrado de cor

        label_cor.config(
            bg=hex_cor
        )

        # ---------------- LUPA ----------------

        inicio_x = max(0, x - 10)
        fim_x = min(largura_original, x + 10)

        inicio_y = max(0, y - 10)
        fim_y = min(altura_original, y + 10)

        regiao = imagem[
            inicio_y:fim_y,
            inicio_x:fim_x
        ]

        img_zoom = Image.fromarray(regiao)

        img_zoom = img_zoom.resize(
            (120, 120),
            Image.NEAREST
        )

        zoom_tk = ImageTk.PhotoImage(
            img_zoom
        )

        label_lupa.config(
            image=zoom_tk
        )

        label_lupa.image = zoom_tk

    label_img.bind(
        "<Motion>",
        mostrar_pixel
    )