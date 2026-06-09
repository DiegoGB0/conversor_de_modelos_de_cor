import numpy as np

'''def converter(imagem):
    imagem = imagem.astype(np.float32) / 255.0

    c = 1 - imagem[:, :, 2]
    m = 1 - imagem[:, :, 1]
    y = 1 - imagem[:, :, 0]

    return np.dstack((c, m, y))'''
    

def converter(imagem):

    altura, largura, _ = imagem.shape

    resultado = np.zeros(
        (altura, largura, 3),
        dtype=np.float32
    )

    for linha in range(altura):
        for coluna in range(largura):

            b, g, r = imagem[linha, coluna]

            r = r / 255.0
            g = g / 255.0
            b = b / 255.0

            c = 1 - r
            m = 1 - g
            y = 1 - b

            resultado[linha, coluna] = [c, m, y]

    return resultado