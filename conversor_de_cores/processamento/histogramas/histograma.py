import cv2
import matplotlib.pyplot as plt

def mostrar_histograma(imagem):

    cores = ("b", "g", "r")

    for i, cor in enumerate(cores):
        hist = cv2.calcHist(
            [imagem],
            [i],
            None,
            [256],
            [0, 256]
        )

        plt.plot(hist)

    plt.title("Histograma RGB")
    plt.xlabel("Intensidade")
    plt.ylabel("Quantidade de Pixels")

    plt.show()