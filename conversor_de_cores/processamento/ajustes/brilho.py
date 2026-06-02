import cv2

def aplicar(imagem, valor):
    return cv2.convertScaleAbs(
        imagem,
        alpha=1,
        beta=valor
    )