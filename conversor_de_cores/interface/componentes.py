import tkinter as tk


def criar_botao(master, texto, comando):

    botao = tk.Button(
        master,
        text=texto,
        command=comando,
        width=20
    )

    botao.pack(pady=5)

    return botao