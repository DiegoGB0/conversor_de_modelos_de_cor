import numpy as np

def converter(imagem):
    imagem = imagem.astype(np.float32) / 255.0

    b = imagem[:, :, 0]
    g = imagem[:, :, 1]
    r = imagem[:, :, 2]

    k = 1 - np.maximum.reduce([r, g, b])

    c = np.where(k < 1, (1 - r - k) / (1 - k), 0)
    m = np.where(k < 1, (1 - g - k) / (1 - k), 0)
    y = np.where(k < 1, (1 - b - k) / (1 - k), 0)

    return np.dstack((c, m, y, k))