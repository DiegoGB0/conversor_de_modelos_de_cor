import numpy as np

'''def converter(imagem):
    imagem = imagem.astype(np.float32) / 255.0

    b = imagem[:, :, 0]
    g = imagem[:, :, 1]
    r = imagem[:, :, 2]

    k = 1 - np.maximum.reduce([r, g, b])

    c = np.where(k < 1, (1 - r - k) / (1 - k), 0)
    m = np.where(k < 1, (1 - g - k) / (1 - k), 0)
    y = np.where(k < 1, (1 - b - k) / (1 - k), 0)

    return np.dstack((c, m, y, k))'''


def converter(imagem):

    altura, largura, _ = imagem.shape

    resultado = np.zeros(
        (altura, largura, 4),
        dtype=np.float32
    )

    for linha in range(altura):
        for coluna in range(largura):

            b, g, r = imagem[linha, coluna]

            r = r / 255.0
            g = g / 255.0
            b = b / 255.0

            k = 1 - max(r, g, b)

            if k < 1:
                c = (1 - r - k) / (1 - k)
                m = (1 - g - k) / (1 - k)
                y = (1 - b - k) / (1 - k)
            else:
                c = 0
                m = 0
                y = 0

            resultado[linha, coluna] = [
                c,
                m,
                y,
                k
            ]

    return resultado