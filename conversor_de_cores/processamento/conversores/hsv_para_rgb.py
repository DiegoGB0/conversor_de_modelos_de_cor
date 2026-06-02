import cv2

def converter(imagem):
    return cv2.cvtColor(
        imagem,
        cv2.COLOR_HSV2BGR
    )