import numpy as np

def converter(imagem):
    c = imagem[:, :, 0]
    m = imagem[:, :, 1]
    y = imagem[:, :, 2]

    r = (1 - c) * 255
    g = (1 - m) * 255
    b = (1 - y) * 255

    return np.dstack((r, g, b)).astype(np.uint8)