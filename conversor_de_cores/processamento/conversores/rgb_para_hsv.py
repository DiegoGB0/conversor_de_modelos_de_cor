import cv2
import numpy as np

'''def converter(imagem):
    return cv2.cvtColor(
        imagem,
        cv2.COLOR_RGB2HSV
    )'''
    

def converter(imagem):

    altura, largura, _ = imagem.shape

    resultado = np.zeros(
        (altura, largura, 3),
        dtype=np.uint8
    )

    for linha in range(altura):
        for coluna in range(largura):

            b, g, r = imagem[linha, coluna]

            r = r / 255.0
            g = g / 255.0
            b = b / 255.0

            maximo = max(r, g, b)
            minimo = min(r, g, b)

            delta = maximo - minimo

            # H
            if delta == 0:
                h = 0

            elif maximo == r:
                h = 60 * (((g - b) / delta) % 6)

            elif maximo == g:
                h = 60 * (((b - r) / delta) + 2)

            else:
                h = 60 * (((r - g) / delta) + 4)

            # S
            if maximo == 0:
                s = 0
            else:
                s = delta / maximo

            # V
            v = maximo

            # Ajuste para faixa OpenCV
            h = int(h / 2)
            s = int(s * 255)
            v = int(v * 255)

            resultado[linha, coluna] = [h, s, v]

    return resultado