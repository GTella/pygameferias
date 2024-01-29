import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    N = 4  # Defina o valor de N conforme desejado

    # Função para criar quadrados do jogo da memória
    def criar_quadrados_memoria(N):
        if N % 2 != 0:
            raise ValueError("N deve ser um número par para garantir pares de cores")

        cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                 (255, 0, 255), (0, 255, 255), (128, 0, 0), (0, 128, 0),
                 (0, 0, 128), (128, 128, 0), (128, 0, 128), (0, 128, 128)]

        cores *= 2
        random.shuffle(cores)

        quadrados = []

        cor_idx = 0

        for i in range(N):
            for j in range(N):
                x = i * N
                y = j * N
                lado = N
                revelado = False
                cor = cores[cor_idx]
                cor_idx += 1
                quadrado = {'x': x, 'y': y, 'lado': lado, 'cor': cor, 'revelado': revelado}
                quadrados.append(quadrado)

        return quadrados

    # Função para verificar colisão de um ponto com um retângulo
    def colisao_ponto_retangulo(x_ponto, y_ponto, x_retangulo, y_retangulo, largura_retangulo, altura_retangulo):
        if x_retangulo <= x_ponto <= x_retangulo + largura_retangulo and y_retangulo <= y_ponto <= y_retangulo + altura_retangulo:
            return True
        else:
            return False

    quadrados_memoria = criar_quadrados_memoria(N)

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for quadrado in quadrados_memoria:
                    if not quadrado['revelado']:
                        if colisao_ponto_retangulo(pos_mouse[0], pos_mouse[1],
                                                  quadrado['x'], quadrado['y'],
                                                  quadrado['lado'], quadrado['lado']):
                            quadrado['revelado'] = True

        window.fill(BLACK)

        for quadrado in quadrados_memoria:
            if not quadrado['revelado']:
                pygame.draw.rect(window, (255, 255, 255), (quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))
            else:
                pygame.draw.rect(window, quadrado['cor'], (quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))

        pygame.display.update()
    return state
