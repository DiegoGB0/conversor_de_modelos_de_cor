import cv2

def aplicar_brilho(imagem, valor):

    return cv2.convertScaleAbs(
        imagem,
        alpha=1.0,
        beta=valor
    )