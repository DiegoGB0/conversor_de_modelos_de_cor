import cv2

def aplicar(imagem, fator):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    hsv[:, :, 1] = cv2.multiply(
        hsv[:, :, 1],
        fator
    )

    return cv2.cvtColor(
        hsv,
        cv2.COLOR_HSV2BGR
    )