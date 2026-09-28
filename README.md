# Trabalho 01 — Processamento Digital de Imagens

Programa em Python que altera a matiz de uma faixa de cores de uma imagem.

O usuário informa um valor de matiz `H` e uma distância `d`. O programa identifica os pixels dentro dessa faixa e desloca a matiz em 180 graus no círculo de cores. A imagem original não é modificada.

## Autores

- Mateus Scarpin Ribeiro — RA 128459
- Sergio de Almeida Cezar — RA 134680

## Requisitos

- Python 3
- NumPy
- OpenCV

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## Como executar

Na pasta do projeto, execute:

```bash
python main.py
```

O programa solicitará:

1. o nome ou caminho da imagem;
2. um valor de `H` entre 0 e 360 graus;
3. uma distância `d` entre 0 e 180 graus.

Exemplo:

```text
Digite o nome da imagem (ex: entrada.ext): entrada.png
Digite o valor para H (0 a 360):
120
Digite o valor para d (0 a 180):
30
```

## Resultado

A imagem processada é salva na mesma pasta da imagem original. O nome do arquivo inclui os valores informados de `H` e `d`.

No exemplo acima, o arquivo gerado será:

```text
entrada_H120_d30.png
```

Depois de salvar o resultado, o programa abre duas janelas para comparar a imagem original com a imagem modificada. Para processar outra imagem, feche uma das janelas.
