import cv2
import os
import numpy as np

imagem = "entrada.png"

if os.path.exists(imagem):
    imagem = cv2.imread(imagem)
else:
    print(f"Erro: O arquivo '{imagem}' não foi encontrado.")
    exit()

while True:
    h = float(input("Digite um valor para H entre 0 e 360"))
    if 0 <= h <= 360:
        h /= 2
        break
    print("Digite um valor para H entre 0 e 360")

while True:
    d = float(input("Digite um valor para H entre 0 e 360"))
    if 0 <= d <= 180:
        d /= 2
        break
    print("Digite um valor para d entre 0 e 180")

imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV) #Converter RGB -> HSV

matiz = imagem_hsv[: , :, 0].astype(np.float32)
limite_superior = h + d
limite_inferior = h - d



