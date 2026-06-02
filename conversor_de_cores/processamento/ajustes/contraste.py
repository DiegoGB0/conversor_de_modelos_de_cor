import cv2

def aplicar(imagem, fator):
    return cv2.convertScaleAbs(
        imagem,
        alpha=fator,
        beta=0
    )