import numpy as np

def converter(imagem):
    imagem = imagem.astype(np.float32) / 255.0

    c = 1 - imagem[:, :, 2]
    m = 1 - imagem[:, :, 1]
    y = 1 - imagem[:, :, 0]

    return np.dstack((c, m, y))