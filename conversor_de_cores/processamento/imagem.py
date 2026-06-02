import numpy as np
from PIL import Image

def abrir_imagem(caminho):
    return Image.open(caminho)

def converter_para_numpy(imagem):
    return np.array(imagem)

def converter_para_pil(imagem):
    return Image.fromarray(imagem)