import tkinter as tk
import customtkinter as ctk
from interface.estilos import criar_label_ajuste


def criar_slider_brilho(master, comando):

    criar_label_ajuste(
        master,
        "Brilho"
    )

    slider = ctk.CTkSlider(
        master,
        from_=-100,
        to=100,
        orientation="horizontal",
        width=300,
        command=comando
    )

    slider.pack(
        padx=10,
        pady=5
    )

    return slider