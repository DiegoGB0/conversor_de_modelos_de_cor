import cv2

def aplicar_contraste(imagem, valor):

    alpha = 1 + (valor / 100)

    return cv2.convertScaleAbs(
        imagem,
        alpha=alpha,
        beta=0
    )