import random
from etapa4 import lado
def criar_quadrados_memoria(N, largura_tela, altura_tela):
    if N % 2 != 0:
        raise ValueError("N deve ser um número par para garantir pares de cores")

    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
             (255, 0, 255), (0, 255, 255), (128, 0, 0), (0, 128, 0),
             (0, 0, 128), (128, 128, 0), (128, 0, 128), (0, 128, 128)]

    cores *= 2
    random.shuffle(cores)

    quadrados = []

    cor_idx = 0

    # Ajuste para centralizar os quadrados na tela
    margem_horizontal = (largura_tela - N * lado) // 2
    margem_vertical = (altura_tela - N * lado) // 2

    for i in range(N):
        for j in range(N):
            x = margem_horizontal + i * lado
            y = margem_vertical + j * lado
            revelado = False
            cor = cores[cor_idx]
            cor_idx += 1
            quadrado = {'x': x, 'y': y, 'lado': lado, 'cor': cor, 'revelado': revelado}
            quadrados.append(quadrado)

    return quadrados