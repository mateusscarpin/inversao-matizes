import cv2
import os
import numpy as np

# Mateus Scarpin Ribeiro RA128459
# Sergio de Almeida Cezar #134680

def validar_parametros(minimo, maximo):
    while True:
        try:
            valor = float(input())
            if minimo <= valor <= maximo:
                return valor
            print(f"O valor deve estar entre {minimo} e {maximo}.")
        except ValueError:
            print("Digite apenas números")


def inverter_matiz(imagem_bgr, h_usuario, d_usuario):
    imagem_hsv = cv2.cvtColor(imagem_bgr, cv2.COLOR_BGR2HSV)

    matiz_opencv = h_usuario / 2.0
    faixa_opencv = d_usuario / 2.0

    canal_matiz = imagem_hsv[:, :, 0].astype(np.float32)

    limite_inferior = matiz_opencv - faixa_opencv
    limite_superior = matiz_opencv + faixa_opencv

    if limite_inferior >= 0 and limite_superior <= 179:
        mascara = (canal_matiz >= limite_inferior) & (canal_matiz <= limite_superior)
    else:
        lim_inf_corrigido = limite_inferior % 180
        lim_sup_corrigido = limite_superior % 180
        mascara = (canal_matiz >= lim_inf_corrigido) | (canal_matiz <= lim_sup_corrigido)

    nova_matiz = canal_matiz.copy()
    nova_matiz[mascara] = nova_matiz[mascara] - 90

    nova_matiz = nova_matiz % 180

    imagem_hsv[:, :, 0] = nova_matiz.astype(np.uint8)

    return cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)


def main():
    largura_tela = 1920
    altura_tela = 1080

    while True:
        nome_imagem = input("Digite o nome da imagem (ex: entrada.ext): ").strip()

        if not os.path.exists(nome_imagem):
            print(f"\n[ERRO] O arquivo '{nome_imagem}' não foi encontrado. Tente novamente")
            continue

        imagem_original = cv2.imread(nome_imagem)

        print("Digite o valor para H (0 a 360): ")
        h_usuario = validar_parametros(0, 360)

        print("Digite o valor para d (0 a 180):")
        d_usuario = validar_parametros(0, 180)

        imagem_resultado = inverter_matiz(imagem_original, h_usuario, d_usuario)

        nome_sem_extensao, extensao = os.path.splitext(nome_imagem)
        nome_arquivo_saida = (
            f"{nome_sem_extensao}_H{int(h_usuario)}_d{int(d_usuario)}{extensao}"
        )

        cv2.imwrite(nome_arquivo_saida, imagem_resultado)

        print(f"Imagem salva como: '{nome_arquivo_saida}'")

        altura_imagem, largura_imagem = imagem_original.shape[:2]

        altura_janela = 650
        proporcao = altura_janela / float(altura_imagem)
        largura_janela = int(largura_imagem * proporcao)

        posicao_y = 100

        posicao_x_esquerda = 150
        posicao_x_direita = (largura_tela - largura_janela) - 550

        cv2.namedWindow("Imagem original", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Imagem original", largura_janela, altura_janela)
        cv2.moveWindow("Imagem original", posicao_x_esquerda, posicao_y)

        cv2.namedWindow("Imagem modificada", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Imagem modificada", largura_janela, altura_janela)
        cv2.moveWindow("Imagem modificada", posicao_x_direita, posicao_y)

        cv2.imshow("Imagem original", imagem_original)
        cv2.imshow("Imagem modificada", imagem_resultado)

        while True:
            if (
                cv2.getWindowProperty("Imagem original", cv2.WND_PROP_VISIBLE) < 1
                or cv2.getWindowProperty("Imagem modificada", cv2.WND_PROP_VISIBLE) < 1
            ):
                break

            cv2.waitKey(30)

        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
