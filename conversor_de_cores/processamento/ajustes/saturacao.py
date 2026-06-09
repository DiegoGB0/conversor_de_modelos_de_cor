import cv2
import numpy as np

def aplicar_saturacao(imagem, valor):

    hsv = cv2.cvtColor(
        imagem,
        cv2.COLOR_RGB2HSV
    )

    fator = 1 + (valor / 100)

    hsv[:, :, 1] = np.clip(
        hsv[:, :, 1] * fator,
        0,
        255
    )

    return cv2.cvtColor(
        hsv,
        cv2.COLOR_HSV2RGB
    )