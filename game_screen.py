import pygame
from config import FPS, WIDTH, HEIGHT, BLACK
from assets import carrega_arquivos
import random

def game_screen(window):
    clock = pygame.time.Clock()

    dicionario_de_arquivos = carrega_arquivos()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    N = 4

    def criar_quadrados_memoria(N):
        if N % 2 != 0:
            raise ValueError("N deve ser um número par para garantir pares de cores")

        cores = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                 (255, 0, 255), (0, 255, 255), (128, 0, 0), (0, 128, 0),
                 ]

        cores *= 2
        random.shuffle(cores)

        quadrados = []

        for i in range(N):
            for j in range(N):
                x = i * 150
                y = j * 150
                lado = 140
                revelado = False
                cor = cores.pop()  # Removendo a cor da lista
                quadrado = {'x': x, 'y': y, 'lado': lado, 'cor': cor, 'revelado': revelado}
                quadrados.append(quadrado)

        return quadrados

    quadrados_memoria = criar_quadrados_memoria(N)
    selecionados = []

    while state != DONE:
        clock.tick(FPS)

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
                            selecionados.append(quadrado)

                            if len(selecionados) == 2:
                                pygame.time.wait(500)  # Aguarda 0.5 segundo antes de esconder as cartas
                                if selecionados[0]['cor'] == selecionados[1]['cor']:
                                    quadrados_memoria.remove(selecionados[0])
                                    quadrados_memoria.remove(selecionados[1])
                                else:
                                    selecionados[0]['revelado'] = False
                                    selecionados[1]['revelado'] = False
                                selecionados = []

        window.fill(BLACK)

        for quadrado in quadrados_memoria:
            if quadrado['revelado']:
                pygame.draw.rect(window, quadrado['cor'], (quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))
            else:
                pygame.draw.rect(window, (255, 255, 255), (quadrado['x'], quadrado['y'], quadrado['lado'], quadrado['lado']))

        pygame.display.update()

        # Verifica se o jogador ganhou
        if not quadrados_memoria:
            state = DONE

    pygame.quit()

    return state

def colisao_ponto_retangulo(x_ponto, y_ponto, x_retangulo, y_retangulo, largura_retangulo, altura_retangulo):
    if x_retangulo <= x_ponto <= x_retangulo + largura_retangulo and y_retangulo <= y_ponto <= y_retangulo + altura_retangulo:
        return True
    else:
        return False
