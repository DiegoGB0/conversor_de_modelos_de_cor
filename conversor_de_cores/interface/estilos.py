import customtkinter as ctk


def criar_titulo(master, texto):
    """Cria um título."""
    
    label = ctk.CTkLabel(
        master,
        text=texto,
        font=("Arial", 12, "bold")
    )

    label.pack()

    return label


def criar_label_ajuste(master, texto):
    """Cria um label para identificação dos ajustes."""

    label = ctk.CTkLabel(
        master,
        text=texto
    )

    label.pack(
        pady=(10, 0)
    )

    return label


def criar_grupo(master):
    """Cria um grupo de widgets alinhado à esquerda."""

    frame = ctk.CTkFrame(master)

    frame.pack(
        side="left",
        padx=15
    )

    return frame


def criar_divisoria(master):
    """Cria uma divisória vertical."""

    frame = ctk.CTkFrame(
        master,
        width=2,
        height=90,
        fg_color="lightgray"
    )

    frame.pack_propagate(False)

    frame.pack(
        side="left",
        padx=10,
        fill="y"
    )

    return frame


def criar_frame_botoes(master):
    """Cria um frame para botões."""

    frame = ctk.CTkFrame(master)

    frame.pack(
        fill="x",
        pady=15
    )

    return frame


def criar_frame_imagens(master):
    """Cria um frame para exibição de imagens."""

    frame = ctk.CTkFrame(master)

    frame.pack(
        side="left",
        padx=10,
        pady=10
    )

    return frame


def criar_frame_ajustes(master):
    """
    Cria um frame com título 'Ajustes',
    simulando um LabelFrame.
    """

    container = ctk.CTkFrame(master)

    container.pack(
        side="left",
        padx=20,
        pady=10,
        fill="y"
    )

    titulo = ctk.CTkLabel(
        container,
        text="Ajustes",
        font=("Arial", 14, "bold")
    )

    titulo.pack(
        pady=(10, 5)
    )

    frame_conteudo = ctk.CTkFrame(container)

    frame_conteudo.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=(0, 10)
    )

    return frame_conteudo