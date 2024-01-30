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
                 ]

        cores *= 2
        random.shuffle(cores)

        quadrados = []

        cor_idx = 0

        for i in range(N):
            for j in range(N):
                x = i * 150
                y = j * 150
                lado = 140
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

    def verificar_correspondencia(quadrados, x_clicado, y_clicado):
        for i, quadrado in enumerate(quadrados):
            x = quadrado['x']
            y = quadrado['y']
            lado = quadrado['lado']

            if colisao_ponto_retangulo(x_clicado, y_clicado, x, y, lado, lado):
                if 'ultimo_clicado' not in globals():
                    global ultimo_clicado
                    ultimo_clicado = i
                else:
                    if quadrados[ultimo_clicado]['cor'] == quadrado['cor']:
                        del quadrados[i]
                        del quadrados[ultimo_clicado]
                    else:
                        quadrados[ultimo_clicado]['revelado'] = False
                        quadrados[i]['revelado'] = False

                    del globals()['ultimo_clicado']
    
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE  # Alteração aqui
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = pygame.mouse.get_pos()
                for quadrado in quadrados_memoria:
                    if not quadrado['revelado']:
                        if colisao_ponto_retangulo(pos_mouse[0], pos_mouse[1],
                                              quadrado['x'], quadrado['y'],
                                              quadrado['lado'], quadrado['lado']):
                            quadrado['revelado'] = True

                
                # logica verificar se tem dois quadrados como true
                            

        window.fill(BLACK)

        for quadrado in quadrados_memoria:
            if not quadrado['revelado']:
                pygame.draw.rect(window, (255, 255, 255), (quadrado['x']+140, quadrado['y']+70, quadrado['lado'], quadrado['lado']))
            else:
                pygame.draw.rect(window, quadrado['cor'], (quadrado['x']+140, quadrado['y']+70, quadrado['lado'], quadrado['lado']))

        pygame.display.update()


        #Etapa 5
        #Verifica se o jogador ganhou
        if not quadrados_memoria:
            state = DONE

# Encerre o jogo corretamente
    pygame.quit()

    return state
