import customtkinter as ctk


def criar_botao(master, texto, comando):

    botao = ctk.CTkButton(
        master,
        text=texto,
        command=comando,
        width=180,
        height=40,
        corner_radius=20
    )

    botao.pack(
        pady=5,
        padx=5
    )

    return botao