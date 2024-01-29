import random

def criar_quadrados_memoria(N):
    # Verifica se N é par para garantir que haverá pares de cores
    if N % 2 != 0:
        raise ValueError("N deve ser um número par para garantir pares de cores")

    # Lista de cores RGB
    cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
             (255, 0, 255), (0, 255, 255), (128, 0, 0), (0, 128, 0),
             (0, 0, 128), (128, 128, 0), (128, 0, 128), (0, 128, 128)]

    # Duplica a lista de cores para garantir pares suficientes
    cores *= 2

    # Embaralha as cores
    random.shuffle(cores)

    # Lista para armazenar os quadrados
    quadrados = []

    cor_idx = 0  # Índice para acessar as cores

    for i in range(N):
        for j in range(N):
            # Calcula as posições e a cor para cada quadrado
            x = i * N
            y = j * N
            lado = N
            revelado = False

            # Obtém a cor atual usando o índice
            cor = cores[cor_idx]
            cor_idx += 1

            # Cria o dicionário para o quadrado e o adiciona à lista
            quadrado = {'x': x, 'y': y, 'lado': lado, 'cor': cor, 'revelado': revelado}
            quadrados.append(quadrado)

    return quadrados

# Exemplo de uso com N=4
N = 4
quadrados_memoria = criar_quadrados_memoria(N)
print(quadrados_memoria)